import streamlit as st

# Set the title of the web app
st.title("Simple User Form")

# Create input fields
name = st.text_input("Name:")
email = st.text_input("Email:")

# Create the submit button
if st.button("Submit"):
    # Basic validation
    if name == "" or email == "":
        st.warning("Please fill in all fields!")
    else:
        # Success message
        st.success(f"Form Submitted!\n\nName: {name}\nEmail: {email}")