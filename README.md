# Rule-Based Chatbot

A beginner-friendly command-line chatbot built with Python's standard library. RuleBot responds to a fixed set of greetings and questions by matching the user's normalized message against predefined rules. It does not learn, browse the web, or generate original answers.

## Objective

Build and understand a small Python program that accepts messages, applies conditional rule matching, and returns a suitable response. This project was prepared for the **CodeOrbit Tech AI Internship**.

## Features

- Recognizes `hello`, `hi`, `hey`, and time-of-day greetings.
- Answers basic conversation questions, including its name, creator, capabilities, and a joke.
- Gives short explanations of Python, AI, machine learning, and chatbots.
- Displays the computer's current local date and time.
- Ignores case differences, extra spaces, and basic punctuation while matching.
- Provides a helpful response for empty and unrecognized messages.
- Keeps chatting until `bye`, `exit`, or `quit` is entered.
- Exits cleanly on end-of-input or Ctrl+C.
- Includes automated tests using Python's built-in `unittest`.

## Technologies Used

- Python 3
- Python standard-library modules: `datetime`, `re`, and `unittest`

No third-party packages, API keys, databases, or network services are used.

## Project Folder Structure

```text
01-rule-based-chatbot/
├── main.py
├── test_main.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Prerequisites

- Python 3 installed on Windows.
- PowerShell or another terminal.

Check that Python is available:

```powershell
python --version
```

If that command is not recognized, try the Windows Python launcher:

```powershell
py --version
```

## Installation and Setup

There are no third-party dependencies to install. Open PowerShell, change to this project folder, and run the chatbot:

```powershell
cd "C:\path\to\01-rule-based-chatbot"
python .\main.py
```

If `python` is unavailable but `py` works, run:

```powershell
py .\main.py
```

## Run the Tests

From this folder, run:

```powershell
python -m unittest -v
```

Or use the Python launcher:

```powershell
py -m unittest -v
```

The tests check greetings (including case, spacing, and punctuation), a general question, date/time responses, fallback and empty input, and exit commands.

## Example Conversation

```text
Welcome to RuleBot! Type 'bye', 'exit', or 'quit' to leave.
You:   GOOD morning!!!
RuleBot: Good morning! I hope you have a great day.
You: What is Python?
RuleBot: Python is a readable, general-purpose programming language used for many kinds of software.
You: Can you recommend a restaurant?
RuleBot: I'm not sure how to respond to that yet. Try asking about Python, AI, machine learning, chatbots, the date, or the time.
You: bye
RuleBot: Goodbye! Thanks for chatting with RuleBot.
```

## How Rule-Based Matching Works

The program first converts the input to lowercase, replaces punctuation with spaces, and collapses repeated whitespace. For example, `"  WHAT is Python?! "` becomes `"what is python"`. The chatbot then checks whether the complete normalized message is in its response rules or in the date/time/exit phrase sets. Exact phrase matching avoids accidental matches such as answering a question about `"hi"` just because those letters appear inside another word.

When the normalized message has no matching rule, the chatbot returns its fallback response. To add a response, add a normalized phrase and its reply to `RESPONSES` in `main.py`. Add date/time variations to their respective sets when needed.

## Limitations

- Responses are predefined and limited to the phrases in the code.
- It does not understand context, learn from conversations, or generate new answers.
- A question must match a supported phrase after normalization; arbitrary rewordings are not understood.
- Date and time come from the computer's local system clock.

## Possible Future Improvements

- Add more carefully selected phrase variations and topics.
- Keep a short conversation history to support simple follow-up rules.
- Move responses into a separate JSON file, while keeping the matching logic simple.
- Add configurable response wording and additional unit tests.

## GitHub Integration

Keep this project as a subfolder of the existing `CodeOrbit-AI-Internship` repository. Do not replace or edit the repository's root `README.md`, and do not add or remove the other project folders. Stage only the chatbot files.

### If the repository is already cloned

In PowerShell, change to the repository root (the directory containing its `.git` folder), and check its current state and branch:

```powershell
Get-Location
git status --short --branch
git branch --show-current
```

If this standalone project folder is not already inside that repository, copy only its contents into the target subfolder. Replace the source path below with the actual location of this project; the destination should be the existing repository's `01-rule-based-chatbot` folder:

```powershell
$source = "C:\path\to\01-rule-based-chatbot"
$destination = Join-Path (Get-Location) "01-rule-based-chatbot"
New-Item -ItemType Directory -Force -Path $destination
Copy-Item -Path (Join-Path $source "*") -Destination $destination -Force
Copy-Item -Path (Join-Path $source ".gitignore") -Destination $destination -Force
```

If the project files are already in the repository's `01-rule-based-chatbot` folder, skip the copy commands.

Review the target files and stage only those files:

```powershell
git status --short
git add -- 01-rule-based-chatbot/main.py 01-rule-based-chatbot/test_main.py 01-rule-based-chatbot/README.md 01-rule-based-chatbot/.gitignore 01-rule-based-chatbot/requirements.txt
git diff --cached --stat
git diff --cached
```

Commit the changes, then push to the branch reported by `git branch --show-current`:

```powershell
git commit -m "Add rule-based chatbot internship project"
$branch = git branch --show-current
git push -u origin $branch
```

Confirm the branch before pushing. These commands do not assume that the branch is named `main`.

### If the repository has not been cloned

Clone the existing central repository (this does not create a new repository), then enter its folder:

```powershell
cd "C:\path\where\you\keep\projects"
git clone https://github.com/YOUR-GITHUB-USERNAME/CodeOrbit-AI-Internship.git
Set-Location .\CodeOrbit-AI-Internship
git status --short --branch
git branch --show-current
```

Replace `YOUR-GITHUB-USERNAME` with the repository owner's public GitHub username. Do not put passwords, tokens, or other credentials in commands or project files. Follow the already-cloned steps above to copy and commit this project.

## Test Cases

| Test | Input / action | Expected result |
|---|---|---|
| Recognized greeting | `hello` | A friendly hello response. |
| Different capitalization | `HELLO` | The same response as `hello`. |
| Extra spaces | `  hi   ` | A friendly response for `hi`. |
| Recognized question | `What is Python?` | A short explanation of Python. |
| Date query | `what is the date` | The current local date in weekday, month, day, year format. |
| Time query | `what time is it` | The current local time in 12-hour format with seconds and AM/PM. |
| Unknown input | `Can you recommend a restaurant?` | The helpful fallback response. |
| Empty input | An empty string or spaces | A prompt to enter a message; the chatbot remains running. |
| Exit command | `bye`, `exit`, or `quit` | A goodbye response and a clean end to the loop. |
| Punctuation | `GOOD morning!!!` | A greeting response matching `good morning`. |

## Beginner Learning Notes

- **Rule-based chatbot:** A program that follows rules written by its developer. RuleBot selects a prepared response; it does not understand the meaning of a message as a generative AI model would.
- **`input()`:** `input("You: ")` displays a prompt, waits for the user to type a line, and returns that line as a string.
- **Normalization:** Lowercasing and removing punctuation in a consistent way lets `HELLO`, `hello`, and `hello!` use the same rule.
- **Conditions and matching:** An `if` statement checks a condition. For example, `if normalized_message in EXIT_COMMANDS` checks whether the complete message is one of the exit phrases.
- **Functions:** `normalize_input`, `generate_response`, and `chat` each handle one responsibility, making the program easier to read and test.
- **Fallback:** If no phrase matches a rule, `generate_response` returns a helpful suggestion rather than failing.
- **Conversation loop:** `while True` repeats the prompt and response steps so multiple messages can be entered.
- **Exiting:** When the normalized input equals `bye`, `exit`, or `quit`, the program displays goodbye and uses `break` to leave the loop. Ctrl+C and end-of-input are also handled cleanly.

## Internship Attribution

**CodeOrbit Tech AI Internship** — Rule-Based Chatbot project.

## Demonstration Checklist

1. Run the unit tests and show that they pass.
2. Start the chatbot and demonstrate at least one greeting with different capitalization or punctuation.
3. Ask a supported general-knowledge question and request the date or time.
4. Enter an unsupported question to demonstrate the fallback.
5. Exit with `bye` and explain that the responses come from predefined rules.
