import os
import json

# 1) Desired structure: everything inside `contents/`
base_dir = "contents"

# 2) Our improved _toc.yml content
toc_content = f"""format: jb-book
root: {base_dir}/00_intro.md

parts:
  - caption: 01 Fundamentals
    chapters:
      - file: {base_dir}/01_fundamentals/01_preliminaries.md
        sections:
          - file: {base_dir}/01_fundamentals/02_text_and_code.ipynb
            subsections:
              - file: {base_dir}/01_fundamentals/03_exercises.md
              - file: {base_dir}/07_exercises/001.md
      - file: {base_dir}/01_fundamentals/04_intro_fss.md

  - caption: 02 Environmental Source Characterization
    chapters:
      - file: {base_dir}/02_env_source_characterization/01_intro.md

  - caption: 03 Hydrostatic and hydrodynamic loads in FSS
    chapters:
      - file: {base_dir}/03_hydro_loads/01_intro.md

  - caption: 04 Mooring systems of FSS
    chapters:
      - file: {base_dir}/04_mooring_systems/01_intro.md

  - caption: 05 Experimental techniques in FSS
    chapters:
      - file: {base_dir}/05_experimental_techniques/01_intro.md

  - caption: 06 Modeling and analysis of FSS
    chapters:
      - file: {base_dir}/06_modeling_analysis/01_intro.md
    
  - caption: 07 Practical Information
    chapters:
      - file: {base_dir}/08_references.md
      - file: {base_dir}/09_changelog.md
      - file: {base_dir}/10_credits.md
"""

# 3) Create the `contents` folder if it doesn't exist
os.makedirs(base_dir, exist_ok=True)

# 4) Subfolders in `contents`
folders = [
    "01_fundamentals",
    "02_env_source_characterization",
    "03_hydro_loads",
    "04_mooring_systems",
    "05_experimental_techniques",
    "06_modeling_analysis",
    "07_exercises"
]

for folder in folders:
    path = os.path.join(base_dir, folder)
    os.makedirs(path, exist_ok=True)

# 5) Write the _toc.yml in the project root
with open("_toc.yml", "w", encoding="utf-8") as f:
    f.write(toc_content)

# 6) Create placeholder files in contents/

# Main introduction
with open(os.path.join(base_dir, "00_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Main Introduction\n\nThis is the root introduction of your Jupyter Book.")

# Fundamentals
with open(os.path.join(base_dir, "01_fundamentals", "01_preliminaries.md"), "w", encoding="utf-8") as f:
    f.write("# 01 Preliminaries\n\nIntroduce fundamental concepts here.")

# Notebook in fundamentals
notebook_json = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}
with open(os.path.join(base_dir, "01_fundamentals", "02_text_and_code.ipynb"), "w", encoding="utf-8") as f:
    json.dump(notebook_json, f, indent=2)

with open(os.path.join(base_dir, "01_fundamentals", "03_exercises.md"), "w", encoding="utf-8") as f:
    f.write("# 03 Exercises\n\nPlaceholder for additional exercises or notes.")

with open(os.path.join(base_dir, "01_fundamentals", "04_intro_fss.md"), "w", encoding="utf-8") as f:
    f.write("# 04 Introduction to FSS\n\nOverview on Floating Structures & Systems.")

# Exercises folder
with open(os.path.join(base_dir, "07_exercises", "001.md"), "w", encoding="utf-8") as f:
    f.write("# Exercise 001\n\nDescribe the first exercise here.")

# Environmental Source Characterization
with open(os.path.join(base_dir, "02_env_source_characterization", "01_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Introduction\n\nEnvironmental sources and data for FSS.")

# Hydro Loads
with open(os.path.join(base_dir, "03_hydro_loads", "01_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Introduction\n\nHydrostatic and hydrodynamic loads in FSS.")

# Mooring Systems
with open(os.path.join(base_dir, "04_mooring_systems", "01_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Introduction\n\nBasics of mooring systems for FSS.")

# Experimental Techniques
with open(os.path.join(base_dir, "05_experimental_techniques", "01_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Introduction\n\nCommon testing methods and setups.")

# Modeling & Analysis
with open(os.path.join(base_dir, "06_modeling_analysis", "01_intro.md"), "w", encoding="utf-8") as f:
    f.write("# Introduction\n\nApproaches to modeling and analyzing FSS.")

# Practical Info (references, changelog, credits) in `contents/`
with open(os.path.join(base_dir, "08_references.md"), "w", encoding="utf-8") as f:
    f.write("# References\n\nList references here.")

with open(os.path.join(base_dir, "09_changelog.md"), "w", encoding="utf-8") as f:
    f.write("# Changelog\n\nLog major changes here.")

with open(os.path.join(base_dir, "10_credits.md"), "w", encoding="utf-8") as f:
    f.write("# Credits\n\nRecognize contributors and sources here.")

print("All folders/files created successfully under `contents/` with numeric prefixes for sorted order.")
