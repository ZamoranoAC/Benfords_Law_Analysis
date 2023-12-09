# Benford's Law Analysis on Dataset

## Description

This repository contains a data analysis project implemented in Python that utilizes Benford's Law to assess the authenticity and distribution of data in a specific dataset. Benford's Law is a statistical tool that examines the frequency of leading significant digits in real-world datasets.

## Project Structure

- **`root.py`**: Main code that loads a dataset from a CSV file and applies Benford's Law to each column.
- **`imports.py`**: Module containing the implementation of Benford's Law and functions for visualizing the results. It makes use of the `pandas`, `numpy`, and `matplotlib` libraries.
- **`your_dataset.csv`**: Example input dataset (replace with your own dataset).

## How to Use

1. Clone this repository: `git clone https://github.com/ZamoranoAC/Benfords_Law_Analysis`
2. Ensure you have Python installed.
3. Install dependencies: `pip install -r requirements.txt` (make sure `numpy`, `pandas`, and `matplotlib` are installed).
4. Run the analysis: `python root.py`.

## Results

Results are presented in graphs comparing the expected Benford's distribution with the observed distribution in each dataset column.

## Contributions

Contributions and enhancements are welcome! If you encounter issues, have suggestions, or want to add new features, feel free to open an issue or submit a pull request.
