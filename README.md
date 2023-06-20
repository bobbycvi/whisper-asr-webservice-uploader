# Whisper ASR Web Service

This is a simple Flask application that allows users to upload an MP3 file to a server. The file is then processed by a Whisper ASR (Automatic Speech Recognition) service. The result from the ASR service is written to a `.txt` file in the "results" folder.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

The project requires the following Python libraries: `Flask`, `Requests`, `Werkzeug`. 

You can install them using pip:
```
pip install Flask
pip install Requests
pip install Werkzeug
```

### Running the Application

To start the application, navigate to the project directory and run the following command:


By default, the application will be running on `http://127.0.0.1:5000/`

### Using the Application

On the main page of the application, you can upload an MP3 file. Click on the "Submit" button to process the file. A loading message will be displayed while the file is being processed.

Once the file is processed, a success page will be displayed. The result of the ASR service is written to a `.txt` file in the "results" folder. The result file will have the same base name as the uploaded file, but with a `_result.txt` extension.

## Application Structure

- `app.py`: The main Flask application. This script handles the routing for the application, manages file upload and saving, and communicates with the ASR service.
- `index.html`: The main page of the application. This page provides a form for the user to upload an MP3 file.
- `result.html`: The error page. If there was an error in processing, an error message will be displayed.
- `success.html`: The success page. If the ASR service successfully processed the uploaded file, a success message is displayed.

## Note

Make sure the Whisper ASR service is available and correctly configured. The current URL used is `http://192.168.1.100:9000/asr`. You may need to adjust this based on your setup. Also, ensure the "uploads" and "results" directories exist in the same location as `app.py`.

## License

This project is licensed under the MIT License.
