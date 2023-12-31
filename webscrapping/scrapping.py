from bs4 import BeautifulSoup
import requests

def write_file(file_name,data):
    with open(file_name,'w') as file:
        file.write(data)

def file_read(file_name):
    with open(file_name,'r') as filename:
        content = filename.read()
        print(content)

def append_file(file_name,data):
    with open(file_name,'a') as filename:
        filename.write(f'\n {data}')

def read_line(file_name,data):
    for line in file_name:
        print(line.strip())

url = "https://kathmandupost.com/"
req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")
all_headlines = soup.find_all("h3")

for hl in all_headlines:
    append_file('abc.txt',hl.string)