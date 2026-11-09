"""Module for comparing text files using k-shingle multiset Jaccard similarity."""

import argparse
import string
from collections import Counter
from shingle import shingles

def jaccard_similarity(counter1, counter2):
    """Calculates the Jaccard similarity index between two multiset counters.

    Args:
        counter1 (Counter): Multiset of shingles from the first text.
        counter2 (Counter): Multiset of shingles from the second text.

    Returns:
        float: Jaccard similarity score ranging from 0.0 to 1.0.

    Raises:
        TypeError: If counter1 or counter2 are not Counter instances.
    """
    if not isinstance(counter1, Counter) or not isinstance(counter2, Counter):
        raise TypeError("Arguments must be Counter instances")

    intersection = counter1 & counter2
    union = counter1 | counter2

    total_intersection = sum(intersection.values())
    total_union = sum(union.values())

    if total_union == 0:
        return 0.0

    return total_intersection / total_union


def tokenize(text, remove_punctuation=False):
    """Splits input text into word tokens with optional punctuation removal.

    Args:
        text (str): Input text string.
        remove_punctuation (bool): If True, strips all punctuation marks.

    Returns:
        list of str: List of extracted word tokens.

    Raises:
        TypeError: If text is not a string or remove_punctuation is not a boolean.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(remove_punctuation, bool):
        raise TypeError("remove_punctuation must be a boolean")

    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()


def main():
    """Parses arguments and calculates Jaccard similarity between two files."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", default="text1.txt")
    parser.add_argument("--target", default="text2.txt")
    parser.add_argument("-k", type=int, default=2)
    parser.add_argument("--remove_punctuation", action="store_true")

    args = parser.parse_args()

    with open(args.query) as f:
        text1 = f.read()

    with open(args.target) as f:
        text2 = f.read()

    tokens1 = tokenize(text1, args.remove_punctuation)
    tokens2 = tokenize(text2, args.remove_punctuation)

    counter1 = shingles(tokens1, args.k)
    counter2 = shingles(tokens2, args.k)

    similarity = jaccard_similarity(counter1, counter2)
    print(f"Jaccard similarity (k={args.k}): {similarity:.4f}")


if __name__ == '__main__':
    main()