from flask import Flask, render_template, request
import os
from PIL import Image
import google.generativeai as genai
import fitz  # PyMuPDF

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

UPLOAD_FOLDER = "uploads"
app = Flask(__name__)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def pdf_to_image(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    img_path = os.path.splitext(pdf_path)[0] + "_page1.png"
    pix.save(img_path)
    return Image.open(img_path)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract_text_position():
    file = request.files["file"]
    target_text = request.form["target_text"].strip()

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = pdf_to_image(filepath) if file.filename.lower().endswith(".pdf") else Image.open(filepath).convert("RGB")

    prompt = f"""
You are given an image of a document. Your task is to return the direction location of the text and the text of what we are asking for "{target_text}".

Return result in text format:
'The location is , the text is'
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    result_text = response.text

    return render_template("result.html", result=result_text, target=target_text)

if __name__ == "__main__":
    app.run(debug=True)
