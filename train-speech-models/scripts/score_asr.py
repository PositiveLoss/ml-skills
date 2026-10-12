"""Score corpus WER/CER with explicit normalization and edit counts."""
import argparse
import json
from pathlib import Path
import unicodedata


def edit_counts(reference, hypothesis):
    # Cell: cost, substitutions, deletions, insertions. Preserve one deterministic optimal path.
    previous = [(j, 0, 0, j) for j in range(len(hypothesis) + 1)]
    for i, ref in enumerate(reference, 1):
        current = [(i, 0, i, 0)]
        for j, hyp in enumerate(hypothesis, 1):
            diagonal = previous[j - 1]
            delta = int(ref != hyp)
            substitution = (diagonal[0] + delta, diagonal[1] + delta, diagonal[2], diagonal[3])
            above, left = previous[j], current[j - 1]
            deletion = (above[0] + 1, above[1], above[2] + 1, above[3])
            insertion = (left[0] + 1, left[1], left[2], left[3] + 1)
            current.append(min((substitution, deletion, insertion), key=lambda item: item[0]))
        previous = current
    cost, substitutions, deletions, insertions = previous[-1]
    return {"edits": cost, "substitutions": substitutions, "deletions": deletions, "insertions": insertions}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcripts", type=Path)
    parser.add_argument("--normalization", choices=("NFC", "NFKC", "none"), default="NFC")
    parser.add_argument("--lowercase", action="store_true")
    parser.add_argument("--include-spaces", action="store_true")
    parser.add_argument("--max-characters", type=int, default=10000)
    parser.add_argument("--max-edit-cells", type=int, default=4000000)
    args = parser.parse_args()
    if args.max_characters < 1:
        parser.error("max-characters must be positive")
    if args.max_edit_cells < 1:
        parser.error("max-edit-cells must be positive")
    def normalize(text):
        result = unicodedata.normalize(args.normalization, text) if args.normalization != "none" else text
        return result.lower() if args.lowercase else result
    rows, seen, totals = [], set(), {"words": 0, "characters": 0, "word_edits": 0, "character_edits": 0, "empty_references": 0}
    try:
        with args.transcripts.open(encoding="utf-8") as stream:
            for number, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                row = json.loads(line)
                if not isinstance(row, dict) or any(not isinstance(row.get(key), str) for key in ("sample_id", "reference", "hypothesis")):
                    raise ValueError(f"line {number}: string fields required")
                sid = row["sample_id"]
                if not sid.strip() or sid in seen:
                    raise ValueError(f"line {number}: sample_id must be unique and nonempty")
                if max(len(row["reference"]), len(row["hypothesis"])) > args.max_characters:
                    raise ValueError(f"line {number}: transcript exceeds length limit")
                seen.add(sid)
                ref, hyp = normalize(row["reference"]), normalize(row["hypothesis"])
                if max(len(ref), len(hyp)) > args.max_characters:
                    raise ValueError(f"line {number}: normalized transcript exceeds length limit")
                ref_words, hyp_words = ref.split(), hyp.split()
                if not args.include_spaces:
                    ref = "".join(ref_words)
                    hyp = "".join(hyp_words)
                if max(len(ref) * len(hyp), len(ref_words) * len(hyp_words)) > args.max_edit_cells:
                    raise ValueError(f"line {number}: edit-distance work exceeds max-edit-cells")
                word, char = edit_counts(ref_words, hyp_words), edit_counts(ref, hyp)
                totals["words"] += len(ref_words)
                totals["characters"] += len(ref)
                totals["word_edits"] += word["edits"]
                totals["character_edits"] += char["edits"]
                totals["empty_references"] += int(not ref_words)
                rows.append({"sample_id": sid, "word": word, "character": char})
        if not rows:
            raise ValueError("transcript data must not be empty")
    except (ValueError, OSError, TypeError) as error:
        parser.error(str(error))
    result = {"wer": totals["word_edits"] / totals["words"] if totals["words"] else None,
              "cer": totals["character_edits"] / totals["characters"] if totals["characters"] else None,
              "totals": totals, "utterances": rows, "normalization": args.normalization,
              "lowercase": args.lowercase, "cer_includes_spaces": args.include_spaces,
              "empty_reference_policy": "Count insertions in the corpus numerator; undefined if total reference length is zero."}
    print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == "__main__":
    main()
