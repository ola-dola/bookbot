from collections import Counter
from stats import get_num_words
import sys


def count_chars(text):
    # counter = Counter(text.lower())
    # return counter
    counter = {}
    for char in text.lower():
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter   


def convert_dict(dict):
    characters_list = []
    for key, val in dict.items():
        characters_list.append({"name": key, "count": val})
    return characters_list


def sort_on(dict):
    return dict["count"]


def print_details(file, file_name):
    num_of_words = get_num_words(file)
    chars = count_chars(file)
    chars_sorted = sorted(convert_dict(chars), key=sort_on, reverse=True)

    print(f"--- Begin report of {file_name} ----")
    print(f"{num_of_words} words found in the document \n")

    for item in chars_sorted:
        if not item["name"].isalpha():
            continue

        print(f"The '{item['name']}' character was found {item['count']} times")

    print(f"\n --- End report ----")


def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) == 1:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
      
    book_path = sys.argv[1]

    with open(book_path) as f:
        file = f.read()
        print_details(file, book_path)


main()
