from PIL import ImageDraw, Image
from io import BytesIO

def get_rectangle(face_posicion):
    top = face_posicion['top']
    left = face_posicion['left']
    right = left + face_posicion['width']
    bottom = top + face_posicion['height']
    
    return ((left, top), (right, bottom))


def draw_image(data, image):
    
    try:
        img = Image.open(BytesIO(image))

    except IOError:
        print(f"\nError to generate the image with the face recognition result")
        
    else:
        draw = ImageDraw.Draw(img)
        
        for face in range(0, len(data)):
            dimensions = get_rectangle(data[face]['faceRectangle'])
            draw.rectangle(dimensions, outline= 'red', width= 3)
            
        img.show()