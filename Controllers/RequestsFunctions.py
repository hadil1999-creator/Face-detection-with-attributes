import requests


def post_Http(url, headers, params, body):
    response = None
    
    try:
        response = requests.request('POST', url, params = params, headers = headers, data = body)
                
    except Exception:
        print(f"\nError in the post function.")
        
    return response

def put_Http(url, headers, body):
    response = None
    
    try:
        response = requests.request('POST', url, headers = headers, data = body)
                
    except Exception:
        print(f"\nError in the put function.")
        
    return response