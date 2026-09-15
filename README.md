# Shotlist Organizer

A Streamlit App that organizes Film Shotlists (Final_Project)

## Features

- CSV-Import of Shotlists (Excel → CSV)
- Filtering by **Scene** or **Location**
- PDF-Export of Shotlist

## Requirements

- Python 3.12.10
- Packages in `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## How to use

1. Clone this repository
2. Open a terminal in the **root folder** of this repository (the folder that contains `FinalProjects/`)
3. Start App:
   ```bash
   streamlit run FinalProject/main.py
   ```
4. Type in Project Name
5. Prepare Excel File (saved as CSV!): Mock File or new file in which columns need to be named exactly: **"Scene"** and **"Location"** 
6. Paste File Path 
7. Decide how you want to filter the Shotlist

## Known Limitations

- Column names need to be "Scene" and "Location" precisely
- Data is currently only saved within each session, not permanently (Download possible though)
- If code can't read newly created CSV file, it might be because German CSV uses ; instead of , to separate columns
  (Should not be the case anymore but if it does turn up again: The ; can be manually changed to , in Excel)

## Author

Fenia Gerhardt
