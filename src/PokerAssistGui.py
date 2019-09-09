from src.gui.CardSelection import CardSelection

import tkinter as tk


class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

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
        CardSelection(frame, self)

    def init_game_information_frame(self, frame):
        pass

    def init_recommended_actions_frame(self, frame):
        pass

    def update_gui(self):
        print("it works ... updating")


class PokerAssistGui:
    def __init__(self):
        root = tk.Tk()
        app = Window(root)
        root.mainloop()


if __name__ == '__main__':
    PokerAssistGui()
