import generative_geometery.setup
#import generative_geometery.plotting
#import generative_geometery.shapes
import os
import tkinter as tk


root = tk.Tk()


def retrieve_input(text_box):
    input_val = text_box.get("1.0", "end-1c")
    print(input_val)
    return input_val


def plot():
    # this runs the code and renders the plot on UI
    pass


def export_package(path, filename):

    #  this creates a directory, exports the code for the design and the image files and saves all to directory

    path = os.path.join(os.getcwd(), path)
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)

    code = retrieve_input(code_input)

    with open(os.path.join(path, filename), 'w') as f:
        f.write(code)



code_input = tk.Text(root, height=2, width=10)
code_input.pack()

project_name_input = tk.Text(root, height=2, width=10)
project_name_input.pack()

buttonCommit = tk.Button(root, height=1, width=10, text="Commit",
                    command=lambda: export_package('test', 'elephants.py')) # this needs to pull project name from another text box

#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

tk.mainloop()