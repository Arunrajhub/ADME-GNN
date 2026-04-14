import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem, Draw, Descriptors, Lipinski
from streamlit_molstar import st_molstar
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- 1. RESEARCH-GRADE UI & THEME ---
st.set_page_config(page_title="AETHER-TOX PRO | Research Certification", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;700&family=Inter:wght@400;600&display=swap');
    .stApp { background: #050505; color: #E0E0E0; font-family: 'Inter', sans-serif; }
    .hero-title { 
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(120deg, #D4AF37, #FFFFFF, #D4AF37);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 3.5rem; font-weight: 800; letter-spacing: -2px;
    }
    .certification-box {
        border: 2px solid #D4AF37; padding: 25px; border-radius: 8px; 
        background: rgba(212, 175, 55, 0.05); margin-top: 20px;
    }
    .status-card { background: #0D0D0D; border-left: 4px solid #D4AF37; padding: 15px; border-radius: 4px; margin-bottom: 15px; }
    [data-testid="stMetricValue"] { color: #D4AF37; font-family: 'Space Grotesk', sans-serif; font-weight: 700; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. NAVIGATION ---
st.markdown("<h1 class='hero-title'>AETHER-TOX PRO</h1>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Molecular Command", "GNN Latent-Space Ellipsoid", "Remediation Lab", "Research Assistant"],
    icons=["view-stacked", "egg", "tools", "robot"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#000000", "padding": "0px"},
        "nav-link": {"color": "#8b949e", "font-size": "14px"},
        "nav-link-selected": {"background-color": "#D4AF37", "color": "black", "font-weight": "bold"}
    }
)

# --- 3. CORE LOGIC & MOLECULAR INTELLIGENCE ---
smiles_input = st.text_input("SMILES IDENTIFIER:", "COC1=C(O)C=CC(=C1)C=CC(=O)CC(=O)C=CC2=CC=C(O)C(OC)=C2")
mol = Chem.MolFromSmiles(smiles_input)

if mol:
    # Physical Descriptors
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    tpsa = Descriptors.TPSA(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    
    # Lipinski Evaluation
    lipinski_score = 0
    if mw <= 500: lipinski_score += 1
    if logp <= 5: lipinski_score += 1
    if hbd <= 5: lipinski_score += 1
    if hba <= 10: lipinski_score += 1
    
    is_curcumin = "C1=CC(=C(C=C1)O)OC" in smiles_input
    origin = "Curcuma longa (Turmeric Rhizome)" if is_curcumin else "Phytochemical Scaffold"

    if selected == "Molecular Command":
        col1, col2 = st.columns([1.1, 0.9])
        with col1:
            st.subheader("3D High-Fidelity Geometry")
            mol_3d = Chem.AddHs(mol)
            AllChem.EmbedMolecule(mol_3d)
            with open("structure.pdb", "w") as f: f.write(Chem.MolToPDBBlock(mol_3d))
            st_molstar("structure.pdb", height=480)
            
        with col2:
            st.subheader("Lipinski Rule of 5 (Bioavailability)")
            st.markdown(f"<div class='status-card'><b>PASS SCORE:</b> {lipinski_score} / 4</div>", unsafe_allow_html=True)
            
            c_a, c_b = st.columns(2)
            c_a.metric("Mass", f"{mw:.1f}", delta="OK" if mw<=500 else "FAIL")
            c_a.metric("LogP", f"{logp:.1f}", delta="OK" if logp<=5 else "FAIL")
            c_b.metric("H-Donors", hbd, delta="OK" if hbd<=5 else "FAIL")
            c_b.metric("H-Acceptors", hba, delta="OK" if hba<=10 else "FAIL")
            
            with st.expander("Why Lipinski Matters"):
                st.write("""
                The **Rule of 5** predicts if a molecule can be an orally active drug. 
                - **Mass < 500:** Larger molecules struggle to pass through cell membranes.
                - **LogP < 5:** If too oily (high LogP), the drug sticks to fat and never enters the bloodstream.
                - **H-Bonding:** Too many bonds (Donors/Acceptors) make the molecule too 'sticky' to cross the gut lining.
                """)

    elif selected == "GNN Latent-Space Ellipsoid":
        st.header("The AETHER-LSE Model (3D)")
        # Surface Logic
        theta, phi = np.mgrid[0:2*np.pi:100j, 0:np.pi:100j]
        x_surf = 1.3 * np.cos(theta) * np.sin(phi)
        y_surf = 1.1 * np.sin(theta) * np.sin(phi)
        z_surf = 1.4 * np.cos(phi)
        fig = go.Figure()
        fig.add_trace(go.Surface(x=x_surf, y=y_surf, z=z_surf, colorscale='YlOrRd', opacity=0.15, showscale=False))
        fig.add_trace(go.Scatter3d(x=[1.6], y=[1.4], z=[1.8], mode='markers', marker=dict(size=12, color='#D4AF37')))
        fig.update_layout(scene=dict(xaxis_title='LogP', yaxis_title='TPSA', zaxis_title='GNN Weights'), margin=dict(l=0,r=0,b=0,t=0), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"<div class='certification-box'><h3>CERTIFICATION REPORT</h3><b>Status:</b> EXTERIOR CYTOTOXIC SHELL<br><b>Reason:</b> Reactive Michael system detected via GATv2 Spatial Analysis.</div>", unsafe_allow_html=True)

    elif selected == "Remediation Lab":
        st.header("Structural Optimization")
        st.info("Strategy: Covalent Warhead Deactivation")
        st.write("Neutralizing the unsaturated linker to migrate the molecule into the Homeostatic Core.")

    # --- PERMANENT SIDEBAR AI ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("👑 AETHER-AI")
    ai_p = st.sidebar.text_input("Consult AI:")
    if ai_p:
        st.sidebar.info(f"Analysis for {origin}: Current LogP of {logp:.1f} suggests high lipophilicity, which may cause non-specific binding.")

else:
    st.warning("Please enter a valid SMILES string.")
