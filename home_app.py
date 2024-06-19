import streamlit as st

from st_pages import Page, Section, show_pages, hide_pages

# Define the pages and sections
pages = [
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

# Display pages
show_pages(pages)

# Hide specific pages
hide_pages(["Thank you"])

# Display final requirements
st.markdown("### FINAL REQUIREMENTS PRESENTED BY:")
st.header("Marinduque, Kyle of BSIS 3B")

# Display image with caption and source attribution
image_path = "./profile.jpg"
image_caption = "Kyle Marinduque"
image_source = "Photo by Thinkstock on Freeimages.com"

# Display the image
st.image(image_path, caption=image_caption, use_column_width=True)

# Display source attribution
st.markdown(f"*{image_source}*")
