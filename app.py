from flask import Flask, request, jsonify, render_template
import whisper
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

# Ensure audio storage directory exists
AUDIO_DIR = os.path.join("data", "samples")
os.makedirs(AUDIO_DIR, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_audio():
    file = request.files["file"]
    filepath = os.path.join(AUDIO_DIR, file.filename)
    file.save(filepath)

    model = whisper.load_model("base")
    result = model.transcribe(filepath)
    transcript = result["text"]

    return jsonify({"transcript": transcript})


if __name__ == "__main__":
    app.run(debug=True)
