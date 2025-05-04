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
You are an intelligent assistant that analyzes a document image to locate specific information.

Objective:
Find the answer to the following query: "{target_text}"

Instructions:
1. Look at the document image.
2. Extract the exact answer to the query if it exists.
3. Determine its approximate position or context (e.g., section title, visual indicator).
4. If the document contains pages, include the page number.
5. If no answer is found, reply: "Answer not found in the document."

Respond in this format:
Answer: <the extracted answer>
Location: <brief description of where in the document it was found>
Page: <page number or 'N/A'>

Only include relevant information. Do not explain your reasoning.
"""


    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt, image])
    result_text = response.text

    return render_template("result.html", result=result_text, target=target_text)

if __name__ == "__main__":
    app.run(debug=True)
