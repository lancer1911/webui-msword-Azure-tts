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

## License

This project is open source and available under the [MIT License](LICENSE).
