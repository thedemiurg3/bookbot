import sys
from stats import get_sorted_char_counts, get_char_counts, get_num_words

def get_book_text(filepath):
    """Reads and returns the contents of a file as a string."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    book_text = get_book_text(book_path)
    
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    char_counts = get_char_counts(book_text)
    sorted_counts = get_sorted_char_counts(char_counts)
    
    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()

