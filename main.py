from pathlib import Path


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    joke = "My agent fixed the demo crash in nine seconds and committed straight to main. The message: \u201cworks on stage.\u201d"
    (output / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
