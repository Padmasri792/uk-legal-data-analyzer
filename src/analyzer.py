"""
UK Legal Data Analyzer
Data Analyst Student Project - Teesside University

This module analyzes UK employment tribunal case data using Pandas, NumPy, and Matplotlib.
It provides data cleaning, statistical analysis, and visualization of employment law cases.

Author: Padma Sri
Date: May 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Path for loading data from relative paths
from pathlib import Path


class LegalDataAnalyzer:
    """
    A class to analyze UK employment tribunal case data.
    
    Attributes:
        data (pd.DataFrame): The loaded tribunal case data.
        data_path (str): Path to the CSV data file.
    """
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = None
    
    def load_data(self) -> pd.DataFrame:
        """Load the CSV data file into a pandas DataFrame."""
        print(f"Loading data from {self.data_path}...")
        self.data = pd.read_csv(self.data_path)
        print(f"Successfully loaded {len(self.data)} records.")
        return self.data
    
    def clean_data(self) -> None:
        """Clean and preprocess the data."""
        # Convert decision_date to datetime
        self.data['decision_date'] = pd.to_datetime(self.data['decision_date'])
        
        # Fill missing award amounts with 0
        self.data['award_amount'] = self.data['award_amount'].fillna(0)
        
        # Convert to numeric where needed
        self.data['award_amount'] = pd.to_numeric(self.data['award_amount'], errors='coerce').fillna(0)
        self.data['hearing_days'] = pd.to_numeric(self.data['hearing_days'], errors='coerce').fillna(0)
        
        # Create month column for time-based analysis
        self.data['month'] = self.data['decision_date'].dt.month
        self.data['year'] = self.data['decision_date'].dt.year
        
        # Create outcome category
        self.data['outcome'] = self.data['resolution_type'].apply(
            lambda x: 'Claimant Won' if x in ['Won', 'Settlement', 'Compensation'] else 'Claimant Lost' if x == 'Lost' else 'Other'
        )
        
        print("Data cleaning complete.")
    
    def descriptive_statistics(self) -> None:
        """Print descriptive statistics for the dataset."""
        print("\n" + "="*60)
        print("DESCRIPTIVE STATISTICS")
        print("="*60)
        
        # Total cases
        total = len(self.data)
        print(f"\nTotal Cases Analyzed: {total}")
        
        # Monetary statistics
        total_awards = self.data['award_amount'].sum()
        avg_award = self.data['award_amount'].mean()
        max_award = self.data['award_amount'].max()
        median_award = self.data['award_amount'].median()
        
        print(f"\n--- Award Amount Analysis ---")
        print(f"Total Awards: {total_awards:,.0f}")
        print(f"Average Award: {avg_award:,.2f}")
        print(f"Median Award: {median_award:,.2f}")
        print(f"Maximum Award: {max_award:,.2f}")
        print(f"Min Award: {self.data['award_amount'].min():,.0f}")
        
        # Hearing days statistics
        avg_hearing_days = self.data['hearing_days'].mean()
        max_hearing_days = self.data['hearing_days'].max()
        print(f"\n--- Hearing Duration ---")
        print(f"Average Hearing Days: {avg_hearing_days:.2f}")
        print(f"Maximum Hearing Days: {max_hearing_days}")
        print(f"Total Hearing Days: {self.data['hearing_days'].sum()}")
    
    def analyze_by_claim_type(self) -> pd.DataFrame:
        """Analyze cases grouped by claim type."""
        claim_analysis = self.data.groupby('claim_type').agg({
            'award_amount': ['count', 'sum', 'mean', 'max'],
            'hearing_days': 'mean'
        }).round(2)
        claim_analysis.columns = ['Case Count', 'Total Awards', 'Avg Award', 'Max Award', 'Avg Hearing Days']
        claim_analysis = claim_analysis.sort_values('Total Awards', ascending=False)
        return claim_analysis
    
    def analyze_by_location(self) -> pd.DataFrame:
        """Analyze cases by tribunal location."""
        location_analysis = self.data.groupby('tribunal_location').agg({
            'award_amount': ['count', 'sum', 'mean'],
            'hearing_days': 'mean'
        }).round(0)
        location_analysis.columns = ['Case Count', 'Total Awards', 'Avg Award', 'Avg Hearing Days']
        location_analysis = location_analysis.sort_values('Total Awards', ascending=False)
        return location_analysis
    
    def analyze_by_outcome(self) -> pd.DataFrame:
        """Analyze win/loss rates."""
        outcome_counts = self.data['outcome'].value_counts()
        win_rate = outcome_counts.get('Claimant Won', 0) / len(self.data) * 100
        
        print(f"\n--- Win/Loss Analysis ---")
        print(outcome_counts.to_string())
        print(f"\nClaimant Win Rate: {win_rate:.1f}%")
        return outcome_counts
    
    def analyze_representation_impact(self) -> None:
        """Analyze the impact of legal representation on outcomes."""
        print("\n--- Legal Representation Impact ---")
        
        # Group by represented and outcome
        rep_outcome = pd.crosstab(self.data['represented'], self.data['outcome'], margins=True)
        print("\nRepresentation vs Outcome:")
        print(rep_outcome.to_string())
        
        # Average award with vs without representation
        avg_award_rep = self.data[self.data['represented'] == 'Yes']['award_amount'].mean()
        avg_award_no_rep = self.data[self.data['represented'] == 'No']['award_amount'].mean()
        
        print(f"\nAverage Award (Represented): {avg_award_rep:,.0f}")
        print(f"Average Award (Not Represented): {avg_award_no_rep:,.0f}")
    
    def create_visualizations(self) -> None:
        """Generate and save analysis charts."""
        print("\nGenerating visualizations...")
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        fig = plt.figure(figsize=(16, 12))
        
        # Subplot 1: Cases by Claim Type
        ax1 = fig.add_subplot(2, 3, 1)
        claim_counts = self.data['claim_type'].value_counts()
        claim_counts.plot(kind='bar', ax=ax1, color=plt.cm.Set3(np.linspace(0, 1, len(claim_counts))))
        ax1.set_title('Cases by Claim Type')
        ax1.set_xlabel('Claim Type')
        ax1.set_ylabel('Number of Cases')
        plt.xticks(rotation=45, ha='right')
        
        # Subplot 2: Cases by Location
        ax2 = fig.add_subplot(2, 3, 2)
        loc_counts = self.data['tribunal_location'].value_counts()
        loc_counts.plot(kind='pie', ax=ax2, autopct='%1.0f%%', colors=plt.cm.Set2(np.linspace(0, 1, len(loc_counts))))
        ax2.set_title('Cases by Tribunal Location')
        ax2.set_ylabel('')
        
        # Subplot 3: Win/Loss Distribution
        ax3 = fig.add_subplot(2, 3, 3)
        outcome_colors = ['#2ecc71', '#e74c3c', '#95a5a6']
        self.data['outcome'].value_counts().plot(
            kind='bar', ax=ax3, color=outcome_colors[:len(self.data['outcome'].value_counts())]
        )
        ax3.set_title('Case Outcomes')
        ax3.set_xlabel('Outcome')
        ax3.set_ylabel('Count')
        plt.xticks(rotation=0)
        
        # Subplot 4: Award Amounts by Claim Type
        ax4 = fig.add_subplot(2, 3, 4)
        award_by_claim = self.data.groupby('claim_type')['award_amount'].mean().sort_values()
        ax4.barh(award_by_claim.index, award_by_claim.values, color=plt.cm.Blues(np.linspace(0.3, 0.9, len(award_by_claim))))
        ax4.set_title('Average Award by Claim Type')
        ax4.set_xlabel('Average Award Amount')
        
        # Subplot 5: Representation Impact on Awards
        ax5 = fig.add_subplot(2, 3, 5)
        rep_data = [self.data[self.data['represented']=='Yes']['award_amount'].mean(),
                    self.data[self.data['represented']=='No']['award_amount'].mean()]
        ax5.bar(['Represented', 'Not Represented'], rep_data, color=['#3498db', '#9b59b6'])
        ax5.set_title('Average Award: Representation Impact')
        ax5.set_ylabel('Average Award Amount')
        ax5.grid(axis='y', alpha=0.3)
        
        # Subplot 6: Award Distribution Histogram
        ax6 = fig.add_subplot(2, 3, 6)
        self.data[self.data['award_amount'] > 0]['award_amount'].hist(bins=10, ax=ax6, color='#e67e22', edgecolor='black')
        ax6.set_title('Distribution of Award Amounts')
        ax6.set_xlabel('Award Amount')
        ax6.set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.savefig('output/analysis_charts.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("Charts saved to output/analysis_charts.png")
    
    def generate_report(self, output_file: str) -> None:
        """Generate a summary report as a CSV file."""
        Path("output").mkdir(parents=True, exist_ok=True)
        
        # Create summary statistics dataframe
        summary = pd.DataFrame({
            'Metric': ['Total Cases', 'Total Awards', 'Average Award', 'Median Award', 
                      'Max Award', 'Max Hearing Days', 'Representation Rate'],
            'Value': [
                len(self.data),
                self.data['award_amount'].sum(),
                round(self.data['award_amount'].mean(), 2),
                round(self.data['award_amount'].median(), 2),
                self.data['award_amount'].max(),
                int(self.data['hearing_days'].max()),
                round((self.data['represented'] == 'Yes').sum() / len(self.data) * 100, 1)
            ]
        })
        summary.to_csv(output_file, index=False)
        print(f"Report saved to {output_file}")
        print(f"\nFull analysis report:")
        print(summary.to_string())
    
    def run_full_analysis(self) -> None:
        """Run the complete analysis pipeline."""
        print("\n" + "#"*60)
        print("# UK LEGAL DATA ANALYZER - Student Project")
        print("# Data Analyst @ Teesside University")
        print("#"*60)
        
        self.load_data()
        self.clean_data()
        self.descriptive_statistics()
        
        print("\n" + "="*60)
        print("ANALYSIS BY CLAIM TYPE")
        print("="*60)
        print(self.analyze_by_claim_type().to_string())
        
        print("\n" + "="*60)
        print("ANALYSIS BY LOCATION")
        print("="*60)
        print(self.analyze_by_location().to_string())
        
        self.analyze_by_outcome()
        self.analyze_representation_impact()
        self.generate_report("output/analysis_summary.csv")
        self.create_visualizations()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETE")
        print("="*60)


if __name__ == "__main__":
    # Initialize analyzer
    data_file = Path(__file__).parent.parent / "data" / "case_data.csv"
    analyzer = LegalDataAnalyzer(str(data_file))
    
    # Run full analysis pipeline
    analyzer.run_full_analysis()
