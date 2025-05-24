# Riley-AI Project Documentation

## Overview
Riley-AI (RILEY: Real-time Intelligent Logical Engine for You) is a modular Windows desktop application designed to function as a real-time intelligent assistant. Inspired by advanced AI systems, Riley-AI integrates voice interaction, memory, and dynamic multimodal features to assist users in various tasks, including invention, science, conversation, coding, and creative ideation.

## Features
- **Voice Interaction**: Communicate with Riley using natural language. Riley can respond with a natural-sounding voice and transcribe spoken commands.
- **Modular AI Core**: The application includes a modular reasoning system that can handle various types of queries, from scientific reasoning to emotional support.
- **Memory Engine**: Riley remembers user preferences and conversation history, allowing for personalized interactions.
- **Multiple Modes**: Switch between different operational modes, including Standard Chat, Inventor, Emotional Support, Scientific Reasoning, Coding Assistant, and Autonomous Mode.
- **Plugin Support**: Extend Riley's capabilities by adding custom plugins for specific tasks.
- **Self-Modification**: Riley can update its own code based on user instructions, allowing for continuous improvement.
- **Advanced Coding Knowledge**: Riley can answer coding questions and provide code snippets in various programming languages.
- **PyQt6 GUI**: The application features a PyQt6-based graphical user interface for chat and interaction.

## Installation
To set up the Riley-AI application, follow these steps:

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd riley_ai_app
   ```

2. **Install Python**:
   Ensure you have Python 3.9 or newer installed. Download it from [python.org](https://www.python.org/downloads/).

3. **Install Requirements**:
   Open PowerShell in the Riley-AI folder and run:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Launch the application by executing:
   ```
   python main.py
   ```

## File Structure
The project is organized as follows:

```
riley_ai_app/
├── main.py                # Entry point for the application
├── gui/                   # GUI components
│   ├── interface.py       # Defines the GUI layout and interactions
│   └── styles.qss         # Stylesheet for the application
├── audio/                 # Audio functionalities
│   ├── listener.py        # Manages voice input
│   └── speaker.py         # Handles text-to-speech
├── jarvis/                # AI reasoning and functionalities
│   ├── __init__.py        # Initializes the jarvis module
│   ├── core.py            # Main AI reasoning engine
│   ├── invention.py       # Generates invention ideas
│   ├── memory.py          # Manages memory engine
│   ├── code_assist.py     # Provides coding assistance
│   ├── equation_solver.py  # Implements equation solving
│   └── github_learning.py  # Analyzes GitHub repositories
├── config/                # Configuration files
│   ├── settings.yaml      # Application settings
│   └── personality.yaml    # Defines Riley's personality traits
├── database/              # Database files
│   └── memory.db          # SQLite database for memory logs
├── utils/                 # Utility functions
│   ├── logging.py         # Logging functionality
│   └── updater.py         # Manages self-modification
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation
```

## Usage
Once the application is running, you can interact with Riley using voice commands or text input. Use the control buttons in the GUI to switch modes, mute, reset memory, and access settings.

To ask a question or get assistance, type your query in the chat box and address "Riley". You can ask coding questions, request code snippets, or seek general help.

## Configuration
To enable advanced code answers, set your OpenAI API key in `main.py` or via an environment variable.

## Extending Riley
To add new features, modify the code in the `features/` folder. For GUI customizations, edit `gui/interface.py`.

## Contributing
Contributions to the Riley-AI project are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Special thanks to the open-source community for their contributions to the libraries and tools used in this project.

---

Riley-AI: Your sentient coding and invention assistant.

## Free OpenAI API Access with Puter.js

Riley-AI supports both official OpenAI API keys and free alternatives like Puter.js. If you do not have an OpenAI API key, you can use Puter.js to access GPT-3.5/4 for free. Below is a step-by-step guide to get started:

### What is Puter.js?
Puter.js is a free, community-powered API that provides access to OpenAI's GPT models without requiring a paid API key. It is suitable for personal, educational, and experimental use.

### How to Use Puter.js with Riley-AI

1. **Get a Puter.js API Endpoint:**
   - Visit [https://puter.com/ai](https://puter.com/ai) and sign up for a free account.
   - After logging in, go to the API section to find your free endpoint URL (e.g., `https://api.puter.com/v1/ai/gpt`).

2. **Update Riley-AI to Use Puter.js:**
   - Open `main.py` and `features/code_knowledge.py` in your Riley-AI folder.
   - Instead of using the `openai` Python package, you will send POST requests to the Puter.js endpoint.
   - Example code snippet to replace OpenAI usage:
     ```python
     import requests
     def answer(self, question, language="python"):
         prompt = f"You are Riley, an expert AI coding assistant. Answer the following question in {language} and explain your reasoning.\nQuestion: {question}"
         try:
             response = requests.post(
                 "https://api.puter.com/v1/ai/gpt",  # Replace with your endpoint
                 json={"prompt": prompt, "max_tokens": 512, "temperature": 0.2}
             )
             data = response.json()
             return data.get("choices", [{}])[0].get("text", "[Riley] No response.")
         except Exception as e:
             return f"[Riley] Sorry, I couldn't answer that due to: {e}"
     ```
   - You can add a toggle in `main.py` to switch between OpenAI and Puter.js endpoints.

3. **No API Key Required:**
   - Puter.js does not require an API key for basic usage, but you may need to be logged in or use a session token for higher limits.

4. **Limitations:**
   - Free APIs may have rate limits, slower response times, or occasional downtime. For mission-critical or commercial use, consider an official OpenAI API key.

### Integration Notes
- Riley-AI is designed to be modular. You can easily swap out the code in `features/code_knowledge.py` to use any compatible GPT endpoint.
- For advanced users: You can further abstract the API logic to support multiple providers and select them via a config file or GUI setting.

### Community Resources
- [Puter.js Documentation](https://puter.com/ai)
- [Riley-AI GitHub Issues](https://github.com/your-repo/issues) for help and troubleshooting

---

With Puter.js, you can use Riley-AI for free, with no paid API key required!