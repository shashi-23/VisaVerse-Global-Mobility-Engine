import os
import json
import io
import pypdf
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# Day 4 & 5: Advanced Structured Output Schema
VISA_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "name": "visa_analysis",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "score": {"type": "integer", "description": "Success probability 0-100"},
                "qualified_visas": {"type": "array", "items": {"type": "string"}},
                "missing_items": {"type": "array", "items": {"type": "string"}},
                "roadmap_steps": {"type": "array", "items": {"type": "string"}},
                "summary": {"type": "string"}
            },
            "required": ["score", "qualified_visas", "missing_items", "roadmap_steps", "summary"],
            "additionalProperties": False
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    country = request.form.get('country')
    file = request.files.get('resume')
    
    if not file:
        return jsonify({"error": "No resume uploaded"}), 400

    # PDF Processing
    reader = pypdf.PdfReader(io.BytesIO(file.read()))
    resume_text = " ".join([page.extract_text() for page in reader.pages])

    try:
        # Day 4: 2025 Policy-Aware Prompt
        response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system", 
                    "content": """You are a 2025 Global Mobility Specialist. 
                    CRITICAL UPDATES FOR USA (2025):
                    - New H-1B petitions filed after Sept 21, 2025, require a $100,000 employer surcharge.
                    - The H-1B lottery is being replaced by a 'Wage-Weighted Selection' (Level IV wages have highest priority).
                    - O-1 and EB-2 NIW are now the primary recommended paths for high-skilled talent to avoid the H-1B surcharge.
                    
                    Analyze the user's resume and return a strict JSON analysis."""
                },
                {"role": "user", "content": f"Country: {country}\nResume Content: {resume_text}"}
            ],
            response_format=VISA_SCHEMA
        )
        
        return jsonify(json.loads(response.choices[0].message.content))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)