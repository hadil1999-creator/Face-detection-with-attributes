REQUEST_URL = '/face/v1.0/detect'

def header(subscription_key):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    return headers

def param():
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,accessories,emotion',
        'recognitionModel': 'recognition_04',
        'returnRecognitionModel': 'false',
        'detectionModel': 'detection_01',
        'faceIdTimeToLive': '86400',
    }
    
    return params