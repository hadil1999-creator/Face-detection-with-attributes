from Resources import Config, FaceDetectConfig
from Controllers import FaceIdentifyController
from io import BytesIO
from PIL import Image
import uuid
import os



def get_path(file_name, file_path = "", image = False):
    if (file_path == "") and (not image):
        path = os.getcwd() + '\\' + file_name

    elif (file_path == "") and image:
        path = Config.DEFAULT_IMAGE_PATH + '\\' + file_name

    else:
        path = file_path + '\\' + file_name
    
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


def open_image(image, binary= False, image_path = ""):
    try:
        if binary:
            img = Image.open(BytesIO(image))
            
        else:
            path = get_path(image, image_path, True)
            img = Image.open(path)
        
    except IOError:
        print(f"\nError to open image")
        
    else:
        return img
    
    return None


def read_image_with_binary(image_name, image_path = ""):
    body = None
    
    path = get_path(image_name, image_path, image= True)
    
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


def read_image_with_binary_by_path(image_path):
    body = None
    
    path = image_path
    
    try:
        img = open(file = path, mode = 'rb')
        body = img.read()
        
    except IOError:
        print(f"\nError to open the image")

    else:
        print(f"\nImage opened successfully")
            
    finally:
        img.close()
        
        return body


def get_face_detection_url(endpoint):
    return endpoint + FaceDetectConfig.REQUEST_URL


def get_dictionary_text(dictionary, key, separator):
    list_values = []
    
    try:
        values = str(dictionary[key])
        list_values = values.split(separator)
    
    except Exception:
        print(f"\nError to get dictionary text")
    
    else:
        return list_values
    
    return None


def get_rectangle(face_posicion):
    top = face_posicion['top']
    left = face_posicion['left']
    right = left + face_posicion['width']
    bottom = top + face_posicion['height']
    
    return ((left, top), (right, bottom))


def get_keys(dictionary):
    list_values = []
    
    try:
        list_values = list(dictionary.keys())
        
        if len(list_values) == 0:
            raise ValueError(f"\nError try obtain dictionary keys")
    
    except ValueError as ve:
        print(ve)
    
    else:
        return list_values
    
    return None


def get_person_group_id():
    PERSON_GROUP_ID = str(uuid.uuid4())             # assign a random ID (or name it anything)
    
    # Used for the Delete Person Group example.
    TARGET_PERSON_GROUP_ID = str(uuid.uuid4())      # assign a random ID (or name it anything)
    return [PERSON_GROUP_ID, TARGET_PERSON_GROUP_ID]


def get_name(returnFaceId, face_id):
    name = ""
    
    try:
        if returnFaceId == 'true':
            name = FaceIdentifyController.identify_face()
            
            if name == None:
                raise ValueError(f"\nUnidentified face.")

        else:
            name = "Error, return face id is disabled"
        
    except ValueError as ve:
        print(ve)
        name = face_id[0:8] + "...\n"
        
    except Exception:
        print(f"\nError to try get_name.")
    
    else:
        name += ".\n"
    
    finally:
        return name


def get_age(age_data):
    age = str(int(age_data))
    
    if Config.DEFAULT_IDIOM == "español": age += " años."
    else: age += "years."
    
    age += "\n"
    
    return age


def get_gender(gender_data):
    gender = gender_data.lower()
    
    if Config.DEFAULT_IDIOM == "español":
        if gender == "male": gender = "Hombre"
        elif gender == "female": gender = "Mujer"
        else: gender = "Género desconocido"
        
    else:
        gender = gender_data
    
    gender += ".\n"
    
    return gender


def get_smile(data_smile):
    smile = ""
    
    if data_smile > 0.95:
        smile = "Smiling."
        
        if Config.DEFAULT_IDIOM == "español":
            smile = "Soniente."
        
        smile += "\n"
    
    return smile


def get_facialHair(data_facialHair):
    facial_hair = ""
    
    try:
        if data_facialHair['moustache'] > .85:            
            if Config.DEFAULT_IDIOM == "español": facial_hair += "FH: Bigote. "
            else: facial_hair += "FH: Mostache. "
        
        if data_facialHair['beard'] > .85:
            if Config.DEFAULT_IDIOM == "español": facial_hair += "Barba. "
            else: facial_hair += "Beard. "
        
        if data_facialHair['sideburns'] > .85:
            if Config.DEFAULT_IDIOM == "español": facial_hair += "Patillas."
            else: facial_hair += "Sideburns"
    
    except Exception:
        print(f"\nError to try get the attribute \"facial hair\"")
    
    finally:
        return facial_hair


def get_headPose(data_headPose):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_facialHair yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_glasses(data_glasses):
    glases = data_glasses.lower()
    
    if Config.DEFAULT_IDIOM == "español":
        if glases == "readingglasses": glases = "Lentes de lectura"
        elif glases == "sunglasses": glases = "Lentes de sol"
        elif glases == "swimminggoggles": glases = "Goggles"
        else: glases = "Sin lentes"
        
    else:
        glases = data_glasses
    
    glases += ".\n"
    
    return glases


