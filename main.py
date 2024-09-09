
def get_words_num(txt):
  words = txt.split()
  return len(words)

def get_book_text(path):
   with open(path) as f:
    return f.read()
   
def get_letters_dict(txt):
 characters = {}
 for char in txt:
  char = char.lower()
  if char in characters:
    characters[char] += 1
  else:
    characters[char] = 1
 return characters


def sort_on(dict):
    return dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    s_list = []
    for ch in num_chars_dict:
        s_list.append({"char": ch, "num": num_chars_dict[ch]})
    s_list.sort(reverse=True, key=sort_on)
    return s_list


def data_report(path):
  book_text = get_book_text(path)
  words_num = get_words_num(book_text)
  dict_characters = get_letters_dict(book_text)
  list_chars = chars_dict_to_sorted_list(dict_characters)
  print(f"--- Begin report of {path} ---")
  print(f"{words_num} words found in the document\n")
  for item in list_chars:
    if item["char"].isalpha():
     print(f"The '{item['char']}' character was found {item['num']} times")
  print("--- End report ---")


def main():
    path = "books/frankenstein.txt"
    data_report(path)


main()

