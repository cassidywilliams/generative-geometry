from generative_geometery.setup import Generate
from generative_geometery.plotting import plot
import generative_geometery.shapes as shapes
import os
import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
import shutil


class GenerativeUI:

    def __init__(self, root):

        self.project_name = 0

        self.master = root
        self.master.geometry("650x280")
        #self.master.resizable(False, False)
        self.master.title("Generative Geometry")
        # self.name_input_label = tk.Label(root, text='Project Name')
        # self.name_input_label.pack()
        # self.project_name_input = tk.Text(root, height=1, width=20)
        # self.project_name_input.pack()

        self.code_input_label = tk.Label(root, text='Input generative code below')
        self.code_input_label.pack(pady=10)
        self.code_input = tk.Text(root, height=10, width=100)
        self.code_input.pack(padx=10)

        # self.canvas = tk.Canvas(root, width=600, height=600)
        # self.canvas.pack()
        # self.img = ImageTk.PhotoImage(Image.open("abcd.png"))
        # self.canvas.create_image(300, 300, image=self.img)

        self.run_code_button = tk.Button(root, height=1, width=15, text="Generate",
                                         command=lambda: self.generate_button())
        self.run_code_button.pack(pady=10)

        # self.export_button = tk.Button(root, height=1, width=15, text="Export Package",
        #                                command=lambda: self.export_package(self.retrieve_input(self.project_name_input),
        #                                                                   self.retrieve_input(self.project_name_input)))
        # self.export_button.pack()

    def generate_button(self):
        if len(self.retrieve_input(self.code_input)) == 0:
            popup = tk.Tk()
            popup.wm_title("Error")
            canvas = tk.Canvas(popup, height=20)
            canvas.pack()
            label = tk.Label(popup, text="You must enter code.")
            label.pack(side="top", fill="x", pady=10, padx=10)
            b1 = tk.Button(popup, text="Ok", command=popup.destroy, width=10)
            b1.pack(padx=10, pady=10)
            popup.mainloop()

        else:
            self.project_name += 1
            popup = tk.Tk()
            popup.wm_title("Results")
            canvas = tk.Canvas(popup, width=600, height=600)
            canvas.pack()

            # this should export the package automatically
            date = datetime.today().strftime('%Y-%m-%d')
            path = os.path.join(os.getcwd(), date + '_' + str(self.project_name))
            self.export_package(path, str(self.project_name))

            # open the png from the exported package
            img = ImageTk.PhotoImage(Image.open(os.path.join(path, str(self.project_name) + ".png")), master=popup)
            canvas.create_image(300, 300, image=img)

            # if keep is selected, simply close popup
            keep = tk.Button(popup, text="Keep image and save project",
                             command=popup.destroy)
            keep.pack(side=tk.LEFT, padx=25, pady=10)

            # if kill is selected, delete package and destroy popup
            kill = tk.Button(popup, text="Discard and return", command=lambda: self.delete_package(path, popup))
            kill.pack(side=tk.RIGHT, padx=25, pady=10)

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

    def delete_package(self, path, popup):
        shutil.rmtree(path)
        popup.destroy()


def main():
    root = tk.Tk()
    GenerativeUI(root)
    root.mainloop()
    #render()


if __name__ == '__main__':
    main()
