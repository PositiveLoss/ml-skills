"""Check a small CPU training loop and an in-memory checkpoint round trip."""
import argparse
import copy
import json
import math


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=40)
    parser.add_argument("--seed", type=int, default=17)
    args = parser.parse_args()
    if args.steps < 2 or args.steps > 10000:
        parser.error("steps must be between 2 and 10000")
    import torch
    torch.set_num_threads(1)
    torch.manual_seed(args.seed)
    torch.use_deterministic_algorithms(True)
    X = torch.randn(64, 4)
    y = (X[:, 0] + .5 * X[:, 1] > 0).long()
    def make():
        model = torch.nn.Sequential(torch.nn.Linear(4, 8), torch.nn.Tanh(), torch.nn.Dropout(.1), torch.nn.Linear(8, 2))
        optimizer = torch.optim.Adam(model.parameters(), lr=.03)
        return model, optimizer
    model, optimizer = make()
    initial = copy.deepcopy(model.state_dict())
    criterion = torch.nn.CrossEntropyLoss()
    losses = []
    checkpoint = None
    boundary = args.steps // 2
    def step(network, opt):
        network.train()
        opt.zero_grad(set_to_none=True)
        loss = criterion(network(X), y)
        assert torch.isfinite(loss)
        loss.backward()
        assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in network.parameters())
        opt.step()
        return float(loss.detach())
    for index in range(args.steps):
        losses.append(step(model, optimizer))
        if index + 1 == boundary:
            checkpoint = {"model": copy.deepcopy(model.state_dict()), "optimizer": copy.deepcopy(optimizer.state_dict()),
                          "rng": torch.get_rng_state().clone()}
    assert math.isfinite(losses[-1]) and losses[-1] < losses[0]
    assert any(not torch.equal(initial[k], model.state_dict()[k]) for k in initial)
    resumed, resumed_optimizer = make()
    resumed.load_state_dict(checkpoint["model"])
    resumed_optimizer.load_state_dict(checkpoint["optimizer"])
    torch.set_rng_state(checkpoint["rng"])
    for _ in range(boundary, args.steps):
        step(resumed, resumed_optimizer)
    assert all(torch.equal(a, resumed.state_dict()[key]) for key, a in model.state_dict().items())
    model.eval()
    with torch.inference_mode():
        first, second = model(X), model(X)
    assert torch.equal(first, second)
    print(json.dumps({"ok": True, "torch": torch.__version__, "device": "cpu", "seed": args.seed,
                      "steps": args.steps, "initial_loss": losses[0], "final_loss": losses[-1],
                      "checkpoint_resume_equal": True, "eval_repeatable": True,
                      "scope": "Synthetic full-batch CPU fixture; no GPU, AMP, data-worker or distributed claims."}, indent=2))


if __name__ == "__main__":
    main()
