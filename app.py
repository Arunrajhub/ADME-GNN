import streamlit as st
import torch
from rdkit import Chem
from rdkit.Chem import AllChem, Draw, Descriptors, Lipinski
from streamlit_molstar import st_molstar
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. THE AETHER-TOX DESIGN SYSTEM ---
st.set_page_config(page_title="AETHER-TOX | Industrial ADMET", layout="wide")

st.markdown("""
    <style>
    /* Dark Matter Aesthetics */
    .stApp { background: radial-gradient(circle at top, #0d1117, #010409); color: #c9d1d9; }
    
    /* Hero Header */
    .hero-text { font-family: 'Space Grotesk', sans-serif; background: linear-gradient(90deg, #58a6ff, #bc8cff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem; font-weight: 800; letter-spacing: -2px; margin-bottom: 0px; }
    
    /* Pro Cards */
    .metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    
    /* Clean Typography */
    h1, h2, h3 { border: none !important; color: #f0f6fc !important; font-family: 'Inter', sans-serif; }
    
    /* Input Styling */
    .stTextInput>div>div>input { background-color: #0d1117 !important; border: 1px solid #30363d !important; color: #58a6ff !important; font-family: 'Roboto Mono', monospace; }
    
    /* Button Aesthetics */
    .stButton>button { background: #238636; border: none; border-radius: 6px; padding: 10px 24px; font-weight: 600; width: 100%; transition: 0.3s; }
    .stButton>button:hover { background: #2ea043; box-shadow: 0 0 15px rgba(46, 160, 67, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE TOP NAVIGATION (MODERN) ---
st.markdown("<h1 class='hero-text'>AETHER-TOX</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#8b949e; margin-top:-10px; margin-bottom:25px;'>NEURAL GRAPH ARCHITECTURE FOR BIOMOLECULAR RISK ASSESSMENT</p>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Clinical Overview", "Deep Analytics", "Metabolic Logic", "Space Map"],
    icons=["activity", "layers", "diagram-3", "bounding-box"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#58a6ff", "font-size": "18px"}, 
        "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px", "--hover-color": "#21262d", "color": "#8b949e"},
        "nav-link-selected": {"background-color": "#21262d", "color": "#f0f6fc", "border-bottom": "3px solid #58a6ff"}
    }
)

# --- 3. INPUT SECTION ---
smiles_input = st.text_input("INPUT MOLECULAR IDENTIFIER (SMILES):", "COC1=C(O)C=CC(=C1)C=CC(=O)CC(=O)C=CC2=CC=C(O)C(OC)=C2")
mol = Chem.MolFromSmiles(smiles_input)

st.markdown("---")

# --- 4. LOGIC LAYERS ---
if selected == "Clinical Overview":
    col1, col2 = st.columns([1.2, 0.8])
    with col1:
        if mol:
            mol_3d =
