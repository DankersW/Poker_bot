import tkinter as tk
from functools import partial

class Window(tk.Frame):
    NUMBER_OF_SUITS = 4
    NUMBER_OF_CARDS = 13
    cards_background_images = list()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.init_images()
        self.init_window()

    def init_images(self):
        cards_dir = "../fig/cards/"
        for i in range(self.NUMBER_OF_SUITS):
            image_buffer = list()
            for j in range(self.NUMBER_OF_CARDS):
                file_name = cards_dir + str(i) + "-" + str(j) + ".gif"
                file_name = "../fig/test.gif"
                image_buffer.append(tk.PhotoImage(file=file_name))
            self.cards_background_images.append(image_buffer)


    """
    old_height = 120
    old_width = 90
    scale_w = new_width/old_width
scale_h = new_height/old_height
photoImg.zoom(scale_w, scale_h)
    """


    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=tk.BOTH, expand=1)
        self.init_card_pool()

    def init_card_pool(self):
        button = list()
        for i in range(self.NUMBER_OF_SUITS):
            for j in range(self.NUMBER_OF_CARDS):
                button.append(tk.Button(self, image=self.cards_background_images[i][j],
                                        command=partial(self.click_card_pool, i, j)))
                button[-1].grid(row=i, column=j)

    def click_card_pool(self, button_suite_index, button_card_index):
        print(button_suite_index, button_card_index)


class PokerAssistGui:
    def __init__(self):
        root = tk.Tk()
        app = Window(root)
        root.mainloop()


if __name__ == '__main__':
    PokerAssistGui()