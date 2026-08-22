import re


def word_error_rate(reference: str, hypothesis: str) -> float:
    reference_words = normalize(reference)
    hypothesis_words = normalize(hypothesis)
    if not reference_words:
        return 0.0 if not hypothesis_words else 1.0

    previous = list(range(len(hypothesis_words) + 1))
    for reference_index, reference_word in enumerate(reference_words, start=1):
        current = [reference_index]
        for hypothesis_index, hypothesis_word in enumerate(hypothesis_words, start=1):
            substitution = previous[hypothesis_index - 1] + (reference_word != hypothesis_word)
            deletion = previous[hypothesis_index] + 1
            insertion = current[hypothesis_index - 1] + 1
            current.append(min(substitution, deletion, insertion))
        previous = current
    return previous[-1] / len(reference_words)


def normalize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())
