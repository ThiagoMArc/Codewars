import re

def is_valid_IP(ip):
    pattern = r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$'
    match = re.match(pattern, ip)
    if match:
        return True
    else:
        return False