def get_emotion(data_emotions):
    emotions = ""
    
    try:
        if data_emotions['anger'] > .90:            
            if Config.DEFAULT_IDIOM == "español": emotions += "Ira"
            else: emotions += "Anger"
        
        elif data_emotions['contempt'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Desprecio"
            else: emotions += "Contempt"
        
        elif data_emotions['disgust'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Asco"
            else: emotions += "Disgust"
        
        elif data_emotions['fear'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Miedo"
            else: emotions += "Fear"
            
        elif data_emotions['happiness'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Felicidad"
            else: emotions += "Happiness"
            
        elif data_emotions['sadness'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Tristeza"
            else: emotions += "Sadness"
            
        elif data_emotions['surprise'] > .90:
            if Config.DEFAULT_IDIOM == "español": emotions += "Sorpresa"
            else: emotions += "Surprise"
            
        else:
            if Config.DEFAULT_IDIOM == "español": emotions += "Neutral"
            else: emotions += "Neutral"
    
    except Exception:
        print(f"\nError to try get the attribute \"facial hair\"")

    else:
        emotions += ".\n"
    
    finally:
        return emotions


def get_hair(data_hair):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_hair yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_makeup(data_makeup):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_makeup yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_accessories(data_accessories):
    accesories = ""
    
    try:
        for accesory in data_accessories:
            if (accesory['type'] == "headWear") and (accesory['confidence'] > 0.90):
                if (Config.DEFAULT_IDIOM == "español"): accesories += "Gorra/Sombrero."
                else: accesories += "HeadWear."
                
            if (accesory['type'] == "glasses") and (accesory['confidence'] > 0.90):
                if (Config.DEFAULT_IDIOM == "español"): accesories += "Lentes."
                else: accesories += "Glasses."
                
            if (accesory['type'] == "mask") and (accesory['confidence'] > 0.90):
                if (Config.DEFAULT_IDIOM == "español"): accesories += "Mascara."
                else: accesories += "Mask."
    
    except Exception:
        accesories = ""
        print(f"\nError to try get accesories.")
    
    else:
        accesories += "\n"
    
    finally:
        return accesories


def get_blur(data_blur):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_blur yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_exposure(data_exposure):
    exposure = ""
    
    if (data_exposure['exposureLevel'] == 'GoodExposure') and (data_exposure['value'] > 0.70):
        if (Config.DEFAULT_IDIOM == "español"): exposure += "Exposición buena.\n"
        else: exposure += "GoodExposure.\n"
    
    if (data_exposure['exposureLevel'] == 'OverExposure') and (data_exposure['value'] > 0.70):
        if (Config.DEFAULT_IDIOM == "español"): exposure += "Sobreexposición.\n"
        else: exposure += "OverExposure.\n"
    
    if (data_exposure['exposureLevel'] == 'UnderExposure') and (data_exposure['value'] > 0.70):
        if (Config.DEFAULT_IDIOM == "español"): exposure += "Bajo exposición.\n"
        else: exposure += "UnderExposure.\n"
    
    return exposure


def get_noise(data_noise):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_noise yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_occlusion(data_occlusion):
    try:
        if True:
            raise NotImplementedError(f"\nNo implement get_noise yet")
    
    except NotImplementedError as nie:
        print(nie)
    
    return ""


def get_mask(data_mask):
    mask = ""
    
    try:
        mask = data_mask['type']
        
        if Config.DEFAULT_IDIOM == 'español':
            if mask == 'noMask': mask = 'Sin mascarilla'
            elif mask == 'faceMask': mask = 'Mascarilla'
            elif mask == 'otherMaskOrOcclusion': mask = 'Otro tipo de mascarilla.'
            else: mask = 'incierto'
            
        if str(data_mask['noseAndMouthCovered']).lower() == 'true':
            if Config.DEFAULT_IDIOM == 'español': mask += '.\nNariz y boca cubiertas'
            else: mask += ".\nNose and mouth covered"
        
    except Exception:
        print(f"\nError to try get the face mask data")
        
    else:
        mask += '.\n'
    
    finally:
        return mask


def get_qualityForRecognition(data_qualityForRecognition):
    qualityForRecognition = ""
    
    qualityForRecognition = data_qualityForRecognition
    
    if Config.DEFAULT_IDIOM == 'español':
        if qualityForRecognition == 'low': qualityForRecognition = 'Bajo'
        if qualityForRecognition == 'medium': qualityForRecognition = 'Medio'
        if qualityForRecognition == 'high': qualityForRecognition = 'Alto'
    
    qualityForRecognition += ".\n"
    
    return qualityForRecognition


def get_face_data(face_attributes):
    params_data = ""
    
    try:
        for attribute in face_attributes:
            if attribute == 'age':
                params_data += get_age(face_attributes[attribute])
                
            elif attribute == 'gender':
                params_data += get_gender(face_attributes[attribute])
                
            elif attribute == 'smile':
                params_data += get_smile(face_attributes[attribute])
            
            elif attribute == 'facialHair':
                params_data += get_facialHair(face_attributes[attribute])
            
            elif attribute == 'headPose':
                params_data += get_headPose(face_attributes[attribute])
            
            elif attribute == 'glasses':
                params_data += get_glasses(face_attributes[attribute])
            
            elif attribute == 'emotion':
                params_data += get_emotion(face_attributes[attribute])
            
            elif attribute == 'hair':
                params_data += get_hair(face_attributes[attribute])
            
            elif attribute == 'makeup':
                params_data += get_makeup(face_attributes[attribute])
            
            elif attribute == 'accessories':
                params_data += get_accessories(face_attributes[attribute])
            
            elif attribute == 'blur':
                params_data += get_blur(face_attributes[attribute])
            
            elif attribute == 'exposure':
                params_data += get_exposure(face_attributes[attribute])
            
            elif attribute == 'noise':
                params_data += get_noise(face_attributes[attribute])
            
            elif attribute == 'occlusion':
                params_data += get_occlusion(face_attributes[attribute])
            
            elif attribute == 'mask':
                params_data += get_mask(face_attributes[attribute])
            
            elif attribute == 'qualityForRecognition':
                params_data += get_qualityForRecognition(face_attributes[attribute])
            
            else:
                raise ValueError(f"\nAttribute not found")
            
    except ValueError as ve:
        print(ve)
    
    finally:
        return params_data