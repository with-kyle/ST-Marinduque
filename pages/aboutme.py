import streamlit as st
from PIL import Image
import os

# Profile Page
st.set_page_config(layout="wide", page_title="About Me")

# Add a header with your full name
st.title('Kyle Marinduque')

# Display your picture
profile_image_path = 'profile.jpg'  # Ensure this path is correct
if os.path.exists(profile_image_path):
    profile_image = Image.open(profile_image_path)
    st.image(profile_image, width=600)
else:
    st.error(f"File not found: {profile_image_path}")

# Add your personal information
st.subheader('Personal Information')
info_columns = st.columns([1, 3])
with info_columns[0]:
    st.write("**Address:** Sitio Cabug Baybay Silay City Negros Occidental")
    st.write("**Birthdate:** February 15, 2002")
    st.write("**Age:** 22 Years Old")
with info_columns[1]:
    st.write("**Gender:** Male")
    st.write("**Religion:** Catholic")
    st.write("**Occupation:** Student")

# Contact Information
st.subheader('Contact Information')
st.write("**Email:** kylemarinduque@gmail.com")
st.write("**Phone:** 09456698047")
st.write("**Facebook:** [Kyle Marinduque](https://www.facebook.com/kylemarinduque)")
st.write("**Instagram:** [@kyleishiii](https://www.instagram.com/kyleishiii)")

# Image Gallery
st.subheader('Gallery')
st.write("Here are some pictures of myself:")

# Define image paths
image_paths = ['picture1.jpg', 'picture2.jpg', 'picture3.jpg']   

# Display images in a vertically stacked layout
for image_path in image_paths:
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, width=400, caption=os.path.basename(image_path))
    else:
        st.error(f"File not found: {image_path}")

# Background (Left-aligned)
st.subheader('Background')
st.markdown('''
The world of anime has captivated me since I was young. From the vibrant colors and fantastical stories to the complex characters and emotional journeys, anime offers a unique and immersive experience. I find myself drawn to the diverse genres, from thrilling action adventures to heartwarming slice-of-life stories. Each series offers a chance to explore new worlds, cultures, and perspectives. Whether it's the epic battles in shounen anime or the introspective narratives of seinen, there's always something new to discover. It's more than just a hobby; it's a passion that fuels my creativity and imagination.

There's nothing quite like the feeling of getting out and exploring the world. Whether it's a hike through a scenic nature trail, a stroll through a bustling city park, or a day trip to a nearby town, I love the sense of adventure that outings bring. I enjoy discovering hidden gems in my own city or venturing further afield to experience new places and cultures. Every outing offers an opportunity to learn something new, whether it's about local history, hidden cafes, or simply appreciating the beauty of nature. It's a chance to disconnect from the everyday routine and reconnect with myself and the world around me.
''')

# Footer
st.write("by koalatech...")
