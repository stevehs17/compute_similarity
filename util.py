from string import punctuation
from sys import _getframe
from typing import List
from validator import not_empty

def has_only_word(word: str, words: List[str]) -> bool:
    not_empty(word)
    not_empty(words)
    return all(w == word for w in words)

def log() -> str:
    func_name = _getframe(1).f_code.co_name
    s = f'Running {func_name}....'
    print(s)
    return s

def strip_final_punctuation(s: str) -> str:
    not_empty(s)
    s = s.rstrip(punctuation)
    not_empty(s)
    return s