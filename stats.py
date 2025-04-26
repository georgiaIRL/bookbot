def word_count(bookText):
    splitText = bookText.split()
    wordCount = 0
    for words in splitText:
        wordCount += 1
    return wordCount 

def char_count(bookText):
    text = bookText.lower()
    charCount = {}
    for char in text:
        if char in charCount:
            charCount[char] += 1 
        else:
            charCount[char] = 1
    return charCount

def char_sort(char_count):
    # First, convert your dictionary to a list of dictionaries with "char" and "num" keys
    chars_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)
        # What should you append to chars_list here?
        
    # Define your sorting helper function
    def sort_on(dict_item):
        return dict_item["num"]
    
    # Now sort the list
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

