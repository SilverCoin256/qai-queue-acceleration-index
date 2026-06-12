#!/usr/bin/env python3
"""
Make figures for QAI paper submission to AAAI Student Abstract
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Set up style for publication
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9

# ============================================================================
# FIGURE 1: EOIR QAI Time Series (FY2016–FY2026)
# ============================================================================

# EOIR data from submission package
years = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])
qai_eoir = np.array([np.nan, 0.917, 0.678, 1.022, 0.691, 1.227, 1.306, 1.341, 1.580, -0.252, -0.382])

fig, ax = plt.subplots(figsize=(10, 4))

# Plot QAI line
ax.plot(years[1:], qai_eoir[1:], 'o-', linewidth=2, markersize=6, color='#2c3e50', label='QAI')

# Add threshold lines
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 0 (stable)')
ax.axhline(y=0.5, color='orange', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 0.5 (degrading)')
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 1.0 (explosive)')

# Highlight explosive regime
ax.axvspan(2018.5, 2024.5, alpha=0.1, color='red', label='Explosive regime (QAI > 1.0)')

# Highlight recovery
ax.axvspan(2024.5, 2026.5, alpha=0.1, color='green', label='Recovery (QAI < 0)')

# Labels and title
ax.set_xlabel('Fiscal Year', fontweight='bold')
ax.set_ylabel('QAI', fontweight='bold')
ax.set_title('EOIR Immigration Courts: Queue Acceleration Index (FY2016–FY2026)', fontweight='bold', fontsize=12)

# Set x-axis to show all years
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, ha='right')

# Set y-axis range
ax.set_ylim(-0.5, 1.8)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)

# Tight layout
plt.tight_layout()

# Save
plt.savefig('../paper/figures/figure1_eoir_qai_timeseries.png', dpi=300, bbox_inches='tight')
plt.savefig('../paper/figures/figure1_eoir_qai_timeseries.pdf', bbox_inches='tight')
plt.close()

print("Figure 1 saved: EOIR QAI time series")

# ============================================================================
# FIGURE 2: USCIS QAI Time Series (FY2019Q1–FY2021Q4)
# ============================================================================

# USCIS quarterly data
quarters = ['FY19Q1', 'FY19Q2', 'FY19Q3', 'FY19Q4', 
            'FY20Q1', 'FY20Q2', 'FY20Q3', 'FY20Q4',
            'FY21Q1', 'FY21Q2', 'FY21Q3', 'FY21Q4']
qai_uscis = np.array([np.nan, 0.007, 0.018, 0.017, 0.017, 0.017, 0.017, 0.017, 0.017, 0.018, 0.018, 0.018])

fig, ax = plt.subplots(figsize=(10, 4))

# Plot QAI line
ax.plot(range(len(quarters))[1:], qai_uscis[1:], 'o-', linewidth=2, markersize=6, color='#2c3e50')

# Add threshold lines
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 0')
ax.axhline(y=0.5, color='orange', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 0.5')
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=1, alpha=0.7, label='QAI = 1.0')

# Labels and title
ax.set_xlabel('Quarter', fontweight='bold')
ax.set_ylabel('QAI', fontweight='bold')
ax.set_title('USCIS: Queue Acceleration Index (FY2019Q1–FY2021Q4)', fontweight='bold', fontsize=12)

# Set x-axis
ax.set_xticks(range(len(quarters)))
ax.set_xticklabels(quarters, rotation=45, ha='right')

# Set y-axis range
ax.set_ylim(-0.1, 0.3)

# Grid
ax.grid(True, alpha=0.3)

# Legend
ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)

# Tight layout
plt.tight_layout()

# Save
plt.savefig('../paper/figures/figure2_uscis_qai_timeseries.png', dpi=300, bbox_inches='tight')
plt.savefig('../paper/figures/figure2_uscis_qai_timeseries.pdf', bbox_inches='tight')
plt.close()

print("Figure 2 saved: USCIS QAI time series")

# ============================================================================
# FIGURE 3: Pressure-Failure Curve (Nonlinear Degradation)
# ============================================================================

# Simulation data
pressure_increase = np.array([0, 10, 25, 50, 100])
months_to_failure = np.array([54, 39, 28, 19, 12])

fig, ax = plt.subplots(figsize=(8, 5))

# Plot the curve
ax.plot(pressure_increase, months_to_failure, 'o-', linewidth=2.5, markersize=8, color='#e74c3c')

# Add annotations for key points
for i, (p, m) in enumerate(zip(pressure_increase, months_to_failure)):
    if i > 0:
        ax.annotate(f'{p}% increase\n→ {m} months', 
                   xy=(p, m), xytext=(p+5, m+3),
                   fontsize=8, ha='left', va='bottom',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.3))

# Labels and title
ax.set_xlabel('Pressure Increase (%)', fontweight='bold')
ax.set_ylabel('Months to Failure (2× Backlog)', fontweight='bold')
ax.set_title('Nonlinear Pressure-Failure Relationship', fontweight='bold', fontsize=12)

# Set axis ranges
ax.set_xlim(-5, 105)
ax.set_ylim(0, 60)

# Grid
ax.grid(True, alpha=0.3)

# Add annotation about nonlinearity
ax.text(50, 45, 'Concave relationship:\nSmall pressure increases produce\ndisproportionate acceleration', 
        fontsize=9, ha='center', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.5))

# Tight layout
plt.tight_layout()

# Save
plt.savefig('../paper/figures/figure3_pressure_failure_curve.png', dpi=300, bbox_inches='tight')
plt.savefig('../paper/figures/figure3_pressure_failure_curve.pdf', bbox_inches='tight')
plt.close()

print("Figure 3 saved: Pressure-failure curve")

# ============================================================================
# FIGURE 4: Combined QAI Comparison (EOIR vs USCIS)
# ============================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=False)

# EOIR plot
ax1.plot(years[1:], qai_eoir[1:], 'o-', linewidth=2, markersize=6, color='#2c3e50', label='EOIR')
ax1.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
ax1.axhline(y=1.0, color='red', linestyle='--', linewidth=1, alpha=0.7)
ax1.set_ylabel('QAI', fontweight='bold')
ax1.set_title('EOIR Immigration Courts (Annual)', fontweight='bold')
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.set_ylim(-0.5, 1.8)
ax1.grid(True, alpha=0.3)
ax1.legend()

# USCIS plot
ax2.plot(range(len(quarters))[1:], qai_uscis[1:], 's-', linewidth=2, markersize=6, color='#e74c3c', label='USCIS')
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
ax2.axhline(y=0.5, color='orange', linestyle='--', linewidth=1, alpha=0.7)
ax2.set_xlabel('Quarter', fontweight='bold')
ax2.set_ylabel('QAI', fontweight='bold')
ax2.set_title('USCIS (Quarterly)', fontweight='bold')
ax2.set_xticks(range(len(quarters)))
ax2.set_xticklabels(quarters, rotation=45, ha='right')
ax2.set_ylim(-0.1, 0.3)
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()

# Save
plt.savefig('../paper/figures/figure4_combined_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('../paper/figures/figure4_combined_comparison.pdf', bbox_inches='tight')
plt.close()

print("Figure 4 saved: Combined comparison")

print("\nAll figures generated successfully!")
print("Location: ../paper/figures/")
