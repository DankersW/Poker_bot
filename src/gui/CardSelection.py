import tkinter as tk
from functools import partial


class CardSelection:
    NUMBER_OF_SUITS = 4
    NUMBER_OF_CARDS = 13
    NUMBER_OF_CARDS_ON_HAND = 2
    NUMBER_OF_CARDS_ON_TABLE = 5
    cards_background_images = list()
    empty_card = None

    button_card_pool = list()
    button_card_hand = list()
    button_card_table = list()

    hand_card_counter = 0
    table_card_counter = 0
    selected_card_destination = "table"
    card_destination_counter = 0

    main_gui = None

    def __init__(self, master_frame, main_view):
        frame = master_frame
        self.main_gui = main_view

        self.init_card_images()
        self.build_card_pool(frame)

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

    def build_card_pool(self, frame):
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
        # self.button_card_pool[button_suite_index][button_card_index].configure(state=tk.DISABLED)
        card_destination = self.get_selected_card_destination()
        if card_destination is not None:
            counter = self.card_destination_counter
            card_destination[counter].configure(
                image=self.cards_background_images[button_suite_index][button_card_index])
            self.increment_card_clicked_counter()
        self.main_gui.update_gui()

    def get_selected_card_destination(self):
        is_table = self.selected_card_destination == "table" and self.table_card_counter < self.NUMBER_OF_CARDS_ON_TABLE
        is_hand = self.selected_card_destination == "hand" and self.hand_card_counter < self.NUMBER_OF_CARDS_ON_HAND
        if is_table:
            self.card_destination_counter = self.table_card_counter
            return self.button_card_table
        elif is_hand:
            self.card_destination_counter = self.hand_card_counter
            return self.button_card_hand
        else:
            return None

    def increment_card_clicked_counter(self):
        if self.selected_card_destination == "table":
            self.table_card_counter += 1
        elif self.selected_card_destination == "hand":
            self.hand_card_counter += 1

    def init_table_cards_frame(self, frame):
        label = tk.Label(frame, text="Cards On Table: ")
        label.pack(side=tk.LEFT)
        for i in range(self.NUMBER_OF_CARDS_ON_TABLE):
            self.button_card_table.append(
                tk.Button(frame, image=self.empty_card, command=partial(self.click_table_pool)))
            self.button_card_table[-1].pack(side=tk.LEFT)
        clear_button = tk.Button(frame, text="Clear", command=partial(self.click_table_clear))
        clear_button.pack(side=tk.RIGHT)

    def click_table_pool(self):
        self.selected_card_destination = "table"

    def click_table_clear(self):
        self.table_card_counter = 0
        for i in range(self.NUMBER_OF_CARDS_ON_TABLE):
            self.button_card_table[i].configure(image=self.empty_card)
        self.main_gui.update_gui()

    def init_hand_cards_frame(self, frame):
        label = tk.Label(frame, text="Cards On Hand  ")
        label.pack(side=tk.LEFT)
        for i in range(self.NUMBER_OF_CARDS_ON_HAND):
            self.button_card_hand.append(tk.Button(frame, image=self.empty_card, command=partial(self.click_hand_pool)))
            self.button_card_hand[-1].pack(side=tk.LEFT)
        clear_button = tk.Button(frame, text="Clear", command=partial(self.click_hand_clear))
        clear_button.pack(side=tk.RIGHT)

    def click_hand_pool(self):
        self.selected_card_destination = "hand"

    def click_hand_clear(self):
        self.hand_card_counter = 0
        for i in range(self.NUMBER_OF_CARDS_ON_HAND):
            self.button_card_hand[i].configure(image=self.empty_card)
        self.main_gui.update_gui()

if __name__ == '__main__':
    app = CardSelection
