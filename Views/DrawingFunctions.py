from ast import Raise
from Resources import ReadFunctions
from PIL import ImageDraw, ImageFont, Image



def get_rectangle(face_posicion):
    top = face_posicion['top']
    left = face_posicion['left']
    right = left + face_posicion['width']
    bottom = top + face_posicion['height']
    
    return ((left, top), (right, bottom))


def draw_rectangle(data, img):
    draw = ImageDraw.Draw(img)
    
    for face in range(0, len(data)):
        dimensions = get_rectangle(data[face]['faceRectangle'])
        draw.rectangle(dimensions, outline= 'red', width= 2)
    
    return img


def draw_rectangles_in_faces(data, image):
    try:
        img = ReadFunctions.open_image(image, True)
        
        if img == None:
            raise ValueError(f"\nError to draw rectangles in faces")

    except ValueError as ve:
        print(ve)
        
    else:
        img = draw_rectangle(data, img)
        
        return img
    
    return None

""" 
def draw_text(draw, img):
    pass


def draw_features(data, image):
    img = draw_rectangle(data, image)
    
    if img != None:
        draw = ImageDraw.Draw(img)
        
        draw.rectangle(((10, 10), (100, 60)), fill= "red")
        
        draw.multiline_text((15,15), "Hola gente", fill= "white")
        
        return img """