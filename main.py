from stats import word_count
from stats import char_count
from stats import char_sort
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        bookText = f.read()
    return bookText 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    text = get_book_text(book)

    wordCount = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")

    charCount = char_count(text)
    charSort = char_sort(charCount)
    print("--------- Character Count -------")
    # Loop through your sorted_chars list
    for char_dict in charSort:
        char = char_dict["char"]
        # Check if the character is alphabetical
        if char.isalpha():
            count = char_dict["num"]
            print(f"{char}: {count}")
    
    print("============= END ===============")
    return 

main()    