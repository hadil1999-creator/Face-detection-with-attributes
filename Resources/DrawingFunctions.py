from Resources import ReadFunctions
from PIL import ImageDraw



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


""" def write_text(dictionary):
    keys = list(dictionary.keys())
    
    text = ""
    for key in keys:
        text += (key + ":\n")
    
    return text """


def draw_features(data, image):
    img = draw_rectangles_in_faces(data, image)
    
    if img != None:
        draw = ImageDraw.Draw(img)
        
        for face in range(0, len(data)):
            dimensions = get_rectangle(data[face]['faceRectangle'])
            draw.rectangle((dimensions[0][0], dimensions[1][1], dimensions[0][0]+80, dimensions[1][1]+50),
                           fill= "red")
            draw.multiline_text((dimensions[0][0]+2, dimensions[1][1]+2),
                                "Hola gente\nPlop\nPlop",
                                fill= "white")
        
        return img