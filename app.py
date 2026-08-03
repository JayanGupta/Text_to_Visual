import streamlit as st
import pandas as pd
import os
import json
from engine.query_processor import LogicEngine
from assets.charts import ChartLibrary
from google import genai

# Page Config
st.set_page_config(page_title="Text to Visual", page_icon="📊", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background-color: #0e0e0e;
        color: white;
    }
    
    .main {
        background: radial-gradient(circle at top left, #6c63ff22, transparent 40%),
                    radial-gradient(circle at bottom right, #1a1a2e, #0e0e0e);
    }
    
    .stTextInput > div > div > input {
        background-color: #1c1c2e !important;
        color: white !important;
        border: 1px solid #6c63ff !important;
        border-radius: 20px !important;
        padding: 10px 20px !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #6c63ff, #48cfad) !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #6c63ff66;
    }
    
    .metric-card {
        background: #1c1c2e;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #6c63ff;
        margin-bottom: 20px;
    }
    
    h1, h2, h3 {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Helper function for Gemini
def call_gemini(prompt):
    api_key = st.session_state.get("api_key") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return json.dumps({
            "error": "Missing API Key. Please provide it in the sidebar."
        })
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return json.dumps({"error": str(e)})

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Text to Visual")
    st.markdown("---")
    st.markdown("### 🔑 API Key")
    api_key_input = st.text_input("Google Gemini API Key", type="password", placeholder="Paste your API key here")
    if api_key_input:
        st.session_state.api_key = api_key_input
        st.success("API Key saved!")

    st.markdown("---")
    st.markdown("### 📁 Upload Data")
    uploaded_file = st.file_uploader("Upload any CSV file", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded **{len(df):,}** rows")
        st.session_state.df = df
        st.session_state.engine = LogicEngine(df)
        
        st.markdown("---")
        st.markdown("### 🗂️ Columns Detected")
        for col in df.columns:
            st.markdown(f"- `{col}`")
    else:
        st.info("Upload a CSV to begin exploration.")

# Main Layout
st.title("📊 Text to Visual")
st.subheader("Ask questions in plain English. Get instant charts.")

if 'df' in st.session_state:
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("### 🔍 Ask a Question")
        query = st.text_input("What do you want to explore?", placeholder="e.g. Top 10 rows by sales", key="query_input")
        submit = st.button("Generate Visualization")
        
        st.markdown("---")
        st.markdown("### 📊 Dataset Overview")
        st.write(f"**Rows:** {len(st.session_state.df):,}")
        st.write(f"**Columns:** {len(st.session_state.df.columns)}")
        if st.checkbox("Show Raw Data (first 10 rows)"):
            st.dataframe(st.session_state.df.head(10))

    with col2:
        if submit and query:
            with st.spinner("Analyzing with Gemini..."):
                plan = st.session_state.engine.process_query(query, call_gemini)
                
                if isinstance(plan, dict) and "error" in plan:
                    st.error(plan["error"])
                else:
                    try:
                        result_df = st.session_state.engine.execute_logic(plan)
                        
                        chart_type = plan.get('chart_type', 'bar')
                        x = plan.get('x')
                        y = plan.get('y')
                        title = plan.get('title', 'Generated Visual')
                        
                        st.markdown(f"### {title}")
                        
                        if chart_type == 'bar':
                            fig = ChartLibrary.bar_chart(result_df, x, y, title)
                        elif chart_type == 'line':
                            fig = ChartLibrary.line_chart(result_df, x, y, title)
                        elif chart_type == 'scatter':
                            fig = ChartLibrary.scatter_plot(result_df, x, y, title)
                        elif chart_type == 'pie':
                            fig = ChartLibrary.pie_chart(result_df, x, y, title)
                        elif chart_type == 'histogram':
                            fig = ChartLibrary.histogram(result_df, x, title)
                        else:
                            fig = ChartLibrary.bar_chart(result_df, x, y, title)
                        
                        st.plotly_chart(fig, use_container_width=True)
                        
                        with st.expander("🔧 Technical Details"):
                            st.code(plan['pandas_code'], language='python')
                            
                    except Exception as e:
                        st.error(f"Logic Error: {str(e)}")
        else:
            st.info("👋 Upload a dataset and enter a query to generate a visualization.")
else:
    st.warning("👈 Upload a CSV file in the sidebar to start exploring.")

st.markdown("""
<div style='text-align: center; color: #444; padding: 20px; margin-top: 40px;'>
    Built by Jayan
</div>
""", unsafe_allow_html=True)
