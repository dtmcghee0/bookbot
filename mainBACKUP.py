import sys
from stats import count_words, count_characters, get_book_text, sort_characters

def get_book_text(filepath):
    "Return the contents of a text file as a string"
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read
    
def main():
    # Check that exactly one argument (the file path) was provided
    if len(sys.argv) != 2:
        print("Usage: python main.py books/frankenstein.txt") #books/frankenstein.txt
        sys.exit(1)

    # Get the path to the book from the command line
    filepath = sys.argv[1]

    # Read the book text
    text = get_book_text(filepath)
    
    # text = get_book_text("books/frankenstein.txt") #books/frankenstein.txt

    num_words = count_words(text)
    char_dict = count_characters(text)
    sorted_chars = sort_characters(char_dict)

    for entry in sorted_chars[:100]:
        print(f"{entry['char']}: {entry['num']}")

    """num_words = count_words(text)
    char_counts = count_characters(text)

    print(f"Found {num_words} total words")
    print(f"Character counts: {char_counts}")
    """

#  This function uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
#def main():
#    filepath = "books/frankenstein.txt"
 #   text = get_book_text(filepath)
 #   print(text)

main()



