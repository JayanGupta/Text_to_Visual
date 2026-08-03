# Text to Visual

> **Ask questions in plain English. Get instant charts.**  
> An AI-powered data exploration tool that turns any CSV into interactive visualizations using Google Gemini.

---

## Features

- **Natural Language Queries** — Ask things like *"Show top 10 by sales"* or *"Distribution of ages"*
- **Works with Any CSV** — Not locked to any domain. Sales, HR, finance, sports — upload and go
- **Powered by Gemini 3.5 Flash** — Fast, accurate query-to-chart translation
- **5 Chart Types** — Bar, Line, Scatter, Pie, Histogram — picked automatically
- **API Key in UI** — No `.env` files needed; paste your key directly in the sidebar
- **Premium Dark UI** — Built with Streamlit, styled for a polished experience

---

## Quick Start

### Requirements
- Python 3.10 or higher (tested up to 3.14)
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### 1. Clone the repo
```bash
git clone https://github.com/JayanGupta/Text_to_Visual.git
cd Text_to_Visual
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

> You should see `(venv)` appear at the start of your terminal prompt. This confirms the virtual environment is active.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Use it
1. Paste your **Google Gemini API key** in the sidebar
2. Upload **any CSV file**
3. Type a question and hit **Generate Visualization**

---

## Why Virtual Environments?

When you clone a Python project on a new machine, none of the packages are pre-installed. A virtual environment (`venv`) creates an isolated, self-contained Python environment for this project only.

| Without `venv` | With `venv` |
|---|---|
| Packages installed globally, can conflict across projects | Each project has its own isolated packages |
| No guarantee the same versions are used on every machine | `requirements.txt` pins versions — anyone can reproduce your exact environment |
| Works on your machine, breaks on others | Works the same everywhere |

**The golden rule:** always activate your `venv` before running or installing anything for this project.

---

## Project Structure

```
Text_to_Visual/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies (pip install -r requirements.txt)
├── .gitignore
├── engine/
│   └── query_processor.py  # Gemini-powered NL → Pandas logic engine
└── assets/
    └── charts.py           # Styled Plotly chart library
```

---

## Deploy on Render

1. Push this repo to **GitHub**
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Set the following:

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

5. Click **Deploy**

> You can optionally set `GOOGLE_API_KEY` as an environment variable in Render so users don't need to paste it manually.

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| AI | Google Gemini 2.5 Flash (`google-genai`) |
| Data | Pandas |
| Charts | Plotly Express |

---

## Example Queries

| Query | Chart Type |
|---|---|
| Top 10 rows by revenue | Bar |
| Sales trend over time | Line |
| Age vs salary | Scatter |
| Revenue share by region | Pie |
| Distribution of customer ages | Histogram |

---

*Built by **Jayan***
