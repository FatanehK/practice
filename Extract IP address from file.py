import re

def extract_ip_addresses(file_path):
    with open(file_path,"r") as file :
        text = file.read()
        ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
        return ip_addresses


# Replace with the path to your text file
file_path = 'path_to_your_text_file.txt'
ip_addresses = extract_ip_addresses(file_path)
print(ip_addresses)
