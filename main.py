"""A small command-line chatbot that responds to predefined rules."""

from datetime import datetime
import re


# These rules match the entire normalized message to avoid accidental matches
# inside unrelated words or longer questions.
RESPONSES = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi there! How can I help?",
    "hey": "Hey! What would you like to talk about?",
    "good morning": "Good morning! I hope you have a great day.",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! What can I do for you?",
    "how are you": "I'm doing well, thank you! How are you?",
    "how are you doing": "I'm doing well, thank you! How are you?",
    "what is your name": "I'm RuleBot, a simple rule-based chatbot.",
    "what s your name": "I'm RuleBot, a simple rule-based chatbot.",
    "who created you": "I was created as a beginner-friendly Python project "
    "for the CodeOrbit Tech AI Internship.",
    "what can you do": "I can respond to greetings and a small set of questions "
    "about Python, AI, machine learning, chatbots, and the date or time.",
    "tell me a joke": "Why did the computer go to the doctor? It had a virus!",
    "what is python": "Python is a readable, general-purpose programming "
    "language used for many kinds of software.",
    "what is ai": "Artificial intelligence (AI) is the field of creating "
    "computer systems that perform tasks associated with human intelligence.",
    "what is machine learning": "Machine learning is a way for computers to "
    "learn patterns from data, rather than being given every rule explicitly.",
    "what is a chatbot": "A chatbot is a computer program that communicates "
    "with people through text or speech.",
}

DATE_QUERIES = {
    "date",
    "what is the date",
    "what s the date",
    "what is today s date",
    "what date is it",
}

TIME_QUERIES = {
    "time",
    "what time is it",
    "what is the time",
    "what s the time",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}


def normalize_input(message: str) -> str:
    """Lowercase a message and replace punctuation with single spaces."""
    message = message.lower()
    message = re.sub(r"[^\w\s]", " ", message)
    return " ".join(message.split())


def generate_response(message: str) -> str:
    """Return a response for a known phrase, date/time query, or unknown input."""
    normalized_message = normalize_input(message)

    if not normalized_message:
        return "I didn't receive a message. Please type something, or type 'bye' to exit."

    if normalized_message in EXIT_COMMANDS:
        return "Goodbye! Thanks for chatting with RuleBot."

    if normalized_message in DATE_QUERIES:
        return f"Today's date is {datetime.now():%A, %B %d, %Y}."

    if normalized_message in TIME_QUERIES:
        return f"The current time is {datetime.now():%I:%M:%S %p}."

    if normalized_message in RESPONSES:
        return RESPONSES[normalized_message]

    return (
        "I'm not sure how to respond to that yet. Try asking about Python, AI, "
        "machine learning, chatbots, the date, or the time."
    )


def chat() -> None:
    """Run the conversation until the user enters an exit command."""
    print("Welcome to RuleBot! Type 'bye', 'exit', or 'quit' to leave.")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Goodbye! Thanks for chatting with RuleBot.")
            break

        response = generate_response(message)
        print(f"RuleBot: {response}")

        if normalize_input(message) in EXIT_COMMANDS:
            break


if __name__ == "__main__":
    chat()
