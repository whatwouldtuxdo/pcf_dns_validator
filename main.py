import os
import socket
import time

domain = os.environ.get('DOMAIN_NAME', 'example.com')
port = os.environ.get('PORT', 80)


while True:
    try:
        start_time = time.time()
        result = socket.getaddrinfo(domain, port)
        end_time = time.time()
        total_time = (end_time - start_time) * 10000
        print("Success - %s - Completed in %.2fms." % (result[2][4][0], total_time))
    except socket.gaierror:
        print("ERROR - DNS Validation")
    time.sleep(5)
