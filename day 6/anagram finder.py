from collections import defaultdict

def find_anagrams(word_list):

    anagram_dict = defaultdict(list)
    
   
    for word in word_list:
     
        sorted_word = "".join(sorted(word))
        anagram_dict[sorted_word].append(word)
    
   
    anagram_sets = [words for words in anagram_dict.values() if len(words) > 1]
    
    return anagram_sets

def main():
    
    word_list = input("Enter a list of words separated by spaces: ").split()
    
   
    anagram_sets = find_anagrams(word_list)
    for i, anagram_set in enumerate(anagram_sets):
        print(f"Anagram Set {i+1}: {anagram_set}")

if __name__ == "__main__":
    main()