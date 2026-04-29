# Cardforge

A simple, open-source flashcard tool that converts CSV files into an interactive study system.

## Why?

Most flashcard apps are paid or restrictive.  
Cardforge lets you create flashcards your way whether by hand, spreadsheet, or AI-generated CSV, and instantly turn them into a study system.

## Features (Current)

- Read questions and answers from CSV 
- Validate user input against answers
- Track correct/incorrect responses
- Command-line interface (CLI)
- Select input CSV via command-line arguments

## Roadmap

- [x] Add tests  
- [ ] Implement case-insensitive answer checking  
- [ ] Add results screen  
- [ ] Randomize question order  
- [ ] Implement spaced repetition  
- [ ] Upgrade to TUI/GUI  

## Current Focus

Implementing case-insensitice answer checking

## Example Input (CSV)

```
question,answer
"What is 2+2?",4
"What is the capital of France?",Paris
```

## Installation

Clone the repository:

```
git clone https://github.com/Garrettdevelops/Cardforge
cd Cardforge
```

Install the package:

```
pip install .
```

### Optional: Virtual Environment

```
python -m venv venv
source venv/bin/activate
pip install .
```

### Development Mode (Recommended)

If you plan to modify the code without reinstalling:

```
pip install -e .
```

## Usage


```
flashcard init my_cards.csv # creates a study deck 
flashcard run my_cards # runs the stored deck.
```

### Example
``` 
$ flashcard init capitals.csv
Deck created: capitals

$ flashcard run capitals
Question: What is the capital of France?
> Paris
Correct!
```


## Vision

A lightweight, flexible flashcard system that:

- runs fully locally  
- is scriptable and developer-friendly  
- works with any CSV generator  
- evolves into a smarter study tool (spaced repetition + UI)  
