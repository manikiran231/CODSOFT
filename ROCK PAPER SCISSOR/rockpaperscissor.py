import tkinter as tk
import random

user_score = 0  
computer_score = 0  

def play_game(user_choice):
    global user_score, computer_score 
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    if result == "You win!":
        user_score += 1  
    elif result == "Computer wins!":
        computer_score += 1  
    update_scores()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def reset_game():
    global user_score, computer_score  
    user_score = 0
    computer_score = 0
    update_scores()
    result_label.config(text="")
    computer_choice_label.config(text="")

def update_scores():
    score_label.config(text=f"Your score: {user_score}\nComputer's score: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x320")  
instruction_label = tk.Label(root, text="Choose your move:")
instruction_label.pack()

rock_button = tk.Button(root, text="Rock", width=8, height=2, command=lambda: play_game('rock'))
rock_button.pack(anchor="center")

paper_button = tk.Button(root, text="Paper", width=8, height=2, command=lambda: play_game('paper'))
paper_button.pack(anchor="center")

scissors_button = tk.Button(root, text="Scissors", width=8, height=2, command=lambda: play_game('scissors'))
scissors_button.pack(anchor="center")

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(anchor="center")

computer_choice_label = tk.Label(root, text="", font=("Helvetica", 12))
computer_choice_label.pack(anchor="center")

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(anchor="center")

score_label = tk.Label(root, text="Your score: 0\nComputer's score: 0", font=("Helvetica", 12))
score_label.pack(anchor="center")

root.mainloop()
