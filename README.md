# webui-msword-Azure-tts

This project is a simple web application that converts Microsoft Word (.docx) files to MP3 format using Azure Text-to-Speech services.

## Features

- Upload a Microsoft Word (.docx) file
- Choose a language and voice for the Text-to-Speech conversion
- Listen to the converted MP3 file
- Download the converted MP3 file
- Delete the converted MP3 file and the original .docx file from the server

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/webui-msword-Azure-tts.git
```

2. Change into the project directory:

```bash
cd webui-msword-Azure-tts
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5321` to access the application.

3. Azure subscription key and the Region for the Azure Text-to-Speech service are needed. Follow the instructions at [BobTranslate](https://bobtranslate.com/service/translate/microsoft.html#_2-%E6%B3%A8%E5%86%8C-azure) to obtain an API key.

## Technologies

- Python
- Flask web framework
- Azure Cognitive Services Text-to-Speech API
- HTML, CSS, and JavaScript for frontend

# Docker 
## https://hub.docker.com/r/lancer1911/webui-msword-azure-tts

This repository contains a Flask-based web application that provides an interface for converting Microsoft Word documents into speech using Azure Cognitive Services Text-to-Speech API. The application is designed to run inside a Docker container, making it easy to deploy and manage.

## Features

- Upload Microsoft Word documents (.docx)
- Convert the text within the Word document to speech using Azure Cognitive Services Text-to-Speech API
- Serve the generated audio file for playback or download
- Input Azure Speech Services API key and region directly through the web interface

## Prerequisites

- Docker installed on your machine
- An Azure account with an active subscription

## How to use

### 1. Clone the repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/lancer1911/webui-msword-azure-tts.git
```

### 2. Build the Docker image

Navigate to the root of the repository and build the Docker image using the following command:

```bash
docker build -t webui-msword-azure-tts .
```

### 3. Run the Docker container

Run the Docker container using the following command:

```bash
docker run -p 5321:5321 webui-msword-azure-tts
```

### 4. Access the web application

Open a web browser and visit `http://localhost:5321` to access the web application. You will be prompted to enter your Azure Speech Services API key and region through the web interface.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
