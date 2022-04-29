from Views import PictureRecognitionView
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

def _open_img():
    '''Opens the file explorer and gets a file's path.
    '''
    
    filename = filedialog.askopenfilename(title='open')
    print(filename)
    return filename

def _resize_image(label: Label, image: Image):
    '''Resize image to label size while maintaining aspect ratio.
    '''
    
    # Image height and width.
    img_width, img_height = image.size

    # Label height.
    label.update()
    label_height = label.winfo_height()
    
    # Normalize the width relative to the change in height.
    relative_width = int(img_width * (label_height/img_height))

    # Adjust the size.
    image = image.resize((relative_width, label_height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    return image

def _display_img_result(label: Label):
    '''Displays the 'result.jpg' image of the root folder by updating the label given.

    :param label: Label that will be updated.
    :type label: Label
    '''

    # Get the image from the root folder.
    image = Image.open('result.jpg')
    image = _resize_image(label, image)

    # Update the label.
    label.config(image = image)
    label.image = image

def picture_button(label: Label, option: str):
    '''Sends API request with selected picture and displays the result.

    :param option: Selected option, can be Basic or Features.
    :type option: str

    :param label: Label that will be updated.
    :type label: Label
    '''

    if(option == 'Basic'): PictureRecognitionView.picture_face_recognition_gui(_open_img())
    if(option == 'Features'): PictureRecognitionView.facial_recognition_with_features_gui(_open_img())
    _display_img_result(label)

def about_button():
    '''Displays about information on messagebox.
    '''

    messagebox.showinfo("About",
    "Universidad Autonoma de Nuevo Leon\n"
    "Facultad de Ciencias Fisico Matematicas\n"
    "033 Sistemas Embebidos Avanzados\n\n"
    "Equipo 1\n"
    "Miembros:\n"
    "Andrik De La Cruz Martínez\n"
    "Edson Yael García Silva\n"
    "Emilio Landin Solis\n"
    "Omar Silvestre Barron Tobias\n\n"
    "Powered by Microsoft Azure Face API"
    )

def contact_button():
    '''Displays contact information on messagebox.
    '''

    messagebox.showinfo("Contact",
    "You can contact the contributors via email.\n\n"
    "emilio.landin@gmail.com\n"
    )