from generative_geometery.setup import Generate
from generative_geometery.plotting import plot
import generative_geometery.shapes as shapes
import os
import tkinter as tk


class GenerativeUI:
    def __init__(self, root):
        self.master = root
        self.master.geometry("750x380")
        self.master.resizable(False, False)
        self.master.title("Generative Geometry")
        self.name_input_label = tk.Label(root, text='Project Name')
        self.name_input_label.pack()
        self.project_name_input = tk.Text(root, height=2, width=10)
        self.project_name_input.pack()

        self.code_input_label = tk.Label(root, text='Code')
        self.code_input_label.pack()
        self.code_input = tk.Text(root, height=10, width=100)
        self.code_input.pack()

        self.buttonCommit = tk.Button(root, height=1, width=10, text="Export Package",
                                      command=lambda: self.export_package(self.retrieve_input(self.project_name_input),
                                                                          self.retrieve_input(self.project_name_input)))

        # command=lambda: retrieve_input() >>> just means do this when i press the button
        self.buttonCommit.pack()

    def retrieve_input(self, text_box):
        """
        Returns text input into a text box
        """
        input_val = text_box.get("1.0", "end-1c")
        return input_val

    def render(self, code_to_run, filename, path):
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

        path = os.path.join(os.getcwd(), path)
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

        code = self.retrieve_input(self.code_input)
        self.render(code, filename, path)

        with open(os.path.join(path, filename+ '.py'), 'w') as f:
            f.write(code)


def main():
    root = tk.Tk()
    GenerativeUI(root)
    root.mainloop()
    #render()


if __name__ == '__main__':
    main()
