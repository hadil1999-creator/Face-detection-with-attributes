from Views import PictureRecognitionView


def run():
    try:
        menu = '''
        1.- Picture face recognition
        2.- Facial recognition with features
        
        Selection: '''
        x = int(input(menu))
    
    except Exception:
        print(f"\nError in the input")
    
    else:
        if x == 1:
            PictureRecognitionView.picture_face_recognition("OmarTobias_3.jpg")
        
        elif x == 2:
            PictureRecognitionView.facial_recognition_with_features("OmarTobias_3.jpg")
        
        else:
            print(f"\nSin accion")


if __name__ == "__main__":
    run()