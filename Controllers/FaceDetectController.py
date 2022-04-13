from Resources import ReadFunctions
import json
import requests


def post_Http(url, headers, params, body):
    response = None
    
    try:
        response = requests.request('POST', url, params = params, headers = headers, data = body)
                
    except Exception:
        print(f"\nError in the post function.")
        
    return response


def face_identify(image_name):
    ENDPOINT, KEY = ReadFunctions.get_connection_string()
    
    headers = ReadFunctions.get_header(KEY)
    
    params = ReadFunctions.get_params()
    
    body = ReadFunctions.read_image_with_binary(image_name= image_name)
    
    url = ReadFunctions.get_face_detection_url(ENDPOINT)
    
    try:
        response = post_Http(url, headers, params, body)
        parse = json.loads(response.text)

    except Exception:
        print(f"\nError to face identify")

    else:
        print(f"\nFace identify successfully")
        return [parse, body]
    
    return [None, None]