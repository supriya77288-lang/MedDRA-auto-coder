import streamlit as st
import pandas as pd

# 1. Load the data from your CSV
@st.cache_data
def load_data():
    # This reads the CSV file you uploaded to GitHub
    return pd.read_csv("symptoms.csv - Canadian Symptom Mapping for PV.csv")

df = load_data()

st.set_page_config(page_title="MedDRA Auto-Coder", page_icon="💊")

st.title("💊 Pharmacovigilance Auto-Coder")
st.markdown("""
This tool maps patient-reported symptoms to standardized MedDRA terms. 
Designed for regulatory compliance and data consistency.
""")

# 2. User Input
user_input = st.text_input("Enter patient symptoms (e.g., dizzy, headache):").lower()

if user_input:
    # 3. Clean and process the input
    # We split by comma or space to handle multiple symptoms
    query_terms = [term.strip() for term in user_input.replace(",", " ").split()]
    
    st.subheader("Coding Results:")
    found_results = []
    
    # 4. Search logic: Iterate through the CSV
    # We check if any of the user's terms exist within the "Verbatim" column
    for term in query_terms:
        if term:
            # Look for matches in the Verbatim column
            match = df[df['Verbatim (Patient Input)'].str.contains(term, case=False, na=False)]
            if not match.empty:
                found_results.append(match)
    
    # 5. Display the findings
    if found_results:
        # Combine all matches and remove duplicates
        results_df = pd.concat(found_results).drop_duplicates()
        st.success(f"Successfully mapped {len(results_df)} terms:")
        st.table(results_df)
    else:
        st.warning("No official matches found. Please check spelling or try common terms.")

# 6. Footer
st.sidebar.markdown("---")
st.sidebar.info("Developed by [Your Name] | Pharm-Tech Integration Project")
