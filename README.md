# 📘 Gemini-Powered Document Locator

This Flask web application allows users to upload a document (PDF or image), ask a specific question about it, and receive an **extracted answer along with its approximate location and page number** using Google's Gemini large language model.

---

## 🚀 Features

- Upload PDFs or images of documents
- Ask a natural language question (e.g. "What is the student's score?")
- Uses `gemini-1.5-flash` to extract and return:
  - The answer
  - Its location or context in the document
  - The page number (if available)

---

## 🧠 Powered By

- 🔮 [Google Generative AI (Gemini)](https://ai.google.dev/)
- 🧾 [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF-to-image conversion
- 🖼️ [Pillow](https://python-pillow.org/) for image processing
- ⚙️ Flask for the backend

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-doc-locator.git
cd gemini-doc-locator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API key

Create a `.env` file or export directly:

```bash
export GEMINI_API_KEY="your-google-api-key"
```

Get your API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## ▶️ Run the app

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📁 File Structure

```
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Upload form
│   └── result.html         # Display results
├── uploads/                # Temporary file uploads
```

---

## 🧪 Example Use

1. Upload a document like a scanned form, test, or paper.
2. Enter a question like:  
   `"Who signed the form?"`  
   or  
   `"What is the date of evaluation?"`
3. Receive structured output like:

```
Answer: Dr. Jane Smith
Location: Bottom of the form, above the signature line
Page: 1
```

---

## 🛡 License

MIT License
