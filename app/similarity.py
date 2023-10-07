from numpy import inner
from typing import List
from validator import empty_not_in, in_range, not_empty, not_none
import tensorflow_hub as hub

MIN_SIMILARITY = 0.0
MAX_SIMILARITY = 1.0

_MODEL_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"
_MODEL = None

def compute_pair_similarity(a: str, b: str) -> float:
    not_empty(a)
    not_empty(b)
    results = compute_similarity([a, b])
    sim = results[0][1]
    in_range(sim, MIN_SIMILARITY, MAX_SIMILARITY)
    return sim

def compute_similarity(strings: List[str]) -> List[List[float]]:
    not_empty(strings)
    empty_not_in(strings)

    print(f'Computing similarity of: {strings}')
    model = _get_model()
    embeds = model(strings)
    product = inner(embeds, embeds)
    sims = product.tolist()
    length = len(strings)
    max_epsilon = 0.00001  # suppress floating point rounding errors that make sim exceed MAX_SIMILARITY
    for i in range(length):
        for j in range(length):
            if sims[i][j] < MIN_SIMILARITY:
                sims[i][j] = MIN_SIMILARITY
            if MAX_SIMILARITY < sims[i][j] < MAX_SIMILARITY+max_epsilon:
                sims[i][j] = MAX_SIMILARITY
            in_range(sims[i][j], MIN_SIMILARITY, MAX_SIMILARITY)
    print(f'Similarity results: {sims}')
    not_empty(sims)
    return sims

def _get_model():
    global _MODEL
    if _MODEL is None:
        print('Loading model...')
        not_none(_MODEL_URL)
        _MODEL = hub.load(_MODEL_URL)
        print('Model loaded.')
    else:
        print('Model is already loaded.')
    not_none(_MODEL)
    return _MODEL
