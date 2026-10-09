# Flashcard_app

 Flashcard app built in python designed to help with A-level physics and maths revision


## Features

- Choose between different subject sets from a menu
- Cards are shuffled each time - they are displayed in a random order
- Tracks your score
- Lets you re-test only the cards you got wrong, until you know them all
- Cards are stored in JSON files, so you can add new ones without touching the code

## How to run

1. Install Python 3
2. Clone this repository:
   `git clone https://github.com/Ankita200716/flashcard_app.git`
3. Open a terminal in the project folder and run:
   `python flashcard.py`

## Adding your own cards

Create or edit a JSON file in this format :
```json 
{
    "Question one": "Answer one",
    "Question two": "Answer two"
}
```
Then add the file to the `sets` dictionary at the top of `flashcard.py`.

## What I learned

- Using dictionaries, lists, loops, and functions in Python
- Validating user input so the program doesn't break on unexpected answers
- Reading data from JSON files
- Using Git and GitHub to track my project with commits

## Future ideas

- Add new cards from inside the program
- Adding a text box to re-type the answer when you get it wrong
- Spaced repetition (missed cards appear more often)
- A web version using Streamlit