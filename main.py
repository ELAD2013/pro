import tkinter as tk
from tkinter import messagebox

class TycoonGame:
    def __init__(self, root):
        self.money = 100  # Starting money
        self.income = 10  # Income per turn
        self.upgrade_cost = 50  # Cost to upgrade income
        self.turn = 1

        # Set up the GUI
        self.root = root
        self.root.title("Tycoon Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")

        # Title
        self.title_label = tk.Label(root, text="Tycoon Game", font=("Arial", 20, "bold"), bg="#f0f8ff", fg="#4CAF50")
        self.title_label.pack(pady=10)

        # Status display
        self.status_frame = tk.Frame(root, bg="#f0f8ff")
        self.status_frame.pack(pady=10)

        self.turn_label = tk.Label(self.status_frame, text=f"Turn: {self.turn}", font=("Arial", 14), bg="#f0f8ff")
        self.turn_label.grid(row=0, column=0, padx=10)

        self.money_label = tk.Label(self.status_frame, text=f"Money: ${self.money}", font=("Arial", 14), bg="#f0f8ff")
        self.money_label.grid(row=1, column=0, padx=10)

        self.income_label = tk.Label(self.status_frame, text=f"Income per turn: ${self.income}", font=("Arial", 14), bg="#f0f8ff")
        self.income_label.grid(row=2, column=0, padx=10)

        self.upgrade_label = tk.Label(self.status_frame, text=f"Upgrade cost: ${self.upgrade_cost}", font=("Arial", 14), bg="#f0f8ff")
        self.upgrade_label.grid(row=3, column=0, padx=10)

        # Action buttons
        self.button_frame = tk.Frame(root, bg="#f0f8ff")
        self.button_frame.pack(pady=20)

        self.earn_button = tk.Button(self.button_frame, text="Earn Income", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.earn_income)
        self.earn_button.grid(row=0, column=0, padx=10)

        self.upgrade_button = tk.Button(self.button_frame, text="Upgrade Income", font=("Arial", 12), bg="#ff9800", fg="white", command=self.upgrade_income)
        self.upgrade_button.grid(row=0, column=1, padx=10)

        self.end_button = tk.Button(self.button_frame, text="End Game", font=("Arial", 12), bg="#f44336", fg="white", command=self.end_game)
        self.end_button.grid(row=0, column=2, padx=10)

    def update_status(self):
        self.turn_label.config(text=f"Turn: {self.turn}")
        self.money_label.config(text=f"Money: ${self.money}")
        self.income_label.config(text=f"Income per turn: ${self.income}")
        self.upgrade_label.config(text=f"Upgrade cost: ${self.upgrade_cost}")

    def earn_income(self):
        self.money += self.income
        self.turn += 1
        messagebox.showinfo("Income Earned", f"You earned ${self.income} this turn!")
        self.update_status()

    def upgrade_income(self):
        if self.money >= self.upgrade_cost:
            self.money -= self.upgrade_cost
            self.income += 10
            self.upgrade_cost += 20
            self.turn += 1
            messagebox.showinfo("Upgrade Successful", "You upgraded your income!")
        else:
            messagebox.showwarning("Upgrade Failed", "Not enough money to upgrade!")
        self.update_status()

    def end_game(self):
        messagebox.showinfo("Game Over", "Thanks for playing!")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = TycoonGame(root)
    root.mainloop()