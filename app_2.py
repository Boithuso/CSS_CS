import streamlit as st
import pandas as pd
import plotly.express as px

##Building a researcher profile page
# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Boithuso Phale"
field = "Immunogenomics"
institution = "University of the Witwatersrand"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")



choice = st.selectbox("Have you heard of Immunogenomics before", ["Yes", "No"])

if choice == "No":
    st.write(f"{field} is (insert brief description of field)")
    st.write(f"Was this an informative description of the field of {field}?")
    st.feedback("stars")
else:
        st.write(f"Super cool stuff right?")



# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "2451444@students.wits.ac.za"
st.write(f"You can reach {name} at {email}.")
