import sys
from stats import get_num_words, get_chars_dict, get_sorted_list

def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
   
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    char_count = get_chars_dict(text)
    sorted_counts = get_sorted_list(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============== END ==============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()
