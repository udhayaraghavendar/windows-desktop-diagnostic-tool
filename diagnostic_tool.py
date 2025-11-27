import psutil
import platform
import subprocess
import socket
from datetime import datetime

# --------------------------------------------------
# LOG FILE SETUP
# --------------------------------------------------
current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
log_file = f"system_report_{current_time}.txt"

def log(message):
    print(message)
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(message + "\n")


# --------------------------------------------------
# SYSTEM INFORMATION
# --------------------------------------------------
def system_info():
    log("\n===== SYSTEM INFORMATION =====")
    log(f"OS Name        : {platform.system()}")
    log(f"OS Version     : {platform.version()}")
    log(f"Machine        : {platform.machine()}")
    log(f"Processor      : {platform.processor()}")

    ram = psutil.virtual_memory()
    log(f"Total RAM      : {round(ram.total / (1024**3), 2)} GB")
    log(f"RAM Usage      : {ram.percent}%")


# --------------------------------------------------
# DISK HEALTH CHECK
# --------------------------------------------------
def disk_health():
    log("\n===== DISK HEALTH CHECK =====")
    disk = psutil.disk_usage("C:/")
    free_percent = 100 - disk.percent

    log(f"Total Disk     : {round(disk.total / (1024**3), 2)} GB")
    log(f"Used Disk      : {disk.percent}%")
    log(f"Free Space     : {round(disk.free / (1024**3), 2)} GB")

    if free_percent < 10:
        log("⚠️ WARNING: Low disk space on C drive!")
    else:
        log("✅ Disk space is sufficient.")


# --------------------------------------------------
# APPLICATION STATUS CHECK
# --------------------------------------------------
def application_status():
    log("\n===== APPLICATION STATUS =====")
    apps_to_check = ["chrome.exe", "msedge.exe", "explorer.exe"]

    running_apps = [p.name().lower() for p in psutil.process_iter()]

    for app in apps_to_check:
        if app in running_apps:
            log(f"✅ {app} is running")
        else:
            log(f"❌ {app} is NOT running")


# --------------------------------------------------
# NETWORK CONNECTIVITY CHECK
# --------------------------------------------------
def network_check():
    log("\n===== NETWORK CONNECTIVITY =====")
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        log("✅ Internet connectivity OK")
    except:
        log("❌ Internet connectivity FAILED")


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------
def main():
    log("====================================")
    log(" WINDOWS DESKTOP DIAGNOSTIC TOOL ")
    log("====================================")

    system_info()
    disk_health()
    application_status()
    network_check()

    log("\n✅ Diagnostic check completed.")
    log(f"Log file saved as: {log_file}")


if __name__ == "__main__":
    main()
