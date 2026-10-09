from pathlib import Path


def main():
    folder = Path(__file__).resolve().parent / "data"
    files = sorted(folder.glob("*.txt"))

    if not files:
        print(f"No .txt files found in {folder}")
        return

    results = []
    for file_path in files:
        text = file_path.read_text(encoding="utf-8")
        word_count = len(text.split())
        results.append((file_path.name, word_count))
        print(f"{file_path.name}: {word_count} words")

    total_words = sum(count for _, count in results)
    largest_file = max(results, key=lambda item: item[1])
    smallest_file = min(results, key=lambda item: item[1])

    print(f"\nTOTAL_WORDS: {total_words}")
    print(f"LARGEST: {largest_file[0]} ({largest_file[1]} words)")
    print(f"SMALLEST: {smallest_file[0]} ({smallest_file[1]} words)")


if __name__ == "__main__":
    main()
