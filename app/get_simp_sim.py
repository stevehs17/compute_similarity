import json
from time import time
from similarity import compute_pair_similarity

def get_simp_sim():
    try:
        print('Starting get_simp_sim() execution...')
        a = 'I walk'
        b = 'I talk'
        start = time()
        sim = compute_pair_similarity(a, b)
        secs = time() - start
        print('compute_pair_similarity seconds:', secs)
        body = json.dumps({'similarity': sim, 'seconds': secs})
        out = {
            'statusCode': 200,
            'body': body
        }
        print('Execution completed successfully.')
        return out
    except Exception as e:
        print('Execution failed.')
        print(e)
        raise e