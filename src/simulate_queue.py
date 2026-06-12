#!/usr/bin/env python3
"""
Queue simulation for pressure-failure relationship
"""

import numpy as np
import pandas as pd

def simulate_queue(lambda_base, mu, c, initial_backlog, pressure_levels, failure_threshold=2.0):
    """
    Simulate queue dynamics under different pressure levels
    
    Parameters:
    - lambda_base: base arrival rate per month
    - mu: service rate per adjudicator per month
    - c: number of adjudicators
    - initial_backlog: initial backlog
    - pressure_levels: list of pressure multipliers
    - failure_threshold: multiplier of initial backlog to define failure
    
    Returns: DataFrame with pressure level and months to failure
    """
    results = []
    
    for p in pressure_levels:
        lambda_p = lambda_base * p
        backlog = initial_backlog
        month = 0
        failure_target = initial_backlog * failure_threshold
        
        while backlog < failure_target and month < 200:  # Safety limit
            backlog = backlog + lambda_p - (c * mu)
            month += 1
            
            if backlog < 0:  # System shrinks, never reaches failure
                month = float('inf')
                break
        
        results.append({
            'pressure_increase': int((p - 1) * 100),
            'months_to_failure': month
        })
    
    return pd.DataFrame(results)

if __name__ == "__main__":
    # USCIS parameters
    lambda_base = 464604  # arrivals per month
    mu = 68.4  # completions per adjudicator per month
    c = 5000  # adjudicators
    initial_backlog = 6578102
    
    pressure_levels = [1.0, 1.1, 1.25, 1.5, 2.0]
    
    df = simulate_queue(lambda_base, mu, c, initial_backlog, pressure_levels)
    df.to_csv('../data/simulation_results.csv', index=False)
    print("Simulation results saved to data/simulation_results.csv")
    print(df)
