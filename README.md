# Breakout Game

This project is a Breakout-style game developed using Python and the Pygame library. The game was created as an example and training exercise using OpenAI's ChatGPT-4 and the Aider tool.

## Game Description

In this Breakout game, you control a paddle to bounce a ball and break bricks. The game includes multiple levels, random gifts, and a scoring system. The objective is to clear all the bricks while avoiding losing the ball. The game ends when you run out of lives.

## Features

- Multiple levels with increasing difficulty
- Random gifts that provide power-ups or challenges
- Score and lives display
- Adjustable ball reflection angle based on paddle hit position

## Prerequisites

- Python 3.12.5
- Pygame 2.6.1

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd Breakout
    ```

2. Install the required Python packages:
    ```bash
    python -m pip install -U pygame
    ```

## Running the Game

To run the game, execute the following command:
```bash
python breakout.py
```

## Using Aider and OpenAI ChatGPT-4

This project was developed using OpenAI's ChatGPT-4 and the Aider tool. You can use these tools to further enhance and customize the game.

### Installation

1. Install the Aider tool:
    ```bash
    python -m pip install -U aider-chat
    ```

2. Set up your environment variables for OpenAI's Azure API:

    **Mac/Linux:**
    ```bash
    export AZURE_API_KEY=<key>
    export AZURE_API_VERSION=2023-05-15
    export AZURE_API_BASE=https://myendpt.openai.azure.com
    ```

    **Windows:**
    ```bash
    setx AZURE_API_KEY <key>
    setx AZURE_API_VERSION 2023-05-15
    setx AZURE_API_BASE https://myendpt.openai.azure.com
    # ... restart your shell after setx commands
    ```

3. Run Aider with your Azure deployment:
    ```bash
    aider --model azure/<your_deployment_name>
    ```

### Making Changes with Aider

To make changes to the code using Aider, follow these steps:

1. Open the file you want to edit.
2. Use the *SEARCH/REPLACE block* format to specify the changes. The format is as follows:

    ```python
    # Full file path
    C:\repo\Breakout\breakout.py
    ```python
    <<<<<<< SEARCH
    # Code to search for
