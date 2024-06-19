import streamlit as st
from st_pages import Page, Section, show_pages, hide_pages

show_pages(
    [
        Page("home_app.py", "ITEQMT Machine Learning Application Portfolio", "👨‍💻"),
        Section("Main Page", "📢"),
        Page("pages/aboutme.py", "ABOUT ME", "1️⃣", in_section=True),
        Page("pages/description_app.py", "Streamlit Features Description", "2️⃣", in_section=True),
        Page("pages/mylearnings.py", "What I Have Learned", "3️⃣", in_section=True),

        Section("Sample Projects", "📂"),
        Page("pages/sentiment_app.py", "Basic Sentiment Analyzer", "1️⃣", in_section=True),
        Page("pages/classifier_app.py", "Weapon Classification", "2️⃣", in_section=True),
        Page("pages/prediction_app.py", "Prediction", "3️⃣", in_section=True),

        Section("Project Source Code", "💻"),
        Page("pages/sentiment_code.py", "Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/classifier_code.py", "Image Classification SRC", "2️⃣", in_section=True),
        Page("pages/prediction_code.py", "Prediction SRC", "3️⃣", in_section=True),
    ]
)
hide_pages(["Thank you"])

st.markdown("### FINAL REQUIREMENTS PRESENTED BY: ")
st.header("Marinduque, Kyle of BSIS 3B")
st.image("./profile.JPG")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)
