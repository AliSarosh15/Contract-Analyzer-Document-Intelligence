from TandC.model.TCmodel import TermsCondition
from flask import app, request,Blueprint,jsonify
from app.extensions import db
import fitz
import os
from PIL import Image
import pytesseract
import requests
from werkzeug.utils import secure_filename  
import json


tc_bp=Blueprint("tandc",__name__)

UPLOAD_FOLDER ='my_uploads'
ALLOWED_FILES = ['png','jpg','jpeg','pdf']

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

def allowed_file(filename):

    fileext = filename.split('.')[1].lower()
    if fileext in ALLOWED_FILES:
        return fileext
    return "unsupported"

def summarise(text):
    prompt="""
Analyze the following Terms and Conditions and return a *strictly valid JSON object* with these exact fields:

- risky_clauses: Unfair terms like waiving legal rights, hidden fees, forced arbitration, or auto-renewals.
- data_privacy_issues: How data is collected, shared, stored, and user tracking concerns.
- cancellation_and_refund_policy: Rules about cancellations, refunds, and penalties.
- user_obligations_and_restrictions: Any user responsibilities or usage limits.
- governing_law_and_jurisdiction: Which laws apply and where disputes are settled.
- ambiguous_language: Vague or unclear clauses that may mislead users.
- summary: A brief consumer-friendly overview of key concerns.

Each field must be a dictionary with:
- "explanation": A short explanation (1 to 2 lines max)
- "quote": A direct quote from the text if possible (optional, can be empty)

Return *only* raw JSON (no markdown, no triple quotes, no language hints like ``json or '''json). The output must be strictly parseable by `json.loads().

Example:
{
  "risky_clauses": {
    "explanation": "The clause forces arbitration, limiting legal rights.",
    "quote": "Any disputes shall be resolved by binding arbitration..."
  },
  "data_privacy_issues": {
    "explanation": "...",
    "quote": "..."
  },
  ...
}

Now analyze the following Terms and Conditions:
{text}
"""
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    },
    data=json.dumps({
    "model": "mistralai/mistral-small-3.2-24b-instruct:free",
    "messages": [
        {
        "role": "system",
        "content": prompt
        }
,
      {
        "role": "user",
        "content": text
      }
    ]}))
    print(response.content)
    response = json.loads(response.content.decode('utf-8'))
    print(response)
    raw= response["choices"][0]["message"]["content"]
    print("raw model output:\n",raw)
    return (raw)

def extract_text_from_file(file_path,ext):
    text=""
    if ext=='pdf':
        doc= fitz.open(file_path)
        for page in doc:
            text+=page.get_text()
        doc.close()
    elif ext in ['png','jpg','jpeg']:
        img= Image.open(file_path)
        text=pytesseract.image_to_string(img)
    else:
        raise ValueError("unsupported file format")
    
    return text

@tc_bp.route('/upload',methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error":"no file part"})
    file=request.files['file']
    print(file.filename)

    if file.filename=='':
        return jsonify({"error":"no selected files"})
    
    if file:
        ext = allowed_file(file.filename)
        if ext!="unsupported":
            filename=secure_filename(file.filename)
            saved_path=os.path.join(UPLOAD_FOLDER,file.filename)
            file.save(saved_path)

            try:
                text= extract_text_from_file(saved_path,ext)
                sum=summarise(text)
                return jsonify({"filename":filename,"summary":sum})
            except Exception as e:
                return jsonify({"error":str(e)})
    return jsonify({"error":"file type not allowed"})

            





@tc_bp.route('/post_txt',methods=["POST"])
def post_text():
    data=request.get_json()
    text=TermsCondition(tc_content=data["tc_content"],req_user=data["req_user"],products_company=data["products_company"],product_name=data["product_name"])
    db.session.add(text)
    db.session.commit()
    return jsonify({"message":"data uploaded"})

