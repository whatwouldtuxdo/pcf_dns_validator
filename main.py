import os
import socket
import time

domain = os.environ.get('DOMAIN_NAME', 'example.com')
port = os.environ.get('PORT', 80)


while True:
    error_count = 0 

    print("# HELP dns_validation Status of Querying DNS endpoint")
    print("# TYPE dns_validation summary")
    try:
        start_time = time.time()
        result = socket.getaddrinfo(domain, port)
        end_time = time.time()
        total_time = (end_time - start_time) * 10000
        print("dns_validation_lookup {}".format(result[2][4][0]))
        print("dns_validation_response_time {}".format(total_time))
    except socket.gaierror:
        error_count=error_count+1
        print("dns_validation_error_count {}".format(error_count))
    time.sleep(5)
