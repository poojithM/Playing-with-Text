# P75 AI Text Processor

## Overview
The P75 AI Text Processor is a powerful Streamlit application designed to enhance and simplify your text interaction experience. Utilizing OpenAI's ChatOpenAI model, this app provides three key functionalities: Humanizing AI-generated text, summarizing long documents, and checking grammar. Each feature is crafted to improve the readability, conciseness, and grammatical integrity of text using advanced natural language processing techniques.

## Features
- **Humanizer**: Converts AI-generated text into natural, human-like language. This feature aims to remove the robotic feel of AI text, making it conversational and engaging while preserving the original meaning.
- **Text Summarizer**: Efficiently condenses long articles or documents into a brief summary that highlights key points and main ideas, maintaining the essence while omitting superfluous details.
- **Grammar Checker**: Analyzes text for grammatical errors and provides a corrected version, ensuring that the output is grammatically sound.

## How It Works
### Setup and Configuration
The application is built using Streamlit, an open-source app framework, which is ideal for rapid development of data applications. It leverages the OpenAI API, specifically using the `gpt-4` model from ChatOpenAI for processing text.

Before starting, the app loads environment variables and configures the API key required to authenticate with OpenAI's services.

### Detailed Functionality
- **Humanizer Function**: This feature takes user-provided AI-generated text as input and uses a custom prompt designed to instruct the model to rephrase the text in a more human-like manner. The rephrased version aims to be clear, expressive, and free from formal tones.
  
- **Text Summarizer Function**: It receives a block of text and applies a summarization prompt to extract the essence of the content. The summary is structured to be brief yet comprehensive, allowing for quick understanding.
  
- **Grammar Checker Function**: This tool scans the provided text for any grammatical inaccuracies and outputs a version corrected for grammar. This ensures that the text is not only accurate but also polished and professional.

### Streamlit Interface
The app's interface is straightforward, consisting of a text area where users can input text and three buttons corresponding to the features. Clicking on any button triggers the respective function and displays the results below the button in a clear, readable format.

## Installation
To run this application, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
