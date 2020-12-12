from pathlib import Path
import json
import random

import pytest

from src.word_collection import WordCollection


@pytest.fixture
def mock_word_collection() -> 'WordCollection':
    """
    Create a mock instance of the WordCollection class.

    :return: A WordCollection instance for the test case.
    """
    test_file_path = (Path(__file__).parent
                      / "fixtures"
                      / "test_words.txt").resolve()
    assert test_file_path.exists() is True
    return WordCollection(test_file_path)


@pytest.fixture
def full_word_list_collection() -> 'WordCollection':
    """
    Get the full list of words for tests.

    :return: A WordCollection instance containing entire word collection.
    """
    test_file_path = (Path(__file__).parent
                      / "fixtures"
                      / "full_word_list.txt").resolve()
    assert test_file_path.exists() is True
    return WordCollection(test_file_path)


def random_string() -> str:
    """
    Create a random string with a length between 1 character and 10.

    :return: A random string of characters.
    """
    result = ""
    for _ in range(random.randint(1, 10)):
        result += random.choice("abcdefghijklmnopqrstuvwxyz")
    return result


@pytest.fixture
def expected_test_words() -> dict:
    """
    Get expected words for test case.

    :return: A dictionary with the first letter as the key and a list of words
             that start with the letter used for the key.
    """
    test_word_file_path = Path(__file__).parent / \
        "fixtures" / "expected_words.json"
    with test_word_file_path.open('r') as fin:
        return json.load(fin)
    return dict()


class TestWordCollection:

    def test_init(self):
        """Test case for instanciating a WordCollection instance."""
        test_file_path = (Path(__file__).parent
                          / "fixtures"
                          / "test_words.txt").resolve()
        assert test_file_path.exists() is True
        word_collection = WordCollection(test_file_path)
        assert isinstance(word_collection, WordCollection)
        assert hasattr(word_collection, 'input_file')
        assert word_collection.input_file == test_file_path

    def test_get_words_from_file(self,
                                 mock_word_collection: dict,
                                 expected_test_words: dict):
        """Test case for getting words from file."""
        test_words = mock_word_collection.get_words_from_file()
        num_words = len(test_words.keys())

        total_word_count = 0
        for list_of_words in test_words.values():
            total_word_count += len(list_of_words)

        assert total_word_count == 100
        assert test_words == expected_test_words
        assert num_words == 22

    def test_replacement_word(self, mock_word_collection: 'WordCollection'):
        test_word = "Canvas"
        res = mock_word_collection.find_replacement_word(test_word)
        assert res.startswith(test_word[0])
        assert len(res) == len(test_word)

    def test_random_word_replacement(self,
                                     full_word_list_collection: 'WordCollection'):
        test_word = "test"
        prev_word = ""
        number_of_runs = 1000
        while number_of_runs > 0:
            rep_word = full_word_list_collection.find_replacement_word(
                test_word)
            assert prev_word != rep_word
            if test_word == rep_word:
                prev_word = rep_word
                test_word = random_string()

            number_of_runs -= 1

        assert number_of_runs == 0
