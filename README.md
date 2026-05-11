# UK Legal Data Analyzer

> A Python-based data analysis project that examines UK employment tribunal case data to identify patterns in case outcomes, award amounts, and the impact of legal representation.

**Student Project** | Data Analyst Programme, Teesside University | May 2026

---

## Overview

This project analyzes a sample dataset of 20 UK employment tribunal cases using Pandas, NumPy, and Matplotlib. It demonstrates core data analysis skills including data cleaning, statistical analysis, visualization, and reporting.

## What This Project Does

- Cleans and preprocesses tribunal case data
- Calculates descriptive statistics for award amounts and hearing durations
- Analyzes cases by claim type, location, and outcome
- Measures the impact of legal representation on case results
- Generates publication-ready charts
- Exports summary reports

---

## Project Structure

```
uk-legal-data-analyzer/
&#127907; data/
   &#127907; case_data.csv         # Sample UK tribunal case data (20 records)
&#127907; src/
   &#127907; analyzer.py           # Main analysis module with LegalDataAnalyzer class
&#127907; output/                  # Generated reports and charts (created on run)
   &#127907; analysis_charts.png   # 6-panel visualization grid
   &#127907; analysis_summary.csv  # Statistical summary report
&#127907; requirements.txt        # Python dependencies
&#127907; README.md
```

---

## Dataset

The dataset contains 20 sample employment tribunal cases with the following columns:

| Column | Description |
|---|---|
| `case_id` | Unique case identifier (UKET format) |
| `claimant_name` | Name of person making the claim |
| `respondent_name` | Employer or organization being sued |
| `legal_area` | Area of law (all Employment) |
| `claim_type` | Type of claim (e.g., Unfair Dismissal, Discrimination) |
| `resolution_type` | How the case was resolved |
| `decision_date` | Date of tribunal decision |
| `award_amount` | Monetary award (0 if claim lost) |
| `hearing_days` | Number of days the hearing lasted |
| `represented` | Whether claimant had legal representation |
| `tribunal_location` | Location of the employment tribunal |

---

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup

```bash
# Clone the repository
git clone https://github.com/Padmasri792/uk-legal-data-analyzer.git

# Navigate to project
cd uk-legal-data-analyzer

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Run Full Analysis

```bash
cd src
python analyzer.py
```

This will:
1. Load and clean the data
2. Print descriptive statistics
3. Analyze cases by type, location, and outcome
4. Generate charts and save to `output/`
5. Export a summary report CSV

### Use in Your Own Code

```python
from src.analyzer import LegalDataAnalyzer

# Initialize and run
analyzer = LegalDataAnalyzer('data/case_data.csv')
analyzer.run_full_analysis()
```

### Individual Methods

```python
# Load data
analyzer.load_data()

# Clean data
analyzer.clean_data()

# Get statistics
analyzer.descriptive_statistics()

# Analyze by category
analyzer.analyze_by_claim_type()
analyzer.analyze_by_location()
analyzer.analyze_by_outcome()
analyzer.analyze_representation_impact()

# Visualize
analyzer.create_visualizations()

# Export report
analyzer.generate_report('output/my_report.csv')
```

---

## Key Findings (From Sample Data)

| Metric | Value |
|---|---|
| **Total Cases** | 20 |
| **Claimant Win Rate** | 85% |
| **Average Award** | 14,535 |
| **Median Award** | 10,500 |
| **Highest Award** | 45,000 |
| **Avg Hearing (Rep)** | 3.8 days |
| **Avg Hearing (No Rep)** | 1.5 days |

### Notable Insights

- **Representation matters**: Represented claimants receive significantly higher average awards
- **Discrimination claims** have the highest average award amounts
- **London tribunals** handle the largest volume of cases
- **Settlements and Compensation** are the most common resolution types

---

## Technologies Used

| Category | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **File I/O** | CSV handling |
| **Standard Lib** | pathlib, datetime |

---

## Skills Demonstrated

- Data cleaning and preprocessing
- Descriptive and inferential statistics
- Group-by analysis and aggregation
- Data visualization (bar charts, pie charts, histograms)
- Object-oriented programming (OOP) in Python
- Report generation and export

---

## Future Improvements

- Add interactive dashboards using Plotly
- Implement machine learning for outcome prediction
- Expand to a larger real tribunal dataset
- Add Jupyter notebook with exploratory analysis
- Create a Streamlit web app for interactive exploration

---

## License

MIT License - feel free to use this code for learning purposes.

---

## Author

**Padma Sri**  
Data Analyst Student, Teesside University  

&#128231; Email: padmasri@example.com  
&#128279; GitHub: [@Padmasri792](https://github.com/Padmasri792)  
&#128279; LinkedIn: [linkedin.com/in/padmasri](https://linkedin.com/in/padmasri)

---

&#169; 2026 Padma Sri. All Rights Reserved.
