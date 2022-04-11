from Controllers import FaceDetectController

def picture_face_recognition(image_name):
    data = FaceDetectController.face_identify(image_name)
    
    print(f"{data}")