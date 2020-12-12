from pathlib import Path
import pytest
from src.sentence import Sentence


@pytest.fixture
def word_collection_file_path() -> Path:
    return (Path(__file__).parent
            / "fixtures"
            / "full_word_list.txt").resolve()


@pytest.fixture
def mock_sentence(word_collection_file_path: Path) -> 'Sentence':
    """Create a mock instance of the Scentence class for test case."""
    test_data = "Hello, World! The start of most programmers adventures."
    return Sentence(test_data, word_collection_file_path)


class TestSentence():

    def test_remove_punctuation(self, word_collection_file_path: Path):
        """Test case for  punctuation from the Sentence."""
        test_data = "Hello, World! The start of most programmers adventures."
        expected_res = "Hello World The start of most programmers adventures"
        sentence = Sentence(test_data, word_collection_file_path)
        assert isinstance(sentence, Sentence)
        assert sentence.org_sentence == test_data
        assert sentence.no_punct_sent == expected_res

    def test_splitting_words(self, mock_sentence: 'Sentence'):
        assert mock_sentence.words == ["Hello",
                                       "World",
                                       "The",
                                       "start",
                                       "of",
                                       "most",
                                       "programmers",
                                       "adventures"]

    def test_replacing_words(self, mock_sentence: 'Sentence'):
        """Test case for replacing words."""
        rep_sentence = mock_sentence.replace_words()
        assert mock_sentence != rep_sentence
        for rep_word, word in zip(rep_sentence.split(" "),
                                  mock_sentence.no_punct_sent.split(" ")):
            assert rep_word != word
            assert len(rep_word) == len(word)
            print(f"{word} -> {rep_word}")
            assert rep_word[0].lower() == word[0].lower()
