import os
import socket
import time

domain = os.environ.get('DOMAIN_NAME', 'example.com')
port = os.environ.get('PORT', 80)


while True:
    error_count = 0 

    print("# HELP dns_validation_lookup Status of Querying DNS endpoint")
    print("# TYPE dns_validation_lookup summary")
    print("# TYPE dns_validation_response_type summary")
    try:
        start_time = time.time()
        result = socket.getaddrinfo(domain, port)
        end_time = time.time()
        total_time = (end_time - start_time)
        print("dns_validation_lookup {} {}".format(result[2][4][0], time.time()))
        print("dns_validation_response_time {} {}".format(total_time, time.time()))
    except socket.gaierror:
        '''
        If we receive a GAIERRROR, name resolution has failed.
        Increment our counter by one and display counter total.
        '''
        error_count += 1
        print("# TYPE dns_validation_error_count counter")
        print("dns_validation_error_count {} {}".format(error_count), time.time())
    time.sleep(5)
