import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(filepath):
    """Return the contents of a text file as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # Check that exactly one argument (the file path) was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book from the command line
    filepath = sys.argv[1]

    # Read the book text
    text = get_book_text(filepath)

    # Count words and characters
    num_words = count_words(text)
    char_dict = count_characters(text)
    sorted_chars = sort_characters(char_dict)

    # Print results
    print(f"Found {num_words} total words\n")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


if __name__ == "__main__":
    main()
