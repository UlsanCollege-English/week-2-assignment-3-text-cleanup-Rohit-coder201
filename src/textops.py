from typing import List


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for w in words:
        if w not in seen:
            seen.add(w)
            result.append(w)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be > 0")

    # Count frequencies
    freq = {}
    first_index = {}
    for i, w in enumerate(words):
        freq[w] = freq.get(w, 0) + 1
        if w not in first_index:
            first_index[w] = i

    # Sort by (-count, first appearance)
    sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], first_index[w]))

    return sorted_words[:k]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    banned_set = set(banned)
    return ["***" if w in banned_set else w for w in words]


# -------------------------
# Tests (can be run directly)
# -------------------------
if __name__ == "__main__":
    # unique_words_preserve_order
    print(unique_words_preserve_order(["a", "b", "a", "c", "b"]))  # ["a", "b", "c"]
    print(unique_words_preserve_order([]))  # []

    # top_k_frequent_first_tie
    words = ["x", "y", "x", "z", "y", "y", "x"]
    print(top_k_frequent_first_tie(words, 2))  # ["x", "y"]

    # redact_words
    words = ["alice", "bob", "alice", "carol"]
    print(redact_words(words, ["alice"]))  # ["***", "bob", "***", "carol"]
    print(redact_words(words, []))  # ["alice", "bob", "alice", "carol"]
