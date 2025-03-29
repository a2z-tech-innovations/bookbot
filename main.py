import sys
from stats import get_char_count, get_num_words, get_sorted_chars

def print_report(path, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    # Get sorted characters and print them
    sorted_chars = get_sorted_chars(char_counts)
    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['count']}")

    print("============= END ===============")

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get book path from command line argument
    path = sys.argv[1]

    try:
        with open(path) as f:
            book_text = f.read()

        word_count = get_num_words(book_text)
        char_counts = get_char_count(book_text.lower())
        print_report(path, word_count, char_counts)

    except FileNotFoundError:
        print(f"Error: Could not find file at {path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
