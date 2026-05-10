import streamlit as st
import pdfplumber
import requests
from openai import OpenAI

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

# OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Streamlit page config
st.set_page_config(page_title="TruthLayer", layout="wide")

# Title
st.title("🛡️ TruthLayer - AI Fact Checker")
st.write("Upload a PDF and verify claims using live web data.")

# -------------------------------
# Extract text from PDF
# -------------------------------

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# -------------------------------
# Extract claims using OpenAI
# -------------------------------

def extract_claims(text):

    prompt = f"""
    Extract important factual claims from the following text.

    Focus on:
    - statistics
    - percentages
    - dates
    - financial numbers
    - technical claims

    Return short bullet points only.

    Text:
    {text[:6000]}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You extract factual claims from documents."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    claims_text = response.choices[0].message.content

    claims = claims_text.split("\n")

    cleaned_claims = []

    for claim in claims:
        claim = claim.strip("- ").strip()

        if claim:
            cleaned_claims.append(claim)

    return cleaned_claims


# -------------------------------
# Search web using Tavily
# -------------------------------

def search_web(query):

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 3
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:

        data = response.json()

        results = data.get("results", [])

        combined_text = ""
        links = []

        for result in results:

            combined_text += result.get("content", "") + "\n"

            links.append(result.get("url", ""))

        return combined_text, links

    return "", []


# -------------------------------
# Verify claim
# -------------------------------

def verify_claim(claim, web_data):

    prompt = f"""
    Claim:
    {claim}

    Web Data:
    {web_data}

    Decide whether the claim is:

    VERIFIED
    INACCURATE
    FALSE
    OUTDATED

    Return in this format:

    Verdict:
    Correct Fact:
    Explanation:
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional fact checking AI."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# Upload PDF
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# -------------------------------
# Main workflow
# -------------------------------

if uploaded_file:

    with st.spinner("Extracting PDF text..."):

        text = extract_text(uploaded_file)

    st.success("PDF uploaded successfully!")

    if st.button("Start Fact Check"):

        # Extract claims
        with st.spinner("Extracting factual claims..."):

            claims = extract_claims(text)

        st.subheader("📌 Detected Claims")

        for i, claim in enumerate(claims):
            st.write(f"{i+1}. {claim}")

        st.divider()

        st.subheader("🔍 Verification Results")

        # Verify claims
        for claim in claims:

            with st.spinner(f"Checking: {claim}"):

                web_data, links = search_web(claim)

                result = verify_claim(claim, web_data)

            st.markdown("---")

            st.markdown("### Claim")
            st.write(claim)

            st.markdown("### Result")
            st.text(result)

            st.markdown("### Sources")

            if links:

                for link in links:
                    st.write(link)

            else:
                st.write("No sources found.")
