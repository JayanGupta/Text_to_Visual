# 📊 Text to Visual

> **Ask questions in plain English. Get instant charts.**  
> An AI-powered data exploration tool that turns any CSV into interactive visualizations using Google Gemini.

---

## ✨ Features

- 🗣️ **Natural Language Queries** — Ask things like *"Show top 10 by sales"* or *"Distribution of ages"*
- 📁 **Works with Any CSV** — Not locked to any domain. Sales, HR, finance, sports — upload and go
- 🤖 **Powered by Gemini 2.5 Flash** — Fast, accurate query-to-code translation
- 📈 **5 Chart Types** — Bar, Line, Scatter, Pie, Histogram — picked automatically
- 🔒 **API Key in UI** — No `.env` files needed; paste your key directly in the sidebar
- 🎨 **Premium Dark UI** — Built with Streamlit, styled for a polished experience

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/your-username/text-to-visual.git
cd text-to-visual
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Use it
1. Paste your **Google Gemini API key** in the sidebar
2. Upload **any CSV file**
3. Type a question and hit **Generate Visualization**

---

## 📁 Project Structure

```
text_to_visual/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore
├── engine/
│   └── query_processor.py  # Gemini-powered NL → Pandas logic engine
└── assets/
    └── charts.py           # Styled Plotly chart library
```

---

## ☁️ Deploy on Render

1. Push this repo to **GitHub**
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Set the following:

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

5. Click **Deploy** 🎉

> **Note:** You can optionally set `GOOGLE_API_KEY` as an environment variable in Render so users don't need to paste it manually.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| AI | Google Gemini 2.5 Flash (`google-genai`) |
| Data | Pandas |
| Charts | Plotly Express |

---

## 📌 Example Queries

| Query | Chart Type |
|---|---|
| Top 10 rows by revenue | Bar |
| Sales trend over time | Line |
| Age vs salary | Scatter |
| Revenue share by region | Pie |
| Distribution of customer ages | Histogram |

---

*Built by **Jayan***
