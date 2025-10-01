from stats import get_num_words, letters_count, sorted_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
   
    
    num_words = get_num_words(text)
    counts = letters_count(text)

        
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter, n in sorted_list(counts):
        if letter.isalpha():
            print(f"{letter}: {n}")    
    print("============ END ==============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
