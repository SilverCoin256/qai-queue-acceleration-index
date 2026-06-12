#!/usr/bin/env python3
"""
Calculate QAI and run statistical tests
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import adfuller, grangercausalitytests

def compute_qai(df):
    """Calculate QAI from pending and completions"""
    df['QAI'] = df['Pending'].diff() / df['Completions']
    return df

def granger_test(data, maxlag=2):
    """Run Granger causality test"""
    # data should be DataFrame with columns: backlog_growth, QAI
    result = grangercausalitytests(data, maxlag=maxlag, verbose=False)
    return result

def adf_test(series):
    """Augmented Dickey-Fuller test"""
    result = adfuller(series, autolag='AIC')
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Critical Values': result[4]
    }

if __name__ == "__main__":
    # Load data
    eoir = pd.read_csv('../data/eoir_annual.csv')
    uscis = pd.read_csv('../data/uscis_quarterly.csv')
    
    # Calculate QAI
    eoir = compute_qai(eoir)
    uscis = compute_qai(uscis)
    
    # Run statistical tests
    print("EOIR ADF Test (Backlog):")
    print(adf_test(eoir['Pending']))
    
    print("\nEOIR ADF Test (QAI):")
    print(adf_test(eoir['QAI'].dropna()))
    
    print("\nEOIR Granger Causality Test:")
    # Prepare data for Granger test
    eoir['backlog_growth'] = eoir['Pending'].diff()
    test_data = eoir[['backlog_growth', 'QAI']].dropna()
    print(granger_test(test_data, maxlag=2)[1][1]['ssr_fttest'])
