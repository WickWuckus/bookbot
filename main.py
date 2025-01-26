def main():
    print(f"--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        def wordcount():
            words = file_contents.split()
            word_count = len(words)
            print(f"{word_count} words found in this document")
            print("                                          ")
        wordcount()
        def lettercount():
            lower_case = file_contents.lower()
            letter_count = {}

            for char in lower_case:
                if char.isalpha():
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1
            dict_list = []
            for letter, count in letter_count.items():
                dict_list.append({"letter":letter, "count":count})

            sorted_dict_list = sorted(dict_list, key=lambda x: x["count"], reverse=True)
            for dictionary in sorted_dict_list:
                print(f"The '{dictionary['letter']}' character was found {dictionary['count']} times")
        lettercount()
    print("--- End report ---")
if __name__ == "__main__":
    main()