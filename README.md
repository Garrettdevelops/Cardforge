# Flashcard CLI (working name)

A simple, open-source flashcard tool that converts CSV files into an interactive study system.

## Why?

Most flashcard apps are paid or restrictive.  
This tool allows anyone — a person, script, or AI — to generate a CSV and instantly turn it into a study system.

## Current Progress

- [x] Initial project setup
- [x] Read from CSV and validate answers
- [x] Add state tracking (track correct/incorrect answers)
- [ ] CLI interface (Click / argparse)
- [ ] Select input CSV via arguments
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

just finished the most basic part of the CLI integration and now need to clean up a lot of this junk and decide what actually needs to be in the GH repo
Found a bug because the location of where the data is stored is based on where the CWD is, so that needs fixed.  
I want to add a results screen soon before I move onto the next step after this.  
I need to rewrite the README.md to make it reflect the actual structure and give instructions on how to install the package.  

