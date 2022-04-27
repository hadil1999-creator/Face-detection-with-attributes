import tkinter
from tkinter import filedialog
from Views import PictureRecognitionView
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

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

root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def open_img():
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    return filename

def display_img():
    x = open_img()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def button_logic():
    PictureRecognitionView.facial_recognition_with_features_gui(open_img())
    img = Image.open('result.jpg')
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()


def run_gui():
    
    root.title('Picture Recognition')

    button = tkinter.Button(root, text='Select Picture', width=25, command=button_logic)
    button.pack()

    
    root.mainloop()


if __name__ == "__main__":
    run()