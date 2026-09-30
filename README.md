# 🎓 AI-Powered Startup Idea Validation Platform

An interactive Streamlit-based platform developed to validate a startup idea using primary research, secondary research, market sizing, competitor analysis, financial feasibility and an AI-based recommendation engine.

---

## 🚀 Project Overview

The startup idea developed for this project is:

**AI-Powered Career & Skill Recommendation Platform for College Students**

The platform aims to help college students identify suitable career paths and skill-development opportunities based on their education, interests, current skills and career goals.

The startup idea is evaluated across four major validation dimensions:

- 📈 Market Demand
- 👥 Customer Demand
- 🏢 Competition
- 💰 Financial Feasibility

---

## 🎯 Project Objectives

The main objectives of the project are:

1. Identify the market potential of the startup idea.
2. Understand customer interest through primary research.
3. Analyze existing competitors.
4. Estimate TAM, SAM and SOM.
5. Evaluate financial feasibility.
6. Study Google Trends related to the market.
7. Develop an AI-based career recommendation engine.
8. Combine the findings into an overall startup validation score.

---

## 📊 Validation Framework

The platform uses four validation factors.

| Factor | Score | Weight |
|---|---:|---:|
| Market Demand | 85/100 | 25% |
| Customer Demand | 65/100 | 30% |
| Competition | 60/100 | 20% |
| Financial Feasibility | 75/100 | 25% |

### Overall Validation Score

**71.5 / 100**

The score is a project-based analytical indicator using research findings and stated assumptions.

---

## 👥 Primary Research

A Google Forms questionnaire was conducted to understand students' career guidance and skill-development needs.

### Survey Sample

**20 student responses**

The questionnaire covered:

- Career confusion
- Career-choice confidence
- Career challenges
- Current sources of guidance
- Interest in AI career recommendations
- Personalized recommendations
- Trust in AI
- Desired recommendations
- Usage frequency
- Willingness to pay
- Preferred pricing
- Recommendation intention

### Customer Demand Finding

For the question:

> Would you use an AI platform that recommends career paths based on your profile?

Responses were:

- Definitely — 2
- Probably — 11
- Maybe — 6
- No — 1

Therefore:

**Definitely + Probably = 13/20 = 65%**

This produces the Customer Demand score of:

**65/100**

---

## 📈 Market Research

Google Trends research was conducted for relevant search terms.

The project examined:

- Career Guidance
- Skill Development
- Career Assessment
- AI Career
- Career Counselling

The research was used as secondary market evidence for the startup validation process.

---

## 🌍 TAM / SAM / SOM Analysis

The project uses the following market-sizing assumptions:

### TAM — Total Addressable Market

**4.46 Crore students**

### SAM — Serviceable Available Market

**89.2 Lakh students**

Based on 20% of TAM.

### SOM — Serviceable Obtainable Market

**89,200 students**

Based on 1% of SAM.

### Illustrative Pricing

Premium subscription:

**₹99/month**

The platform also displays illustrative revenue opportunities based on these assumptions.

> Note: TAM, SAM and SOM figures are project assumptions used for academic market-sizing analysis.

---

## 🏢 Competitor Analysis

The platform compares the proposed startup with existing career guidance platforms.

Competitors analyzed include:

- CareerGuide
- Edumilestones
- Mindler

The comparison considers:

- Career assessment
- Career guidance
- AI features
- Target users
- Indicative pricing

### Proposed Platform Focus

The proposed platform focuses on:

- College students
- Personalized career recommendations
- AI-based skill recommendations
- Course recommendations
- Certification recommendations
- Internship and job recommendations
- Affordable premium subscription

---

## 💰 Financial Feasibility

The project uses an illustrative financial model.

### Assumptions

| Item | Value |
|---|---:|
| Free Plan | ₹0 |
| Premium Plan | ₹99/month |
| Paid Users | 100/month |
| Monthly Revenue | ₹9,900 |
| Monthly Operating Cost | ₹5,000 |
| Monthly Profit | ₹4,900 |
| Profit Margin | 49.5% |

### Annual Estimate

Annual Revenue:

**₹1,18,800**

Annual Profit:

**₹58,800**

> These are project assumptions for financial feasibility analysis and are not actual business results.

---

## 🤖 AI Career Recommendation Engine

The platform includes a rule-based recommendation engine.

Users can enter:

- 🎓 Degree / Education
- ❤️ Areas of Interest
- 🛠️ Current Skills
- 🎯 Career Goal

The system generates:

### Career Recommendations

Examples:

- Data Analyst
- Business Analyst
- BI Analyst
- Financial Analyst
- HR Analyst
- Digital Marketing Analyst
- Software Developer
- Product Analyst
- Entrepreneur

### Skill Recommendations

Examples:

- Advanced Excel
- SQL
- Power BI
- Python
- Financial Modelling
- Digital Marketing
- HR Analytics
- Communication
- Problem Solving

The recommendations are generated based on the user's selected profile inputs.

---

## 📊 Streamlit Dashboard

The application contains eight main sections:

### 🏠 Home

Provides the overall startup validation dashboard.

### 📋 Research Data

Displays:

- Survey response count
- AI platform interest
- Personalized recommendation interest
- Career challenges
- Survey data

### 📊 Market Size

Displays:

- TAM
- SAM
- SOM
- Market-size chart
- Illustrative revenue opportunity

### 🏢 Competitor Analysis

Displays:

- Competitor comparison
- Pricing comparison
- Market positioning
- Platform differentiation

### 💰 Financial Feasibility

Displays:

- Revenue
- Operating cost
- Profit
- Profit margin
- Annual estimates

### 📈 Google Trends

Displays:

- Search terms
- Interest values
- Growth observations
- Market-demand research

### 🤖 AI Recommendation

Provides personalized career and skill recommendations.

### 🚀 Validate Idea

Combines all four validation dimensions and displays the final startup validation score.

---

## 🛠️ Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- Google Forms
- Google Trends
- CSV Dataset

---

## 📁 Project Structure

```text
AI_CAREER_VALIDATOR/
│
├── app.py
├── survey_responses.csv
└── README.md
