import generative_geometery.setup
#import generative_geometery.plotting
#import generative_geometery.shapes
import tkinter as tk


root = tk.Tk()


def retrieve_input():
    inputValue = textBox.get("1.0","end-1c")
    print(inputValue)


def plot():
    # this runs the code and renders the plot on UI
    pass


def export_package():
    # this creates a directory, exports the code for the design and the image files and saves all to directory
    pass


textBox = tk.Text(root, height=2, width=10)
textBox.pack()
buttonCommit = tk.Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())

#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

tk.mainloop()