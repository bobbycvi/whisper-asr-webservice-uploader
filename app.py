import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["RESULTS_FOLDER"] = "results"
app.config["ALLOWED_EXTENSIONS"] = {"mp3"}


def process_file(filename):
    url = "http://192.168.1.100:9000/asr"
    with open(filename, "rb") as audio_file:
        files = {"audio_file": audio_file}
        response = requests.post(url, files=files)
    response.raise_for_status()

    result = response.text
    filename_only = os.path.basename(filename)
    result_filename = f"{os.path.splitext(filename_only)[0]}_result.txt"
    result_path = os.path.join(app.config["RESULTS_FOLDER"], result_filename)
    with open(result_path, "w") as result_file:
        result_file.write(result)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(tuple(app.config["ALLOWED_EXTENSIONS"])):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            try:
                process_file(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                return redirect(url_for("success"))
            except requests.exceptions.HTTPError as e:
                error_message = str(e.response.content)
                app.logger.error("Error processing file: %s", error_message)
                return render_template("result.html", error=error_message)
            except Exception as e:
                app.logger.error("Error processing file")
                app.logger.exception(e)
                return render_template("result.html", error="Error processing file")
        else:
            return render_template(
                "index.html", error="Invalid file format. Please upload an MP3 file."
            )
    else:
        return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
