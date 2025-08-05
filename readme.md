## Keno Analyzer

A Python application that fetches results of the Massachusetts Lottery game "Keno". It analyzes the most and least common number combinations over a chosen date range.

## Features
- Fetches real-time Keno results from the Massachusetts Lottery API
- Analyzes combination sizes from 1 to 12 numbers
- Two display formats:
  - Terminal (CLI) for quick analysis
  - Tkinter GUI with a touchscreen-friendly, two-column layout
- Scrollable results in the GUI
- Dynamic headers that update based on selections
- Displays hot numbers (most common) and cold numbers (least common) in the same run

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/olivercahill/keno-analyzer.git
cd keno-analyzer
pip install -r requirements.txt
```

## Terminal (CLI) Example
Insert Integer values for <combo_size> <top_n> <days> : 
```bash
python keno/KenoPatterns_Terminal.py <combo_size> <top_n> <days>
```

## User Interface (GUI) Example
Select values from the interface:
```bash
python keno/KenoPatterns_UI.py
```

## Disclaimer
This project is for educational and entertainment purposes only. Keno is a game of chance and there is no guarantee that this will help you win.

## License
Licensed under MIT License, see LICENSE file for details.