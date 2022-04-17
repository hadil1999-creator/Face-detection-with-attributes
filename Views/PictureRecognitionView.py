from Controllers import FaceDetectController
from Resources import DrawingFunctions
from PIL import Image



def picture_face_recognition(image_name):
    data, image = FaceDetectController.face_identify(image_name)
    
    if (data != None) and (image != None):
        picture = DrawingFunctions.draw_rectangles_in_faces(data, image)
        
        if picture != None:
            picture.show()
            picture.save("result.jpg")
            picture.close()


def facial_recognition_with_features(image_name):
    data, image = FaceDetectController.face_identify(image_name)
    
    if (data != None) and (image != None):
        picture = DrawingFunctions.draw_features(data, image)
        
        if picture != None:
            picture.show()
            picture.save("result.jpg")
            picture.close()
        