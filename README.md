# Simple DBMS (Part 1: CLI & Command Parser)
A lightweight console Database Management System (DBMS) implementation in Python. The first phase of this project provides an interactive Command Line Interface (CLI / REPL) and a syntax parsing engine for SQL-like commands.
Built entirely using Python's standard library (⁠sys⁠, ⁠re⁠) with zero external dependencies.
## Features (⁠part1⁠)
 ### REPL Interface (Read-Eval-Print Loop):
 <br> Reads input line-by-line from standard input (⁠sys.stdin⁠).</br>
 <br>Supports multi-line statement buffering (executes when encountering ⁠;⁠).</br>
 <br>Gracefully catches syntax errors without crashing the main loop.</br>
 ### Command Parsing & Validation:
 <br> Syntax validation for ⁠CREATE⁠, ⁠INSERT⁠, and ⁠SELECT⁠ statements via regular expressions.</br>
 <br>Verifies table existence and column count matches during insertions.</br>
 <br>Automatically strips single-line comments (⁠//⁠).</br>
## Command Syntax
| Command | Description | Example |
| :--- | :--- | :--- |
| CREATE | Create table structure | CREATE users(id, name, email); | 
| INSERT | Validation of data insertion into a table | INSERT INTO users("1", "Ivan", "email"); |
| SELECT | Request to view data from the table | SELECT FROM users; |
** All command must end with ;
