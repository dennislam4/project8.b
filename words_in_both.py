# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/21/2022
# Description: A function that takes two strings as parameters and returns a set of only
# those words that appear in both strings.

def words_in_both(first_sentence, second_sentence):
    """
    A function that takes from two separate strings into a list of strings and returns the
    words that are in both strings.
    """
    first_words = first_sentence.lower().split(" ")
    second_words = second_sentence.lower().split(" ")
    same_words = []
    for word in first_words:
        if (word in second_sentence) and (word not in same_words):
            same_words.append(word)
    return same_words

