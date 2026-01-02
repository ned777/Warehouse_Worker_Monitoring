# Warehouse Worker Monitoring

**Author:** Ned Nguyen<br>
**Platform:** Linux (Debian/Ubuntu-based)<br>
**Tech Stack:** Python, Flask, SQLite, HTML/CSS

A real-time warehouse worker monitoring system that tracks item scanning activity, analyzes workload, and provides intelligent alerts to prevent worker overload.

---

## Project Architecture
 
### Project Structure

```
Warehouse_Worker_Monitoring/
│
├── app/
│   ├── scanner.py        # Worker item scanning logic
│   ├── monitor.py        # Monitoring & workload analysis
│   ├── database.py       # SQLite connection helper
│   ├── app.py            # Flask web application
│   ├── templates/        # HTML templates for web interface
│   │   └── index.html
│   └── venv/             # Python virtual environment
│
├── data/
│   ├── database.db       # SQLite database
│
└── README.md
```

## Setup Instructions

### Installing Flask

This project uses Flask for the web interface. The virtual environment is already created in the `app/` folder.

1. Navigate to the app folder and activate the virtual environment:
```bash
cd app
source venv/bin/activate
```

2. Install Flask:
```bash
pip install Flask
```

3. Verify installation:
```bash
python -c "import flask; print(flask.__version__)"
```

4. When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## How to Run the Program

### Running the Flask Web Interface

1. Activate the virtual environment:
```bash
cd app
source venv/bin/activate
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://localhost:5000/warehouse
```

4. To stop the server, press `Ctrl+C` in the terminal

### Running the Scanner

Use this to simulate item scanning:
```
    python3 app/scanner.py
```

### Running the Monitoring System

Use this to analyze worker workload:
```
    python3 app/monitor.py
```    
## Features

### Workload Monitoring
The system tracks and categorizes scanned items based on weight:
- **Overload** (≥150 lbs): Heavy-duty items requiring maximum effort
- **Heavy** (100-149 lbs): Substantial items requiring significant effort
- **Medium** (50-99 lbs): Moderate items requiring average effort
- **Light** (<50 lbs): Lightweight items requiring minimal effort

### Category-Specific Alerts
The monitoring system provides intelligent alerts for each workload category:

**Warning Levels:**
- **Warning**: Worker is handling too much in this category - intervention recommended
- **Normal**: Workload is within acceptable range
- **Abnormal**: Too little activity in this category - potential workflow issue

**Alert Thresholds (15-minute window):**
- Overload: Normal (4-8), Warning (>8)
- Heavy: Normal (6-9), Warning (>9)
- Medium: Normal (8-12), Warning (>12)
- Light: Normal (14-20), Warning (>20)

## Example Output

### Web Dashboard Display
The web interface at `http://localhost:5000/warehouse` shows:
- **Total Load Score**: Cumulative workload score for last 15 minutes
- **Items Scanned**: Number of items processed
- **Workload Analysis**: Real-time scale values and total score
- **Category Analysis & Alerts**: Color-coded alerts for each weight category
- **Recent Scans Table**: Detailed list of scanned items with classifications

### Scale System
- 4 = Overload (≥150 lbs)
- 3 = Heavy (100-149 lbs)
- 2 = Medium (50-99 lbs)
- 1 = Light (<50 lbs)

### Category Alert Examples

**Overload Category:**
- Score >8 → **Warning**: Watch out for this worker not to work too much
- Score 4-8 → **Normal**: Normal workload
- Score <4 → **Abnormal**: Too little overload work

**Heavy Category:**
- Score >9 → **Warning**: Be careful: Too much work
- Score 6-9 → **Normal**: Normal workload
- Score <6 → **Abnormal**: Too little heavy work

**Medium Category:**
- Score >12 → **Warning**: Too much: Watch out
- Score 8-12 → **Normal**: Normal workload
- Score <8 → **Abnormal**: Too little medium work

**Light Category:**
- Score >20 → **Warning**: Too much work
- Score 14-20 → **Normal**: Normal workload
- Score <14 → **Abnormal**: Not normal - Too little light work

## Future Enhancements

### Future Enhancements

- AI-based anomaly detection for worker fatigue/overloading
- Real-time dashboard for supervisors
- Automated email/SMS alerts
- Barcode scanner hardware interface

## License
MIT License

