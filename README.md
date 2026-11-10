# Queue Acceleration Index (QAI)

The Queue Acceleration Index compares the change in pending cases with the number of cases completed in the same period. This repository applies it to USCIS and EOIR data.

## What is QAI?

```
QAI = (Pending_t - Pending_{t-1}) / Completions_t
```

A value of 0 means the backlog stayed the same. Positive values indicate growth. For example, 1.2 means the backlog grew by 1.2 cases per completed case. Negative values indicate a shrinking backlog. The ratio requires a positive number of completions.

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

The working title is *The Queue Acceleration Index: Measuring Institutional Throughput from Public Data*. See the [manuscript source](paper/paper_aaii_template.tex).

## License

MIT

## Questions

Open an issue on GitHub.
