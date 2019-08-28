import tkinter as tk
from functools import partial


class Window(tk.Frame):
    NUMBER_OF_SUITS = 4
    NUMBER_OF_CARDS = 13
    cards_background_images = list()

    button_card_pool = list()
    button_card_hand = list()
    button_card_table = list()

    hand_card_counter = 0
    table_card_counter = 0

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.init_card_images()
        self.init_window()

    def init_card_images(self):
        cards_dir = "../fig/cards/"
        for i in range(self.NUMBER_OF_SUITS):
            image_buffer = list()
            for j in range(self.NUMBER_OF_CARDS):
                file_name = cards_dir + str(i) + "-" + str(j) + ".gif"
                image_buffer.append(tk.PhotoImage(file=file_name))
            self.cards_background_images.append(image_buffer)
        file_name = cards_dir + "empty-card.gif"
        self.empty_card = tk.PhotoImage(file=file_name)

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=tk.BOTH, expand=1)

        control_frame = tk.LabelFrame(self, text="control frame")
        control_frame.pack(fill="both", expand="yes", side=tk.LEFT)
        visualisation_frame = tk.LabelFrame(self, text="visualisation frame")
        visualisation_frame.pack(fill="both", expand="yes", side=tk.LEFT)

        self.init_control_frame(control_frame)
        self.init_visualisation_frame(visualisation_frame)

    def init_control_frame(self, frame):
        card_pool_frame = tk.Frame(frame)
        game_information_frame = tk.LabelFrame(frame, text="game information frame")
        recommended_actions_frame = tk.LabelFrame(frame, text="recommendated actions frame")

        card_pool_frame.pack(fill="both", expand="yes")
        game_information_frame.pack(fill="both", expand="yes")
        recommended_actions_frame.pack(fill="both", expand="yes")

        self.init_card_pool_frame(card_pool_frame)
        self.init_game_information_frame(game_information_frame)
        self.init_recommended_actions_frame(recommended_actions_frame)

    def init_visualisation_frame(self, frame):
        label = tk.Label(frame, text="Inside the visualisation")
        label.pack()

    def init_card_pool_frame(self, frame):
        available_cards_frame = tk.Frame(frame)
        table_cards_frame = tk.Frame(frame)
        hand_cards_frame = tk.Frame(frame)

        available_cards_frame.pack(fill="both", expand="yes")
        table_cards_frame.pack(fill="both", expand="yes")
        hand_cards_frame.pack(fill="both", expand="yes")

        self.init_available_cards_frame(available_cards_frame)
        self.init_table_cards_frame(table_cards_frame)
        self.init_hand_cards_frame(hand_cards_frame)

    def init_available_cards_frame(self, frame):
        for i in range(self.NUMBER_OF_SUITS):
            for j in range(self.NUMBER_OF_CARDS):
                self.button_card_pool.append(tk.Button(frame, image=self.cards_background_images[i][j],
                                        command=partial(self.click_card_pool, i, j)))
                self.button_card_pool[-1].grid(row=i, column=j)

    def click_card_pool(self, button_suite_index, button_card_index):
        print(button_suite_index, button_card_index)
        #self.button_card_pool[button_suite_index][button_card_index].configure(state=tk.DISABLED)
        
        card_destination = self.get_selected_card_destination()
        if card_destination is not None:
            card_destination[self.table_card_counter].configure(
                            image=self.cards_background_images[button_suite_index][button_card_index])
            self.table_card_counter += 1

    def get_selected_card_destination(self):
        if self.table_card_counter < 5:
            return self.button_card_table
        else:
            return None

    def init_table_cards_frame(self, frame):
        label = tk.Label(frame, text="Cards On Table: ")
        label.pack(side=tk.LEFT)
        for i in range(5):
            self.button_card_table.append(tk.Button(frame, image=self.empty_card))
            self.button_card_table[-1].pack(side=tk.LEFT)

    def init_hand_cards_frame(self, frame):
        label = tk.Label(frame, text="Cards On Hand  ")
        label.pack(side=tk.LEFT)
        for i in range(2):
            self.button_card_hand.append(tk.Button(frame, image=self.empty_card))
            self.button_card_hand[-1].pack(side=tk.LEFT)

    def init_game_information_frame(self, frame):
        pass

    def init_recommended_actions_frame(self, frame):
        pass

class PokerAssistGui:
    def __init__(self):
        root = tk.Tk()
        app = Window(root)
        root.mainloop()


if __name__ == '__main__':
    PokerAssistGui()