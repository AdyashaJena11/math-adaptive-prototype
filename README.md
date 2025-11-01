# Math Adventures - AI-Powered Adaptive Learning Prototype

This project is a minimal Python prototype for an adaptive math learning application, submitted for the "Adaptive Learning Assignment". The objective is to build a system that dynamically adjusts math puzzle difficulty based on user performance.

The prototype is designed to help children (ages 5-10) practice basic math (addition, subtraction, and multiplication) and keep them in their optimal challenge zone.

## Features

* **Dynamic Puzzle Generation**: Creates simple math problems on the fly.
* **Three Difficulty Levels**: Includes `Easy` (single-digit addition), `Medium` (double-digit add/subtract), and `Hard` (single-digit multiplication).
* **Performance Tracking**: Logs user correctness and response time for each puzzle.
* **Adaptive Engine**: Automatically adjusts the next puzzle's difficulty based on the user's recent performance.
* **Session Summary**: Displays an end-of-session performance report, including accuracy, total correct, and average time.

## Adaptive Logic Explained

This prototype uses a **simple, rule-based logic** for its adaptive engine. The decision to change difficulty is based on the user's performance on the **last two consecutive questions**.

* **Promotion**: If the user gets **2 answers in a row correct**, the difficulty is increased (e.g., Easy $\rightarrow$ Medium).
* **Demotion**: If the user gets **2 answers in a row incorrect**, the difficulty is decreased (e.g., Medium $\rightarrow$ Easy).
* **Maintain**: If performance is mixed (one correct, one incorrect), the difficulty level remains the same to ensure stability.

## How to Run

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/AdyashaJena11/math-adaptive-prototype.git](https://github.com/AdyashaJena11/math-adaptive-prototype.git)
    cd math-adaptive-prototype
    ```

2.  **Navigate to the source directory:**
    ```sh
    cd src
    ```

3.  **Run the application:**
    ```sh
    python main.py
    ```

4.  The application is a console app. It will first ask for your name and initial difficulty to begin the session.

## Repository Structure

The code is organized into modules as recommended by the assignment.
