
def main():
    book_path = "books/frankenstein.txt"
    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = character_count(text)
    print(f"{num_words} words found in the document\n\n")
    for k, v in characters:
        if k in alphabet:
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    #save in case I need ALL chars, not just letters
    alphabet = set()
    #alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    for char in text.lower():
        alphabet.add(char)
    counter_dict = dict.fromkeys(alphabet, 0)
    for char in text.lower():
        counter_dict[char] += 1
    sorted_counter_dict = sorted(counter_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_counter_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()