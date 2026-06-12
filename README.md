# Queue Acceleration Index (QAI)

Simple metric to check if government backlogs are getting worse or better.

## What is QAI?

```
QAI = (Pending_t - Pending_{t-1}) / Completions_t
```

Basically: how fast is the backlog growing compared to how fast cases are getting done?

- QAI > 0: backlog growing
- QAI > 1: backlog growing faster than cases being resolved (bad)
- QAI < 0: backlog shrinking (good)

## Files

**Data**
- `data/uscis_quarterly.csv` - USCIS quarterly data
- `data/eoir_annual.csv` - EOIR annual data

**Code**
- `src/extract_uscis.py` - Get data from USCIS PDFs
- `src/extract_eoir.py` - Get data from EOIR PDFs
- `src/compute_qai.py` - Calculate QAI and run stats
- `src/simulate_queue.py` - Queue simulation
- `src/generate_figures.py` - Make all the plots

**Paper**
- `paper/paper_aaii_template.tex` - LaTeX for AAAI submission
- `paper/references.bib` - References
- `paper/figures/` - All figures

## Setup

```bash
pip install -r requirements.txt
```

## How to run

```bash
# Get the data
python src/extract_uscis.py
python src/extract_eoir.py

# Calculate QAI
python src/compute_qai.py

# Run simulation
python src/simulate_queue.py

# Make figures
python src/generate_figures.py

# Compile the paper
cd paper
pdflatex paper_aaii_template.tex
bibtex paper_aaii_template
pdflatex paper_aaii_template.tex
pdflatex paper_aaii_template.tex
```

## Where the data comes from

- USCIS: https://www.uscis.gov/about/reports-and-studies
- EOIR: https://www.justice.gov/eoir/reports-statistics

## Citation

If you use this, please cite:

```
@article{qai-aaai2027,
  title={The Queue Acceleration Index: Measuring Institutional Throughput from Public Data},
  author={Author Name},
  journal={AAAI-27 Student Abstract},
  year={2027}
}
```

## License

MIT

## Questions

Open an issue on GitHub or email me at [email@example.com]
