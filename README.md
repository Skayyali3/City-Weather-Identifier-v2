# City-Weather-Identifier-v2

##  Project History
This GUI is the second version of a three-part evolution:
1. **[Jordan Weather Legacy v1](https://github.com/Skayyali3/Jordan-Weather-Identifier-v1)** - The Prototype: First Python GUI using static File I/O.
2. **City Weather Identifier v2 (This repo)** - Data Viz: Desktop app with live API integration and Seaborn/Matplotlib graphs. 
3. **[City Weather Identifier v3](https://github.com/Skayyali3/City-Weather-Identifier-v3)** - Full-Stack: Responsive web app with Flask backend and Pandas data processing.

---

## The Data Viz Edition
While v1 proved the logic, v2 focuses on data visualization. This desktop application fetches live global weather data and generates dynamic charts to help users visualize 7-day trends.

## Key Features
-Geospatial Intelligence: Integrated `geopy` to convert human-readable city names into Latitude and Longitude coordinates for API precision.
- Time-Series Analysis: Implemented logic to map API timestamps to readable chart axes using the `datetime` library.
- Visual Analytics:
   1.Line Plots: For tracking Max/Min temperature fluctuations.
   2.Bar Charts: For visualizing precipitation, rain, and snowfall sums.
- Interactive GUI: Built with `tkinter`, featuring a dynamic `Option Menu` that updates the visualization type based on user preference.

---

## Tech Stack & Dependencies
1. GUI: `tkinter`
2. Data Science: `matplotlib`, `pandas` and `seaborn`
3. Networking: `requests` and `geopy`

---

## How to Run

Follow these steps to run the project locally:

### 1. Clone the repository and enter:
```bash
git clone https://github.com/Skayyali3/City-Weather-Identifier-v2.git
cd City-Weather-Identifier-v2
```
### 2. Make a virtual environment
```bash
python -m venv venv

source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

### 3. Install the needed requirements
```bash
pip install -r requirements.txt
```

### 4. Run
```bash
python City_Weather_Identifier.py

```
## License

This project is licensed under the MIT License – see the **[LICENSE](LICENSE)** file for details.

## Author
**Saif Kayyali**
