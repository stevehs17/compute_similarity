import json
from similarity import compute_pair_similarity

def lambda_handler(event, context):
    return get_simp_sim()

def get_simp_sim():
    try:
        print('Starting get_simp_sim() execution...')
        a = 'I walk'
        b = 'I talk'
        sim = compute_pair_similarity(a, b)
        body = json.dumps({'similarity': sim})
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