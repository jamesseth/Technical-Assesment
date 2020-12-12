"""
Implement a class object to represent a sentence.
Provide common utilities.
"""
import re
from typing import Union
from pathlib import Path
from word_collection import WordCollection


class Sentence:
    """
    Create a Sentence instance.

    Handle basic filtering and word replacements.
    :param sentence: A sentence to perform word replacement on.
    :param word_file_path: A path to a file containing the words to use for
                           replacement.
    """

    def __init__(self, sentence: str, word_file_path: Union[Path, str]):
        """
        Create a Sentence instance.

        Handle basic filtering and word replacements.
        :param sentence: A sentence to perform word replacement on.
        :param word_file_path: A path to a file containing the words to use for
                                replacement.
        """
        self.org_sentence = sentence
        self.no_punct_sent = re.sub(r'[^\w\s]', '', sentence)
        self.words = [word.strip() for word in self.no_punct_sent.split(' ')]
        self.word_collection = WordCollection(word_file_path)

    def replace_words(self) -> str:
        """
        Replace words in the sentence with words from the word collection.

        :return: Return the sentence with the replace words that started with
                 the same letter and had the same length
        """
        for index, word in enumerate(self.words):
            self.words[index] = self.word_collection.find_replacement_word(
                word)
        return " ".join(self.words)

    def __str__(self) -> str:
        """
        Return a string representation of the current instance.

        :return: A string representation of the current instance.
        """
        return " ".join(self.words)
