# Cardforge

A simple, open-source flashcard tool that converts CSV files into an interactive study system.

## Why?

Most flashcard apps are paid or restrictive.  
Cardforge lets you create flashcards your way whether by hand, spreadsheet, AI-generated CSV, or even just adding your notes and instantly turn them into a study system.

## Features (Current)

- Read questions and answers from CSV 
- Track correct/incorrect responses
- Command-line interface (CLI)
- Select input CSV via command-line arguments
- Verbose option to display a results screen

## Roadmap

- [x] Add tests  
- [ ] Randomize question order  
- [ ] Add plain text and markdown note intake support
- [ ] Upgrade to TUI/GUI  

## Current Focus

Randomizing question order

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
The correct answer is Paris
Rate the question's difficulty 1-4, one being instantly remembered and 4 being no idea
> 1

```


## Vision

A lightweight, flexible flashcard system that:

- runs fully locally  
- is scriptable and developer-friendly  
- works with any CSV generator  
- evolves into a smarter study tool (spaced repetition + UI)  
