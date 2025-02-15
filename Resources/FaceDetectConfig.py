REQUEST_URL = '/face/v1.0/detect'

import requests
import json
from collections import defaultdict

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


# Example: Store the data
log = defaultdict(list)

# Sample code for sending the request to the Azure Face API
def detect_faces(subscription_key, image_path):
    url = "https://<your_region>.api.cognitive.microsoft.com" + REQUEST_URL
    headers = header(subscription_key)
    params = param()
    
    # Open image file
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Send request
    response = requests.post(url, headers=headers, params=params, data=image_data)

    if response.status_code == 200:
        face_data = response.json()

        # Log the detected attributes to monitor for drift and fairness
        for face in face_data:
            attributes = face.get('faceAttributes', {})
            age = attributes.get('age', None)
            gender = attributes.get('gender', None)
            emotion = attributes.get('emotion', {})

            log['age'].append(age)
            log['gender'].append(gender)
            log['emotion'].append(emotion)
        
        return face_data
    else:
        return f"Error: {response.status_code}, {response.text}"

def evaluate_fairness():
    gender_counts = {'male': 0, 'female': 0}
    emotion_counts = defaultdict(int)

    # Count occurrences of gender and emotions in the logged data
    for gender in log['gender']:
        if gender:
            gender_counts[gender] += 1

    for emotion in log['emotion']:
        if emotion:
            max_emotion = max(emotion, key=emotion.get)
            emotion_counts[max_emotion] += 1

    print("Gender Distribution:", gender_counts)
    print("Emotion Distribution:", emotion_counts)

def detect_data_drift():
    # Example: monitor age distribution over time
    age_values = log['age']
    if age_values:
        average_age = sum(age_values) / len(age_values)
        print(f"Average Age: {average_age}")

"""""
# Example usage

detect_faces(subscription_key, image_path)
evaluate_fairness()
detect_data_drift()
"""