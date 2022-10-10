from tkinter import *
from tkinter import ttk

### creating widgets.
# widgets must have a parent passed into the constructor.
'''
	widgets don't need to be assigned to variables, unless they need to be referenced later.
'''

root = Tk()
content = ttk.Frame(root)
ttk.Button(content)

### widget configuration.
# configuration can be done in multiple ways.
button = ttk.Button(content, text="Hello", command="buttonpressed")
button.grid()

# output the value of the text property.
print(button['text'])

# configure using indexing.
button['text'] = 'Goodbye'
print(button['text'])

# configure using an instance method.
button.configure(text='Wassup')
print(button.configure('text'))

# print all configuration values.
print(button.configure())


### widget introspection.
def print_hierarchy(w, depth=0):
    print('\t' * depth + '%s w=%d h=%d (%d,%x)' %
          (w.winfo_class(), w.winfo_width(), w.winfo_height(), w.winfo_x(),
           w.winfo_y()))
    for child in w.winfo_children():
        print_hierarchy(child, depth + 1)


print_hierarchy(root)
