import tkinter
from Views import PictureRecognitionView
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

def interface():
    # Start the window and set initial parameters.
    root = Tk()
    root.geometry('900x600')
    root.resizable(width=True, height=True)
    root.title('Picture Recognition')
    
    # Styles --------------------------------------------------------------------------------------------------------------------------
    style = ttk.Style()

    # Fonts.
    style.configure('TMenubutton', font=('Helvetica', 10))
    style.configure('TButton', font=('Helvetica', 10))
    style.configure('TLabel', font=('Helvetica', 10))

    # Backgrounds.
    style.configure('TFrame')
    style.configure('red.TFrame', background='red')

    paddings = {'padx': 5, 'pady': 5}

    # Functions --------------------------------------------------------------------------------------------------------------------------
    # About us.
    def about_button():
        tkinter.messagebox.showinfo("About",
        "Universidad Autonoma de Nuevo Leon\n"
        "Facultad de Ciencias Fisico Matematicas\n"
        "033 Sistemas Embebidos Avanzados\n\n"
        "Team #1\n"
        "Members:\n"
        "\n"
        "\n"
        "\n"
        "\n\n"
        "Powered by Microsoft Azure Face API"
        )

    # Contact
    def contact_button():
        tkinter.messagebox.showinfo("Contact",
        "You can contact the contributors via email.\n\n"
        "\n"
        "\n"
        "\n"
        "\n"
        )
    
    # Opens the file explorer and gets a file's path.
    def open_img():
        filename = filedialog.askopenfilename(title='open')
        print(filename)
        return filename

    # Displays the 'result.jpg' image of the root folder by updating the panel label declared below.
    def _display_img():
        # Get the image from the root folder.
        image = Image.open('result.jpg')
        image = ImageTk.PhotoImage(image)

        # Update the label.
        label.config(image = image)
        label.image = image

    def button_logic(option):
        if(option == 'Basic'): PictureRecognitionView.picture_face_recognition_gui(open_img())
        if(option == 'Features'): PictureRecognitionView.facial_recognition_with_features_gui(open_img())
        _display_img()

    # Frames --------------------------------------------------------------------------------------------------------------------------
    # Contains intro text, dropdown menu, and button.
    topframe = ttk.Frame(root)
    topframe.pack(side=TOP)

    # Contains panel label.
    bottomframe = ttk.Frame(root)
    bottomframe.pack(side= BOTTOM, fill=BOTH, expand=True)

    # Widgets --------------------------------------------------------------------------------------------------------------------------
    # Upper menu.
    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label='Contact', command=contact_button)
    menu.add_command(label='About', command=about_button)
    menu.add_command(label='Exit', command=root.quit)
    
    # Text.
    intro_text = 'Reconocimiento facial y deteccion de caracteristicas.'
    intro = ttk.Label(topframe, text = intro_text)
    intro.grid(column = 0, columnspan = 2, row = 0, **paddings)

    # Button, calls button logic. Uses lambda function to send function with arguments.
    button = ttk.Button(topframe, text='Analyze Picture', command=lambda: button_logic(chosen.get()))
    button.grid(column = 0, row = 1, sticky = "e", **paddings)

    # Dropdown menu.
    options = ['Basic', 'Features']
    chosen = StringVar()
    dropdown = ttk.OptionMenu(topframe, chosen, options[0], *options)
    dropdown.grid(column = 1, row = 1, sticky = "w", **paddings)

    # Image panel, declared in here to  be updated when we press the button instead of creating a widget everytime.
    label = Label(bottomframe)
    label.pack(side = BOTTOM, fill = "both", expand = True, **paddings)

    root.mainloop()