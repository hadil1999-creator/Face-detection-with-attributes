from Views import PictureRecognitionView
from Interface import Interface

def run():
    try:
        menu = '''
        1.- Reconocimiento de rostros en imagen
        2.- Reconocimiento facial con atributos
        
        Selección: '''
        x = int(input(menu))
    
    except Exception:
        print(f"\nError in the input")
    
    else:
        if x == 1:
            PictureRecognitionView.picture_face_recognition("OmarTobias_3.jpg")
        
        elif x == 2:
            PictureRecognitionView.facial_recognition_with_features("OmarTobias_3.jpg")
        
        else:
            print(f"\nSin acción")

if __name__ == "__main__":
    Interface.interface()