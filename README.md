# GEO Assignment Submission

## Overview

This project contains solutions for both parts of the assessment:

### Part 1
GEO (Generative Engine Optimization) Product Strategy & Monetization Roadmap Presentation.

### Part 2
TruthLayer — AI-powered Fact-Checking Web Application.

The application extracts factual claims from uploaded PDF documents, verifies them using live web search, and flags claims as:
- VERIFIED
- INACCURATE
- FALSE
- OUTDATED

---

# Part 1: GEO Product Strategy

## Features
- GEO analytics concept
- AI search visibility tracking
- Competitor comparison
- Monetization roadmap
- Short-term and long-term strategy
- Automatic PPT generation using Python

## PPT Generator

Run:

```bash
python create_ppt.py
Generated file:

GEO_Product_Strategy.pptx
Part 2: TruthLayer Fact-Checking Agent
Features
PDF Upload
Claim Extraction using OpenAI
Live Web Verification using Tavily Search
AI-based Fact Validation
Streamlit Frontend
Deployment Ready
Tech Stack
Frontend
Streamlit
Backend
Python
AI Models
OpenAI GPT-4.1 Mini
Web Search
Tavily API
PDF Parsing
pdfplumber
Project Structure
Assignment/
│
├── app.py
├── create_ppt.py
├── requirements.txt
├── .gitignore
├── README.md
├── GEO_Product_Strategy.pptx
└── .env
Installation
Clone Repository
git clone <your-repository-url>
Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
Run Locally
python -m streamlit run app.py

App runs at:

http://localhost:8501
Streamlit Cloud Deployment

For deployment:

Push project to GitHub
Connect repository to Streamlit Cloud
Add secrets in Streamlit Cloud:
OPENAI_API_KEY="your_openai_key"
TAVILY_API_KEY="your_tavily_key"
Deploy app
Evaluation Workflow
Upload PDF
Extract claims
Search live web
Verify claims
Generate verdicts with evidence
Example Verdicts
VERIFIED
FALSE
OUTDATED
INACCURATE
Future Improvements
Multi-agent verification pipeline
Citation confidence scoring
OCR support for scanned PDFs
Source ranking system
Exportable verification reports
Batch document processing
Deployment Link
https://assessmentappuctmanager-u7m6unps4imlwnzy2prvm3.streamlit.app/
GitHub Repository
https://github.com/majordevbhargav/Assessment_Product_Manager/
Demo Video
https://drive.google.com/file/d/1qHEp7_xFB5z3MkxSDIQLyMiOizACGrtQ/view?usp=sharing
Author
Dev Bhargav
