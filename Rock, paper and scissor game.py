import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("400x300")  # Set window size
        master.configure(bg="#f0f8ff")  # Light blue background

        self.choices = ["rock", "paper", "scissors"]

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # User choice label
        self.user_choice_label = tk.Label(
            self.master,
            text="Choose rock, paper, or scissors:",
            font=("Helvetica", 14, "bold"),
            bg="#f0f8ff"
        )
        self.user_choice_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Buttons with color
        self.rock_btn = tk.Button(self.master, text="Rock", command=lambda: self.get_user_choice("rock"),
                                  font=("Helvetica", 12), bg="#FFB6C1", width=10)
        self.rock_btn.grid(row=1, column=0, padx=10, pady=10)

        self.paper_btn = tk.Button(self.master, text="Paper", command=lambda: self.get_user_choice("paper"),
                                   font=("Helvetica", 12), bg="#98FB98", width=10)
        self.paper_btn.grid(row=1, column=1, padx=10, pady=10)

        self.scissors_btn = tk.Button(self.master, text="Scissors", command=lambda: self.get_user_choice("scissors"),
                                      font=("Helvetica", 12), bg="#87CEFA", width=10)
        self.scissors_btn.grid(row=1, column=2, padx=10, pady=10)

        # Result label
        self.result_label = tk.Label(self.master, textvariable=self.result_var,
                                     font=("Helvetica", 12, "italic"), bg="#f0f8ff", fg="blue")
        self.result_label.grid(row=2, column=0, columnspan=3, pady=20)

        # Play again button
        self.play_again_btn = tk.Button(self.master, text="Play Again", command=self.play_again,
                                        font=("Helvetica", 12), bg="#FFD700")
        self.play_again_btn.grid(row=3, column=1, pady=10)

    def get_user_choice(self, choice):
        self.user_choice_var.set(choice)
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(choice, computer_choice)
        self.result_var.set(result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return f"It's a tie! You both chose {user_choice}."
        if (user_choice == "rock" and computer_choice == "scissors") or \
           (user_choice == "paper" and computer_choice == "rock") or \
           (user_choice == "scissors" and computer_choice == "paper"):
            return f"You win! {user_choice.capitalize()} beats {computer_choice}."
        else:
            return f"You lose! {computer_choice.capitalize()} beats {user_choice}."

    def play_again(self):
        self.result_var.set("")
        self.user_choice_var.set("")

root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()
