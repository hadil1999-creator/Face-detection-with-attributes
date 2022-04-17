from Resources import ReadFunctions, FaceDetectConfig
from PIL import ImageDraw



def draw_rectangle(data, img, in_attributes= False):
    draw = ImageDraw.Draw(img)
    
    if in_attributes:
        dictionary = FaceDetectConfig.param()
        
        attributes = ReadFunctions.get_dictionary_text(dictionary, 'returnFaceAttributes', ',')
        
        for face in data:
            dimensions = ReadFunctions.get_rectangle(face['faceRectangle'])
            
            draw.rectangle((dimensions[0][0], dimensions[1][1], dimensions[0][0]+80, dimensions[1][1]+60),
                           fill= "red")
            
            draw.multiline_text((dimensions[0][0]+2, dimensions[1][1]+2),
                                text= attributes,
                                fill= "white")
        
    else:
        for face in data:
            dimensions = ReadFunctions.get_rectangle(face['faceRectangle'])
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


def draw_features(data, image):
    img = draw_rectangles_in_faces(data, image)
    
    if img != None:
        img = draw_rectangle(data, img, True)
        
    return img