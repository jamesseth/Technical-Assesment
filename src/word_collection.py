from pathlib import Path
import random
from typing import Union


class WordCollection:

    def __init__(self, file_path: Union[Path, str]):
        self.input_file: Path = Path(file_path)
        self.words = self.get_words_from_file()
        self.__orignal_words = self.words

    def get_words_from_file(self) -> dict:
        """
        Get words from file.

        :return: A dictionary of words with the first letter as the key and the
                 value a list of the words starting with that letter in the file.
        """
        words = dict()
        if self.input_file.exists() and self.input_file.is_file():
            with self.input_file.open('r', encoding='utf-8') as fin:
                for line in fin.readlines():
                    word = (line
                            .replace('\n', '')
                            .replace('\r', '')
                            .strip()
                            .lower())

                    first_letter = word[0]
                    if first_letter not in words.keys():
                        words[first_letter] = []

                    words[first_letter].append(word)

        for letter, word_list in words.items():
            words[letter] = sorted(word_list, key=str.lower)

        return words

    def restore_words_for(self, letter):
        self.words[letter] = self.__orignal_words[letter]

    def find_replacement_word(self, word: str) -> str:
        """
        Find a word from the collection to replace the parsed word.

        The word must start with the same character and must have same length.
        If no word is found matching the predicate above return the original
        word.
        :param word: The word to replace.
        :return: Replacement word matching the predicate otherwise the parsed 
                 word.
        """
        if not word or not isinstance(word, str) or len(word) < 1:
            raise ValueError("The parsed word to replace must be of type str"
                             "and have length greater than 0."
                             f"Got {word}")

        first_letter = word[0].lower()
        word_length = len(word)

        if first_letter in self.words.keys():
            if len(self.words[first_letter]) < 1:
                self.restore_words_for(first_letter)
            num_words = len(self.words[first_letter])
            for rep_word in random.sample(self.words[first_letter], num_words):
                if (rep_word.startswith(first_letter) and
                        len(rep_word) == word_length):
                    self.words[first_letter].remove(rep_word)
                    return rep_word
        return word
