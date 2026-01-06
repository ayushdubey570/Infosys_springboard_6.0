# AI-Based Knowledge Graph Builder for Enterprise Intelligence
## Module 1: Data Ingestion & Normalization

### 📋 Project Overview
This project aims to build a "Company Brain" by transforming disconnected enterprise data (emails, support tickets, and databases) into a structured **Knowledge Graph**. 

This specific module handles the **Normalization and Cleaning** of the Customer Support Ticket dataset. By cleaning the data now, we ensure that our AI models can accurately identify entities (people, products, issues) and their relationships without being distracted by "noise" or inconsistent formatting.

---

### 🏗️ The Data Pipeline
The normalization process follows these logical steps:
1. **Load**: Reading raw CSV data from Kaggle sources.
2. **Standardize**: Converting column headers to a programmer-friendly format.
3. **Impute**: Filling in missing descriptions to prevent pipeline crashes.
4. **Map**: Collapsing multiple status types (Pending, Open, Resolved) into binary categories.
5. **Sanitize**: Using Regular Expressions (Regex) to remove special characters and symbols.



---

### 🛠️ Environment Setup

#### 1. Prerequisites
- Python 3.8 or higher installed.
- The `customer_support_data.csv` file located in the root directory.

#### 2. Required Libraries
Install the necessary data processing library using pip:
```bash
pip install pandas
```

#### 3. Run Script
- Open your terminal or command prompt in the project folder.
_ Run the script:
```bash
python normalize_tickets.py
```
- Look for the file cleaned_support_tickets.csv in your folder.

### 🧠 Key Terminology

*   **Normalization:** Making different data points look the same (e.g., merging "Resolved" and "Closed").
    
*   **Regex (Regular Expressions):** A powerful tool used to find and replace patterns in text.
    
*   **Data Ingestion:** The first step of a pipeline where data is brought into the system.
    
*   **Entity Resolution:** The future step where we ensure "Laptop" and "laptop" refer to the same object in our Graph.
