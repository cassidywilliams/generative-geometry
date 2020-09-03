from generative_geometery.setup import Generate
from generative_geometery.plotting import plot
import generative_geometery.shapes as shapes
import os
import tkinter as tk
from datetime import datetime
from PIL import ImageTk,Image


class GenerativeUI:

    def __init__(self, root):
        self.master = root
        self.master.geometry("1000x1000")
        #self.master.resizable(False, False)
        self.master.title("Generative Geometry")
        self.name_input_label = tk.Label(root, text='Project Name')
        self.name_input_label.pack()
        self.project_name_input = tk.Text(root, height=2, width=10)
        self.project_name_input.pack()

        self.code_input_label = tk.Label(root, text='Code')
        self.code_input_label.pack()
        self.code_input = tk.Text(root, height=10, width=100)
        self.code_input.pack()

        # self.canvas = tk.Canvas(root, width=600, height=600)
        # self.canvas.pack()
        # self.img = ImageTk.PhotoImage(Image.open("abcd.png"))
        # self.canvas.create_image(300, 300, image=self.img)

        self.preview_button = tk.Button(root, height=1, width=15, text="Preview",
                                       command=lambda: self.popup("hola"))
        self.preview_button.pack()

        self.export_button = tk.Button(root, height=1, width=15, text="Export Package",
                                       command=lambda: self.export_package(self.retrieve_input(self.project_name_input),
                                                                          self.retrieve_input(self.project_name_input)))
        self.export_button.pack()

    def popup(self, msg):
        popup = tk.Tk()
        popup.wm_title("Results")
        # label = tk.Label(popup, text=msg, font=(None, 24))
        # label.pack(side="top", fill="x", pady=10, padx=10)

        canvas = tk.Canvas(popup, width=600, height=600)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open("abcd.png"), master=popup)
        canvas.create_image(300, 300, image=img)

        b1 = tk.Button(popup, text="Close", command=popup.destroy, width=10)
        b1.pack(padx=10, pady=10)
        popup.mainloop()

    def retrieve_input(self, text_box):
        """
        Returns text input into a text box
        """
        input_val = text_box.get("1.0", "end-1c")
        return input_val

    def run_code_input(self, code_to_run, filename, path):
        init = Generate(600, 600, 20, 15, 15)
        surface, ctx = init.setup_canvas()
        exec(code_to_run)

        # for i in range(0, 50):
        #     plot(ctx, shapes.spiro(5, 10, 4), .05, (i * .001, i * .01, i * .02))
        #     ctx.rotate(5)

        surface.write_to_png(path + '/' + filename + '.png')
        surface.write_to_png(path + '/' + filename + '.svg')

    def export_package(self, path, filename):

        #  this creates a directory, exports the code for the design and the image files and saves all to directory
        date = datetime.today().strftime('%Y-%m-%d')
        path = os.path.join(os.getcwd(), path + '_' + date)
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        code = self.retrieve_input(self.code_input)
        self.run_code_input(code, filename, path)

        with open(os.path.join(path, filename + '.py'), 'w') as f:
            f.write(code)


def main():
    root = tk.Tk()
    GenerativeUI(root)
    root.mainloop()
    #render()


if __name__ == '__main__':
    main()
