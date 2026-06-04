import random
import time
from datetime import datetime

### Sets for random logs
# small router, large VPC, business network, small router
ip_addresses = ["192.168.1.10", "10.0.0.45", "172.16.5.4", "192.168.1.50"]
methods = ["GET", "POST", "DELETE", "PUT"]
# server targets: login, grants page (non-profit/education sim), user data, homepage
endpoints = ["/api/v1/login", "/api/v1/grants", "/api/v1/users", "/index.html"]
# Status: ok, created, client error, server error
status_codes = [200, 201, 404, 500]
# To simulate randomness
weights = [0.7, 0.15, 0.1, 0.05]

print("Generating mock server.log: ")

# Use 'with' to automatically close file once done
with open("server.log", "w") as log_file:
    for _ in range(100):
        # timestamp format: YYYY-MM-DD Hr:Min:Sec
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = random.choice(ip_addresses)
        method = random.choice(methods)
        endpoint = random.choice(endpoints)
        status = random.choices(status_codes, weights=weights)[0]

        log_line = f"[{timestamp}] {ip} - {method} {endpoint} - STATUS: {status}\n"
        log_file.write(log_line)

print("\nSuccessfully created 100 service.log entries!\n")
