from pathlib import Path


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    joke = "The live demo crashed; my AI coding agent patched it in nine seconds and filed the postmortem with one line: root cause, human clicked Export."
    (output / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
