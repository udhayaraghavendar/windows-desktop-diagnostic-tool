# windows-desktop-diagnostic-tool
## A Python-based Windows diagnostic utility designed to collect essential system health information, verify application status, and check network connectivity.The tool automatically generates a timestamped diagnostic report, making it useful for IT Support / Application Support scenarios.

## ✅ Key Features

- Displays system and OS details
- Monitors RAM usage
- Checks C: drive disk health
- Verifies running applications
- Tests internet connectivity
- Generates detailed log report automatically

## 🛠️ Tech Stack

- Python 3
- psutil
- platform
- socket
- datetime

## 📁 Project Structure
```
windows-desktop-diagnostic-tool/
├── diagnostic_tool.py
├── README.md
└── system_report_sample.txt
 ```

## ▶️ How to Run
```bash
Step 1: Install Dependency
pip install psutil

Step 2: Run the Script
python diagnostic_tool.py
```
## 📄 Output

- Console shows real-time diagnostic results
- A log file is created automatically in the same folder
- Example: system_report_27_11_2025_18_45_12.txt

## 🔍 Diagnostic Checks

- System Information  
- Operating System
- Processor & architecture
- Total RAM and usage %

### Disk Health
- Total disk size (C drive)
- Used and free space
- Low disk space warning
- Application Status

### Checks if the following applications are running:
- chrome.exe
- msedge.exe
- explorer.exe

### Network Connectivity
- Tests internet connection using Google DNS (8.8.8.8)

## Output:

<img width="1920" height="1080" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/1f20f6a4-9df8-4dba-aa72-454ff3bf09c9" />

## Log File:

<img width="1920" height="1080" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/ad5c9d40-5826-4bb8-a0ea-8550661334ce" />
<img width="1920" height="1080" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/34a38916-3e91-4184-85de-72f5613696bd" />

## 🎯 Use Case

- This project simulates real-world desktop health checks commonly handled by:
- IT Support Engineers
- Application Support Engineers
- Service Desk Agents
- It demonstrates practical troubleshooting and basic automation skills using Python

## 🚀 Future Enhancements

- CPU monitoring
- Service status checks
- Export report as PDF
- Email alert integration
- Cross-platform support

## 👤 Author

- Udhayaraghavendar
- B.Tech – Information Technology
- Skills: Python | SQL | Networking | IT Support
