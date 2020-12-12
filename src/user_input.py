"""Use parsed arguments to run the sentence replacement application."""
import argparse
from pathlib import Path

from sentence import Sentence

DEFAULT_WORD_FILE_PATH = (Path(__file__).parent
                          / 'static'
                          / 'word_collection.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sentence', help='A sentence to replace words on.')
    parser.add_argument('--word_file',
                        type=argparse.FileType('r'),
                        default=DEFAULT_WORD_FILE_PATH,
                        help='A file path to a file containing words.'
                             'These words will be used for word replacements.')

    args = parser.parse_args()
    sentence = Sentence(args.sentence, args.word_file)

    # Used to provide output back to the active tty.
    print(sentence.replace_words())  # noqa:T001
