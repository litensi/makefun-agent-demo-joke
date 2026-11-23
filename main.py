from pathlib import Path


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    joke = "Our live demo crashed. My AI coding agent patched it. Now when it crashes, the app says, “Any questions?”"
    (output / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
