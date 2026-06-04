

import json
import requests

def parse_log_file(file_path):
    # Initialize directory for data gathering
    metrics = {
        "Total_Requests": 0,
        "Errors_404": 0,
        "Errors_500": 0,
        "Successful_Requests": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            metrics["Total_Requests"] += 1

            if "STATUS: 200" in line or "STATUS: 201" in line:
                metrics["Successful_Requests"] += 1
            elif "STATUS: 404" in line:
                metrics["Errors_404"] += 1
            elif "STATUS: 500" in line:
                metrics["Errors_500"] += 1
        
        return metrics
    
def send_webhook_alert(data):
    # dummy endpoint for testing
    webhook_url = "https://httpbin.org/post"
    # alert webhook json incomming
    headers = {"Content-Type": "application/json"}

    system_status = "CRITICAL" if data["Errors_500"] > 0 else "HEALTHY"
    
    payload = {
        "alert_title": "Faux Server Log Summary",
        "system_status": system_status,
        "metrics": data
    }

    print(f"Sending alert payload to simulated endpoint: ")
    response = requests.post(webhook_url, data=json.dumps(payload, indent=4), headers=headers)

    # Update user on status
    print(f"\nSystem Operation Status: {system_status}\n")

    if response.status_code == 200 or response.status_code == 201:
        print("Alert Successfully Delivered! :D ")
    else:
        print("Failed to Send Alert. Server Responded: {response.server_code}")

# if file is run directly, return results, otherwise allow function to be runnable on it's own
if __name__ == "__main__":
    results = parse_log_file("server.log")
    print("Parsing Complete. Resulting Status Data: ")

    #use json.dumps to convert dict to formatted string
    clean_results = json.dumps(results, indent=4)
    print(clean_results)

    #send parsed log, not string
    send_webhook_alert(results)