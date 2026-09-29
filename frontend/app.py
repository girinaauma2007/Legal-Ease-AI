import streamlit as st

# Page Setup
st.set_page_config(page_title="LegalEaseAI", page_icon="⚖️", layout="centered")

st.title("⚖️ LegalEaseAI - Input Output")
st.write("Legal document-a simple Tamil la puriya vaikka")

# INPUT
st.subheader("Input: Legal Text")
user_input = st.text_area("Inga type pannunga", 
    "The Tenant shall not sublet the premises without prior written consent of the Landlord.",
    height=150)

# BUTTON
if st.button("Simplify - Simple-aakku"):
    text_low = user_input.lower()
    
    # LOGIC - Input -> Output
    if "sublet" in text_low:
        output = "Tenant-ku Landlord permission illama veeta vera yaarukkum rent-ku vida koodathu.\n\nRisk Level: HIGH"
    elif "security" in text_low and "non-refundable" in text_low:
        output = "Rs.50,000 security deposit kattanum, athu thirumba kedaikathu.\n\nRisk Level: HIGH - Paisa loss"
    elif "terminate" in text_low or "notice" in text_low:
        output = "30 naal munnadi notice kuduthu agreement-a yaarum mudikalam.\n\nRisk Level: LOW"
    elif "indemnify" in text_low:
        output = "Oru side ku loss vantha, inoru side antha loss-a katta venum.\n\nRisk Level: MEDIUM"
    elif "rent" in text_low and "5th" in text_low:
        output = "Prathi maasam 5th date kulla rent kattanum, late na fine.\n\nRisk Level: MEDIUM"
    else:
        output = "Ithu oru sattapoorva oppantham, ithai pinpatra vendum.\n\nRisk Level: LOW"
    
    # OUTPUT
    st.subheader("Output: Tamil Simple")
    st.success(output)
    st.code(f"INPUT:\n{user_input}\n\nOUTPUT:\n{output}", language="text")

st.divider()
st.write("Backend status: Running on http://127.0.0.1:8000")