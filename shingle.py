"""Module for extracting and counting k-shingles from text tokens."""

import argparse
from collections import Counter


def shingles(t, k):
    """Extracts all k-shingles from a list of tokens and returns their counts.

    Args:
        t (list of str): List of word tokens.
        k (int): Size of each shingle (number of consecutive tokens).

    Returns:
        Counter: A multiset mapping each k-shingle (as a tuple of tokens)
            to its frequency count.

    Raises:
        TypeError: If t is not a list or k is not an integer.
        ValueError: If k is less than 1 or if elements in t are not strings.
    """
    if not isinstance(t, list):
        raise TypeError("Tokens must be provided as a list")
    if not all(isinstance(token, str) for token in t):
        raise ValueError("All tokens in the list must be strings")
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k < 1:
        raise ValueError("k must be at least 1")

    shingle_list = [tuple(t[i:i + k]) for i in range(len(t) - k + 1)]
    return Counter(shingle_list)


def main():
    """Parses command-line arguments and prints the n most common k-shingles from input text."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", type=int, default=2)
    parser.add_argument("-n", type=int, default=10)

    args = parser.parse_args()

    tokens = []

    while True:
        try:
            line = input()
            tokens.extend(line.split())
        except EOFError:
            break

    shingle_counts = shingles(tokens, args.k)

    for shingle, count in shingle_counts.most_common(args.n):
        shingle_str = " ".join(shingle)
        print(f"{shingle_str}: {count}")


if __name__ == '__main__':
    main()