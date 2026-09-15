# GEO Strategy & TruthLayer

An assessment project combining a GEO product strategy and monetization proposal with **TruthLayer**, an AI-assisted fact-checking application for PDF documents.

## Project Overview

The repository contains two connected assessment deliverables:

1. **GEO Product Strategy**: a product strategy, analytics, and monetization roadmap for Generative Engine Optimization.
2. **TruthLayer**: a Streamlit application that extracts factual claims from uploaded PDFs, verifies them using live web search, and produces evidence-backed verdicts.

## TruthLayer Features

- PDF upload and parsing
- AI-assisted claim extraction
- Live web verification through Tavily
- Claim classification as verified, inaccurate, false, or outdated
- Evidence-oriented verification workflow
- Streamlit interface

## GEO Strategy Features

- GEO analytics concept
- AI search visibility tracking
- Competitor comparison
- Monetization roadmap
- Short- and long-term product strategy
- Automated presentation generation

## Tech Stack

- Python
- Streamlit
- OpenAI API
- Tavily Search API
- pdfplumber
- python-pptx

## Project Structure

```text
Assignment/
├── app.py
├── create_ppt.py
├── requirements.txt
├── .gitignore
├── README.md
└── GEO_Product_Strategy.pptx
```

## Local Setup

```bash
git clone https://github.com/majordevbhargav/Assessment_Product_Manager.git
cd Assessment_Product_Manager
pip install -r requirements.txt
```

Create a local `.env` file or configure the required secrets through your deployment platform:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Run the fact-checking application:

```bash
python -m streamlit run app.py
```

Generate the presentation:

```bash
python create_ppt.py
```

## Verification Workflow

```text
PDF
 ↓
Claim Extraction
 ↓
Web Search
 ↓
Evidence Collection
 ↓
AI Validation
 ↓
Verdict + Evidence
```

## Limitations

Fact-checking results depend on the quality and availability of external sources and model interpretation. Results should be reviewed by a human before being treated as authoritative.

## Author

**Dev Bhargav**

- GitHub: https://github.com/majordevbhargav
- LinkedIn: https://www.linkedin.com/in/devbhargav100
