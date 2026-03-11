import streamlit as st

# MedDRA Dictionary
meddra_data = {
    "headache": {"PT": "Headache", "LLT": "Pain in head", "Code": "10019233"},
    "dizzy": {"PT": "Dizziness", "LLT": "Lightheadedness", "Code": "10013573"},
    "heart racing": {"PT": "Palpitations", "LLT": "Awareness of heart beat", "Code": "10033557"},
    "nausea": {"PT": "Nausea", "LLT": "Feeling queasy", "Code": "10028813"},
    "skin rash": {"PT": "Rash", "LLT": "Skin eruption", "Code": "10037844"},
    "tired": {"PT": "Fatigue", "LLT": "Lethargy", "Code": "10016256"},
    "chest pain": {"PT": "Chest pain", "LLT": "Discomfort chest", "Code": "10008479"}
}

st.set_page_config(page_title="MedDRA Auto-Coder", page_icon="💊")

st.title("💊 MedDRA Auto-Coder")
st.markdown("### Professional Portfolio Project: Supriya Bhati")
st.write("This tool demonstrates the use of logic-based mapping to convert patient 'verbatim' language into regulatory-standard MedDRA terms.")

query = st.text_input("Enter Patient Symptom (e.g., I have a bad headache):")

if query:
    found = False
    for key, values in meddra_data.items():
        if key in query.lower():
            st.success(f"✅ **Match Found**")
            col1, col2 = st.columns(2)
            col1.metric("Preferred Term (PT)", values["PT"])
            col2.metric("MedDRA Code", values["Code"])
            st.info(f"**Lowest Level Term (LLT):** {values['LLT']}")
            found = True
    
    if not found:
        st.error("No direct match found in the demo dictionary.")

st.sidebar.title("About this Project")
st.sidebar.info("This application bridges the gap between clinical pharmacy expertise and automated data coding in Pharmacovigilance.")
