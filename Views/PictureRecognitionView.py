from ast import And
from PIL import ImageDraw
from Controllers import FaceDetectController
from Views import DrawingFunctions


def picture_face_recognition(image_name):
    data, image = FaceDetectController.face_identify(image_name)
    
    if (data != None) and (image != None):
        DrawingFunctions.draw_image(data, image)