from textblob import TextBlob
import colorama
from colorama import Fore, Style
import sys, time

# Initialize colorama
colorama.init(autoreset=True)

# Global variables
username = ""
conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_processing_anim():
    """Show a processing animation."""
    print(f"{Fore.CYAN} Detecting sentiment clues", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print()

def analyze_sentiment(text):
    """Analyze the sentiment of a given text and update the counts."""
    global positive_count, negative_count, neutral_count
    try:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        conversation_history.append(text)

        if sentiment > 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN} Very positive sentiment detected, Agent {username} Score: {sentiment:.2f}"
        elif 0.25 <= sentiment <= 0.75:
            positive_count += 1
            return f"\n{Fore.GREEN} Positive sentiment detected, Agent {username} Score: {sentiment:.2f}"
        elif -0.25 <= sentiment <= 0.25:
            neutral_count += 1
            return f"\n{Fore.YELLOW} Neutral sentiment detected, Agent {username} Score: {sentiment:.2f}"
        elif -0.75 <= sentiment < -0.25:
            negative_count += 1
            return f"\n{Fore.RED} Negative sentiment detected, Agent {username} Score: {sentiment:.2f}"
        else:
            negative_count += 1
            return f"\n{Fore.RED} Very negative sentiment detected, Agent {username} Score: {sentiment:.2f}"
    except Exception as e:
        return f"{Fore.RED} An error occurred during analysis: {str(e)}"

def execute_command(command):
    """Execute specific commands like summary, reset, or history."""
    global conversation_history, positive_count, negative_count, neutral_count

    if command == "summary":
        return (f"{Fore.CYAN} Mission Report:\n"
                f"{Fore.GREEN} Positive messages detected: {positive_count}\n"
                f"{Fore.RED} Negative messages detected: {negative_count}\n"
                f"{Fore.YELLOW} Neutral messages detected: {neutral_count}\n")
    elif command == "reset":
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0
        return f"{Fore.CYAN} Mission Reset Complete\n"
    elif command == "history":
        return "\n".join([f"{Fore.CYAN} Mission {i + 1}: {msg}" for i, msg in enumerate(conversation_history)]) \
            if conversation_history else f"{Fore.YELLOW} No conversation history yet.\n"
    else:
        return f"{Fore.RED} Unknown command: {command}\n"

# Main program
def main():
    global username
    print(f"{Fore.MAGENTA}Welcome to the Sentiment Analysis Program!")
    username = input(f"{Fore.CYAN}Enter your Agent Name: {Fore.RESET}").strip()
    print(f"{Fore.GREEN}Hello, Agent {username}! Let's analyze some sentiments.")

    while True:
        user_input = input(f"\n{Fore.CYAN}Enter text or a command (summary, reset, history, exit): {Fore.RESET}").strip()
        if user_input.lower() == "exit":
            print(f"{Fore.MAGENTA}Goodbye, Agent {username}. Mission Terminated.\n")
            break
        elif user_input.lower() in ["summary", "reset", "history"]:
            print(execute_command(user_input.lower()))
        else:
            show_processing_anim()
            print(analyze_sentiment(user_input))

if __name__ == "__main__":
    main()
