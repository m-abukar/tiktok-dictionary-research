# TikTok Dictionary - Reddit Data Collection Research

Academic research project for Computer Science dissertation at University of Warwick.

## Project Overview

This repository contains the data collection component for researching emerging slang terminology popularized on TikTok. The system monitors Reddit discussions to identify and analyze new slang terms for linguistic research and educational purposes.

## Purpose

Analyzing how Gen Z slang evolves and spreads across social media platforms by:
- Identifying trending terminology from Reddit discussions where users ask "what does X mean?"
- Extracting linguistic context and usage patterns
- Building a machine learning model to classify and predict potential slang terms
- Creating a free educational resource documenting TikTok-specific terminology for public benefit

## Reddit API Usage

### Data Collection Scope
- **Subreddits monitored**: r/TikTokCringe, r/OutOfTheLoop, r/GenZ, r/NoStupidQuestions, r/explainlikeimfive
- **Data collected**: Post titles and text containing slang terminology questions
- **Frequency**: 3 times per week (Monday/Wednesday/Friday mornings)
- **Rate limit**: 40 requests per minute (within Reddit's 60/min allowance)
- **Privacy**: No user data, comments, votes, or personal information collected

### What We DON'T Do
- No posting or commenting
- No voting or user interaction  
- No personal data collection
- No real-time monitoring
- No storage of individual user information

### What We DO
- Read public posts containing slang terminology questions
- Extract aggregate statistics on term frequency
- Cross-validate findings across multiple subreddits
- Integrate with Google Trends for additional validation

## Research Methodology

### 1. Term Extraction
Identify posts matching patterns: "what does [X] mean?", "can someone explain [term]?"

### 2. Frequency Analysis
Track mention counts across subreddits to identify emerging terminology

### 3. Machine Learning Classification
Train model on existing slang terms to predict new ones

### 4. Cross-Platform Validation
Verify findings with Google Trends data

## Technical Stack

- **Language**: Python 3.10+
- **Reddit API**: PRAW (Python Reddit API Wrapper)
- **Machine Learning**: scikit-learn, NLTK
- **Backend**: Django REST Framework
- **Database**: PostgreSQL

## Privacy & Ethics

- Only public post data collected
- No user profiling or tracking
- Aggregated statistics only
- Fully GDPR compliant
- Research methodology publicly documented

## Academic Affiliation

- **Institution**: University of Warwick, Computer Science Department
- **Project**: CS310 Individual Project (Dissertation)
- **Academic Year**: 2025-2026

## Main Application

The full TikTok Dictionary platform (web application, complete ML pipeline, user interface) is maintained in a private repository for dissertation purposes.

---

*This repository contains only the Reddit data collection component for research transparency.*
