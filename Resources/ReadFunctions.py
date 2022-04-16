from Resources import Config, FaceDetectConfig
from io import BytesIO
from PIL import Image
import os



def get_path(file_name, path = ""):
    if path == "":
        path = os.getcwd() + '\\' + file_name
        
    else:
        path = path + '\\' + file_name
    
    return path


def read_text_document(file_name, path_file = ""):
    
    content = []
    
    path = get_path(file_name, path_file)
    
    try:
        with open(file= path, mode='r', encoding='utf-8') as f:
            content = f.readlines()
        f.close()
        
    except IOError:
        print(f"\nError to try  open the file {file_name}")
    
    else:
        print(f"\nFile {file_name} open successfully")
    
    finally:                    
        return content


def get_endpoint(en_ak):
    endpoint = ""
    
    try:
        endpoint = en_ak[0][:-1]
    
    except Exception:
        print(f"\nError in the reading of the endpoint")
        
    finally:
        return endpoint
        

def get_key(en_ak):
    key = ""
    
    try:
        key = en_ak[1]
    
    except Exception:
        print(f"\nError in the reading of the API Key")
        
    finally:
        return key
 
    
def get_connection_string():
    EN_AK = []
    
    EN_AK = read_text_document(file_name= Config.CONNECTION_FILE_NAME)
    
    try:
        if len(EN_AK) == 0:
            raise ValueError(f"\nERROR: The Api key and/or endpoint are missing")
    
    except ValueError as ve:
        print(ve)
    
    else:
        ENDPOINT = get_endpoint(EN_AK)
        KEY = get_key(EN_AK)
        
        return [ENDPOINT, KEY]
    
    return [None, None]


def get_header(KEY):
    return FaceDetectConfig.header(KEY)


def get_params():
    return FaceDetectConfig.param()


""" def open_image(image, binary= False, path = ""):
    img = None
    
    try:
        if binary:
            img = Image.open(BytesIO(image))
        else:
            img = Image.open(BytesIO(image))
            
    except IOError:
        print(f"\nError to open image")
 """

def read_image_with_binary(image_name, image_path = ""):
    body = None
    
    if image_path == "":
        path = get_path(image_name, Config.DEFAULT_IMAGE_PATH)
        
    else:
        path = get_path(image_name, image_path)
    
    try:
        img = open(file = path, mode = 'rb')
        body = img.read()
        
    except IOError:
        print(f"\nError to open the image {image_name}")

    else:
        print(f"\nImage {image_name} open successfully")
            
    finally:
        img.close()
        
        return body
    

def get_face_detection_url(endpoint):
    return endpoint + FaceDetectConfig.REQUEST_URL