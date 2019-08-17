import tkinter as tk
from functools import partial

# todo: get all cards from the folders automatic
# todo: build a listed list with the cards
# todo: resize button

class Window(tk.Frame):
    cards_background_images = list()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.init_images()
        self.init_window()

    def init_images(self):
        cards_dir = "../fig/cards/"
        button_background = ["../fig/card-1.gif", "../fig/card-2.gif", "../fig/card-3.gif", "../fig/card-4.gif"]
        for i in range(4):
            self.cards_background_images.append(tk.PhotoImage(file=button_background[i]))


    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=tk.BOTH, expand=1)
        self.init_card_pool()

    def init_card_pool(self):
        button = list()
        for i in range(4):
            button.append(tk.Button(self, image=self.cards_background_images[i],
                                    command=partial(self.click_card_pool, i)))
            button[-1].grid(row=0, column=i)

    def click_card_pool(self, button_index):
        print(button_index)


class PokerAssistGui:
    def __init__(self):
        root = tk.Tk()
        app = Window(root)
        root.mainloop()


if __name__ == '__main__':
    PokerAssistGui()