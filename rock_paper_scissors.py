# rock_paper_scissors.py
import random

def play_game():
    print("===== ROCK • PAPER • SCISSORS =====")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    user_score = 0
    computer_score = 0
    rounds = 0

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if user_choice == computer_choice:
            print("Result: It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("Result: You win! 🎉")
            user_score += 1
        else:
            print("Result: You lose. 😢")
            computer_score += 1

        rounds += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score} | Rounds: {rounds}\n")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score} | Total Rounds: {rounds}")
            print("Goodbye!")
            break
        print("----------------------------\n")

if __name__ == "__main__":
    play_game()