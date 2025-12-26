# Warehouse Worker Monitoring (Ubuntu

## Project Architecture
 
### Project Structure


Warehouse_Worker_Monitoring/
│
├── app/
│   ├── scanner.py        # Worker item scanning logic
│   ├── monitor.py        # Monitoring & workload analysis
│   ├── database.py       # SQLite connection helper
│
├── data/
│   ├── database.db       # SQLite database
│
└── README.md

## How to Run the Program

### Running the Scanner
-------------------
Use this to simulate item scanning:

    python3 app/scanner.py

### Running the Monitoring System
-----------------------------
Use this to analyze worker workload:

    python3 app/monitor.py
    
## Example Output

### Sample Output (monitor.py)
--------------------------
Scale values: [4, 3, 2, 1]
Total scale score within 15 mins: 10

Meaning:
4 = overload
3 = heavy
2 = medium
1 = light

## Future Enhancements

### Future Enhancements
-------------------
- AI-based anomaly detection for worker fatigue/overloading
- Real-time dashboard for supervisors
- Automated email/SMS alerts
- Barcode scanner hardware interface

## License
MIT License

