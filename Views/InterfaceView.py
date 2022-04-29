from Resources import InterfaceFunctions
from tkinter import *
from tkinter import ttk

paddings = {'padx': 5, 'pady': 5}

def _startup():
    '''Start the window and set initial parameters.
    '''

    root = Tk()
    root.geometry('900x600')
    root.resizable(width=True, height=True)
    root.title('Picture Recognition')

    return root

def _set_menu(master):
    '''Creates upper menu with Contact, About, and Exit buttons.
    '''

    menu = Menu(master)
    master.config(menu=menu)
    menu.add_command(label='Contact', command=InterfaceFunctions.contact_button)
    menu.add_command(label='About', command=InterfaceFunctions.about_button)
    menu.add_command(label='Exit', command=master.quit)

def _set_styles():
    '''Set fonts, paddings, and colors.
    '''

    style = ttk.Style()

    # Fonts.
    style.configure('TMenubutton', font=('Helvetica', 10))
    style.configure('TButton', font=('Helvetica', 10))
    style.configure('TLabel', font=('Helvetica', 10))

    # Backgrounds.
    style.configure('TFrame')
    style.configure('red.TFrame', background='red')

    

def _set_frames(master):
    '''Create frames.
    '''

    # Contains intro text, dropdown menu, and button.
    topframe = ttk.Frame(master)
    topframe.pack(side=TOP)

    # Contains panel label.
    bottomframe = ttk.Frame(master)
    bottomframe.pack(side= BOTTOM, fill=BOTH, expand=True)

    return topframe, bottomframe


def interface_view():
    '''Load the interface.
    '''

    root = _startup()

    topframe, bottomframe = _set_frames(root)

    _set_styles()

    _set_menu(root)    

    # Text.
    intro_text = 'Reconocimiento facial y deteccion de caracteristicas.'
    intro = ttk.Label(topframe, text = intro_text)
    intro.grid(column = 0, columnspan = 2, row = 0, **paddings)

    # Button, calls button logic. Uses lambda function to send function with arguments.
    button = ttk.Button(topframe, text='Analyze Picture', command=lambda: InterfaceFunctions.picture_button(label, chosen.get()))
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