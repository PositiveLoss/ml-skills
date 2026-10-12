# Task reference

Gymnasium returns terminated and truncated separately; their learning-target implications depend on the task definition. Episode reward is not automatically the desired real-world objective. Correlated trajectories and changing policies complicate confidence estimates. Offline policy evaluation has assumptions that must be stated and checked.

Primary sources:
- https://gymnasium.farama.org/api/env/
- https://spinningup.openai.com/en/latest/spinningup/rl_intro.html
