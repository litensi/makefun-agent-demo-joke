from pathlib import Path


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    joke = "Our live demo crashed when I clicked Export. My AI coding agent shipped a fix. The front row had one question: “Where’s Export?”"
    (output / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
