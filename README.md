# AI-Powered Resume Screening & Job Matching System

## Project Overview

This project is an AI-powered recruitment solution that automatically analyzes resumes and compares them with job descriptions. The system extracts skills from uploaded PDF resumes, identifies matching and missing skills, calculates semantic similarity using NLP techniques, and generates a final match score with candidate recommendations.

## Features

* Upload Resume in PDF Format
* Resume Text Extraction using PyPDF2
* Skill Extraction and Matching
* Missing Skill Detection
* Skill Match Percentage Calculation
* TF-IDF Vectorization
* Cosine Similarity Scoring
* Final Match Score Generation
* Candidate Recommendation System
* Interactive Streamlit User Interface

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* PyPDF2
* NLP
* TF-IDF
* Cosine Similarity

## Project Workflow

1. Upload Resume PDF
2. Extract Resume Text
3. Extract Skills from Resume and Job Description
4. Identify Matched and Missing Skills
5. Calculate Skill Match Percentage
6. Compute Resume-JD Similarity Score
7. Generate Final Match Score
8. Display Candidate Recommendation

## Installation

Install the required dependencies:

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## Sample Output

* Skills Found in Resume
* Skills Required in Job Description
* Matched Skills
* Missing Skills
* Skill Match Percentage
* Resume-JD Similarity Score
* Final Match Score
* Candidate Recommendation

## Use Cases

* Resume Screening
* Applicant Tracking Systems (ATS)
* HR Tech Solutions
* Recruitment Automation
* AI/ML Portfolio Projects

## Future Enhancements

* Multiple Resume Ranking
* Candidate Name Extraction
* Email and Phone Extraction
* Resume Database Integration
* Advanced NLP Models

## Author

Likhitha
