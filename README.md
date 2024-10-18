# Voice Assistant

This is a Python-based voice assistant that can perform various tasks, such as playing music, searching the web, telling the time, telling jokes, opening applications, and even interacting with the user through voice commands.

## Features

- **Voice Interaction**: The assistant can recognize your voice commands and respond accordingly.
- **Web Search and Navigation**: Opens popular websites or performs searches based on your commands.
- **Media Playback**: Can play music from a specified directory or open YouTube music.
- **Jokes**: Tells jokes to entertain the user.
- **Time and Date**: Provides the current time and date.
- **Notes**: Can take, store, and read notes.
- **Location and Directions**: Provides location information and directions using Google Maps.
- **Software Control**: Opens applications like Google Chrome and Visual Studio Code.
- **Translation**: Translates text using Google Translate.
- **Command Prompt**: Opens the command prompt.

## Installation

### Prerequisites

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Required Packages

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
The `requirements.txt` file contains the following dependencies:
- `pyttsx3`
- `SpeechRecognition`
- `wikipedia`
- `pyjokes`
- `requests`

### Run the Voice Assistant

To start the voice assistant, run the `main.py` script:

```bash
python Jarves.py
```
## Usage

1. **Start the Assistant**: 
   - Run the voice assistant by executing the `Jarves.py` script:
     ```bash
     python Jarves.py
     ```
   - The assistant will greet you and wait for your commands.

2. **Give Voice Commands**: 
   - Use natural language to interact with the assistant. Some example commands include:
     - "Open Google"
     - "Play music"
     - "What is the time?"
     - "Tell me a joke"
     - "Where is New York?"
     - "Translate hello to Bengali"
     - "Write a note"
     - "Show note"
     - "What is my IP address?"

3. **Stop the Assistant**: 
   - Say "exit" to end the assistant's session.

## Customization

You can modify the code to customize the assistant's behavior or add more features. The main sections to update are:
- **Voice recognition and response**: Customize the `takeCommand()` and `speak()` functions.
- **Command handling logic**: Add or modify commands in the main `while` loop.

## Troubleshooting

- **Speech Recognition Issues**: Make sure your microphone is functioning properly and that the `SpeechRecognition` library is installed correctly.
- **pyttsx3 Not Speaking**: Verify that the correct voice package is installed for your system, and adjust the voice settings in the code if needed.
- **Dependencies Missing**: Make sure you have installed all the dependencies listed in the `requirements.txt` file.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues to propose new features or report bugs.
