# Warehouse Worker Monitoring (Linux – Debian/Ubuntu-based)

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
## Example Output

### Sample Output (monitor.py)
```
	Scale values: [4, 3, 2, 1]
	Total scale score within 15 mins: 10
```
Meaning:
4 = overload
3 = heavy
2 = medium
1 = light

## Future Enhancements

### Future Enhancements

- AI-based anomaly detection for worker fatigue/overloading
- Real-time dashboard for supervisors
- Automated email/SMS alerts
- Barcode scanner hardware interface

## License
MIT License

