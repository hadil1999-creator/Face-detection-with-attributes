REQUEST_URL = "/face/v1.0/persongroups/"

def header(subscription_key):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    
    return headers

def body(name_person, data):
    body = {
        'name': name_person,
        'userData': data,
        'recognitionModel': 'recognition_01',
    }
    
    return body