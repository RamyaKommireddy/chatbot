import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Healthcare Chatbot",
    page_icon="🩺",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
.chat-box {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user {
    color: #d63384;
    font-weight: bold;
}
.bot {
    color: #0d6efd;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- FAQ DATA ----------------
faq = {
    "fever": "Fever is a temporary increase in body temperature. Drink fluids and rest. Consult a doctor if it lasts more than 2 days.",
    "headache": "Headaches can occur due to stress or dehydration. Try rest and hydration.",
    "cold": "Common cold symptoms include sneezing and runny nose. Rest and warm fluids help.",
    "covid": "COVID-19 symptoms include fever, cough, and breathing difficulty. Wear a mask and consult a doctor if needed.",
    "diabetes": "Diabetes is a condition affecting blood sugar levels. Regular exercise and a healthy diet help control it.",
    "blood pressure": "High blood pressure can cause heart problems. Reduce salt intake and exercise regularly.",
    "doctor": "You should consult a doctor if symptoms are severe or persist for several days.",
    "emergency": "In case of emergency, please contact your nearest hospital immediately."
}

# ---------------- CHATBOT FUNCTION ----------------
def get_response(user_input):
    user_input = user_input.lower()
    for key in faq:
        if key in user_input:
            return faq[key]
    return "I'm sorry, I can only answer basic health-related questions. Please consult a doctor for accurate advice."

# ---------------- UI ----------------
st.title("🩺 AI Healthcare FAQ Chatbot")
st.write("Ask me basic healthcare questions (This is not medical advice).")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your question here:")

if st.button("Send"):
    if user_input:
        response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# ---------------- DISPLAY CHAT ----------------
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-box'><span class='user'>You:</span> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-box'><span class='bot'>Bot:</span> {message}</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("⚠️ This chatbot provides general information only. Not a substitute for professional medical advice.")
