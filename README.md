# 🌍 VisaVerse Navigator | AI-Powered Global Mobility Agent

> **VisaVerse AI Hackathon 2025 Submission**
> Removing barriers to global opportunity with structured AI intelligence.

<img width="1274" height="646" alt="image" src="https://github.com/user-attachments/assets/6c2d1eec-437c-47b1-b939-b2774441736e" />


## 💡 Inspiration: The 2025 Mobility Crisis
Moving borders has never been harder. In 2025, immigration rules are shifting rapidly—from the USA's new wage-weighted H-1B selection to evolving Digital Nomad policies in Europe. Navigating hundreds of pages of dense legal text is a massive barrier for global talent.

We built **VisaVerse Navigator** to be an intelligent, 24/7 mobility consultant that turns complex regulations into a clear, personalized roadmap.

## 🚀 What It Does
VisaVerse Navigator is a full-stack web application that performs a real-time **"Visa Gap Analysis"**:

1.  **Multimodal Input:** Accepts professional resumes (PDF).
2.  **Policy-Grounded Analysis:** Uses OpenAI's GPT-4o, explicitly prompted with late-2025 immigration rules for the USA, Portugal, Germany, and Canada.
3.  **Structured Intelligence:** Instead of a generic chat bubble, it outputs a strict JSON schema, powering a visual "Success Meter," identifying specific profile gaps, and generating a step-by-step action plan.

## 🛠️ How We Built It (Tech Stack)

* **AI Engine:** OpenAI GPT-4o (Snapshot `2024-08-06`)
    * *Key Technique:* utilized **Structured Outputs (JSON Schema)** to enforce reliable, parseable data returned by the LLM, ensuring zero-hallucination UI rendering.
    * *System Prompting:* Engineered complex system instructions to ground the AI in specific 2025 regulations (e.g., US H-1B wage levels vs. O-1 criteria).
* **Backend:** Flask (Python) for handling API requests and file processing.
* **Data Processing:** `PyPDF2` for extracting raw text from resume documents.
* **Frontend:** HTML5, CSS3 (Glassmorphism design), and Bootstrap for a responsive, modern user experience.

## ✨ Key Features

* **🇺🇸 USA 2025 Ready:** Specifically programmed to understand the shift to Wage-Weighted Selection and the rise of O-1/EB-2 NIW alternatives.
* **🎯 Visual Success Meter:** Instantly quantifies eligibility probability from 0-100%.
* **🔍 Gap Identification:** Doesn't just say "yes/no"—it highlights exactly what is missing (e.g., "Missing publications for O-1," "Salary below Level IV threshold").
* **🗺️ Dynamic Roadmap:** Generates actionable next steps based on the specific user profile.

## ⚙️ Installation & Local Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/visaverse-navigator.git](https://github.com/yourusername/visaverse-navigator.git)
    cd visaverse-navigator
    ```

2.  **Create a virtual environment & install dependencies**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up Environment Variables**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_sk_key_here
    ```

4.  **Run the application**
    ```bash
    python app.py
    ```
    Access the app at `http://127.0.0.1:5000`.

## 👥 The Team
* **R.Sai Shashi Kiran** - Software Engineer & AI Engineer

---
