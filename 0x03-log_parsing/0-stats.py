#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys

if __name__ == "__main__":
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}


    def print_stats():
        """Print statistics"""
        print('File size: {}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print("{}:{}".format(key, status_codes[keys]))

    def parse_line(line):
        """Check whether the lines matches or not"""
        try:
            line = line[:-1]
            word = line.split(' ')
            file_size[0] += int(word[-1])
            status_code = int(word[-2])

            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass
    
    line_num = 1
    try:
        for line in sys.stdin:
            parse_line(line)
            """ printing after every 10 lines"""
            if line_num % 10 == 0:
                print_stats()
            line_num += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

