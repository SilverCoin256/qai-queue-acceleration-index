#!/usr/bin/env python3
"""
Get EOIR annual data from PDF reports
"""

import pdfplumber
import pandas as pd

def extract_eoir_annual():
    """
    Get EOIR annual data from Workload Statistics
    Returns: DataFrame with columns: FY, Pending, Received, Completions, QAI
    """
    # Placeholder - for replication, using extracted data directly
    
    data = {
        'FY': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
        'Pending': [826488, 975977, 1108300, 1391361, 1551975, 1694232, 2105305, 2811648, 3925351, 3723932, 3570145],
        'Received': [228450, 295259, 316132, 547236, 369586, 244262, 707525, 1206103, 1783909, 562372, 238041],
        'Completions': [143478, 163072, 195145, 277076, 232312, 115966, 314814, 526754, 704949, 798014, 402714]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate QAI
    df['QAI'] = df['Pending'].diff() / df['Completions']
    
    return df

if __name__ == "__main__":
    df = extract_eoir_annual()
    df.to_csv('../data/eoir_annual.csv', index=False)
    print("EOIR data saved to data/eoir_annual.csv")
