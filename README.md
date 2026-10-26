# Rule-Based Chatbot

A beginner-friendly command-line chatbot built with Python's standard library. RuleBot responds to greetings and questions by matching user messages against predefined rules. It does not learn or generate original answers.

## Features

- Recognizes greetings such as `hello`, `hi`, and `good morning`.
- Answers predefined questions about Python, AI, machine learning, and chatbots.
- Displays the current local date and time.
- Handles capitalization, punctuation, and extra spaces.
- Provides a fallback response for unsupported messages.
- Exits using `bye`, `exit`, or `quit`.
- Includes automated unit tests using Python's built-in `unittest`.

## Technologies

- Python 3
- `datetime`
- `re`
- `unittest`

No third-party packages or API keys are required.

## Project Structure

```text
01-rule-based-chatbot/
├── main.py
├── test_main.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Run the Chatbot

```powershell
python main.py
```

If needed, use the Windows Python launcher:

```powershell
py main.py
```

## Run Tests

```powershell
python -m unittest -v
```

## Example Conversation

```text
Welcome to RuleBot! Type 'bye', 'exit', or 'quit' to leave.

You: GOOD morning!!!
RuleBot: Good morning! I hope you have a great day.

You: What is Python?
RuleBot: Python is a readable, general-purpose programming language used for many kinds of software.

You: bye
RuleBot: Goodbye! Thanks for chatting with RuleBot.
```

## How It Works

1. Normalizes the user's input by converting it to lowercase and handling punctuation and whitespace.
2. Checks whether the normalized message matches a predefined rule.
3. Returns the associated response if a rule matches.
4. Returns a fallback message for unsupported inputs.

## Limitations

- Responses are predefined.
- The chatbot does not learn or retain conversational context.
- Unsupported phrasings may not match existing rules.
- Date and time depend on the computer's local clock.

## Future Improvements

- Add more response rules and phrase variations.
- Support simple conversation history.
- Store responses in a separate JSON file.
- Expand automated test coverage.

## Internship Attribution

**CodeOrbit Tech AI Internship** — Rule-Based Chatbot project.