from Controllers import RequestsFunctions
from Resources import ReadFunctions
import json


def face_identify(image_name):
    ENDPOINT, KEY = ReadFunctions.get_connection_string()
    
    headers = ReadFunctions.get_header(KEY)
    
    params = ReadFunctions.get_params()
    
    body = ReadFunctions.read_image_with_binary(image_name= image_name)
    
    url = ReadFunctions.get_face_detection_url(ENDPOINT)
    
    try:
        response = RequestsFunctions.post_Http(url, headers, params, body)
        parse = json.loads(response.text)

    except Exception:
        print(f"\nError to face identify")

    else:
        try:
            if len(parse) == 0:
                raise ValueError(f"\nNo faces identify in the image")
        
        except ValueError as ve:
            print(ve)

        else:    
            print(f"\nFace identify successfully")
            return [parse, body]
        
    return [None, None]

def face_identify_by_path(image_path):
    ENDPOINT, KEY = ReadFunctions.get_connection_string()
    
    headers = ReadFunctions.get_header(KEY)
    
    params = ReadFunctions.get_params()
    
    body = ReadFunctions.read_image_with_binary_by_path(image_path)
    
    url = ReadFunctions.get_face_detection_url(ENDPOINT)
    
    try:
        response = RequestsFunctions.post_Http(url, headers, params, body)
        parse = json.loads(response.text)

    except Exception:
        print(f"\nError to face identify")

    else:
        try:
            if len(parse) == 0:
                raise ValueError(f"\nNo faces identify in the image")
        
        except ValueError as ve:
            print(ve)

        else:    
            print(f"\nFace identify successfully")
            return [parse, body]
        
    return [None, None]