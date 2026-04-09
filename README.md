# Flashcard CLI (working name)

A simple, open-source flashcard tool that converts CSV files into an interactive study system.

## Why?

Most flashcard apps are paid or restrictive.  
This tool allows anyone — a person, script, or AI — to generate a CSV and instantly turn it into a study system.

## Current Progress

- [x] Initial project setup
- [x] Read from CSV and validate answers
- [ ] Add state tracking (track correct/incorrect answers)
- [ ] CLI interface (Click / argparse)
- [ ] Select input CSV via arguments
- [ ] Implement spaced repetition
- [ ] Upgrade to TUI/GUI

## Current Focus

Building state tracking using JSON so the program can:
- track performance per question
- enable future spaced repetition logic

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

~15 commits in so far.  
Recently added a tracking class with multiple methods to manage state.

Next step: persist state using JSON.
