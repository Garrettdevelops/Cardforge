# Cardforge

A simple, open-source flashcard tool that converts CSV files into an interactive study system.

## Why?

Most flashcard apps are paid or restrictive.  
This tool allows anyone — a person, script, or AI — to generate a CSV and instantly turn it into a study system.

## Current Progress

- [x] Initial project setup
- [x] Read from CSV and validate answers
- [x] Add state tracking (track correct/incorrect answers)
- [x] CLI interface (Click / argparse)
- [x] Select input CSV via arguments
- [ ] Implement spaced repetition
- [ ] Upgrade to TUI/GUI

## Current Focus

Bug fixing and cleaning up the structure of the project 

## Example Input (CSV)

question,answer  
"What is 2+2?",4  
"What is the capital of France?",Paris  

## Vision

A lightweight, flexible flashcard system that:
- is fully local
- is scriptable
- works with any CSV generator
- evolves into a smarter study tool (spaced repetition + UI)

## Dev Notes

I want to add a results screen soon before I move onto the next step after this.  
I need to rewrite the README.md to make it reflect the actual structure and give instructions on how to install the package.  

