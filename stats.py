# This function takes a filepath as input and returns the contents of the file as a string
def get_book_text(filepath):
    "Return the contents of a text file as a string"
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# This function accepts the text from the book as a string, and returns the number of words in the string.
def count_words(text):
    "Return the number of words in the given text string."
    words = text.split() #split the text into a list of words by whitespace
    return len(words)

def count_characters(text):
    "Return a dictionary mapping each character (lowercased) to the number of times it appears in the text."
    char_counts = {}
    for char in text.lower(): #convert each character to lowercase
        if not char.isalpha(): # skip anything thats not a letter
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_dict):
    "Takes a dictionary of characters and counts, and returns a sorted list of dictionaries in descending orfer by count."

    # Convert the char_dict into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]

    # Define a helper function to get the 'num' key for sorting
    def sort_on(item):
        return item["num"]
    
    # Sort the list in-place from greatest to least
    char_list.sort(reverse=True, key=sort_on)

    return char_list

# Instead of printing the books contents, print this message to the console: Found {num_words} total words
"""def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

# call main to execute the program
main()
"""