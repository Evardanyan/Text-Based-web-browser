import os
import sys
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style

init()

def parse_html(request):
    if "https://" not in request:
        request = "https://" + request
    content = []
    ext_content = ""
    page = requests.get(request)
    soup = BeautifulSoup(page.content, "html.parser")
    result = ""
    lines = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])
    for line in lines:
        result += line.text + "\n"
    lines1 = soup.find_all(["a"])
    for line1 in lines1:
        result += Fore.BLUE + line1.text + "\n"
    lines3 = soup.find_all(["ul", "ol", "li"])
    for line3 in lines3:
        result += line3.text + "\n"
    return result

args = sys.argv
dir_name = args[1]


try:
        # Create target Directory
    os.mkdir(f'C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{dir_name}')
    print("Directory ", dir_name, " Created ")
except FileExistsError:
    print("Directory ", dir_name, " already exists")

history_path = f'C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{dir_name}/'
custom_list = []
browser_history = deque()

while True:
    url_input = str(input())
    if url_input in custom_list:
        read_file = f"C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/{url_input}"
        with open(read_file, 'r', encoding="utf-8") as r:
            print(r.read())
    if url_input == "wiki":
        url_input = 'wikipedia'
        read_file = f"C:/Users/topso/PycharmProjects/Text-Based Browser/Text-Based Browser/task/tb_tabs/{url_input}"
        with open(read_file, 'r', encoding="utf-8") as r:
            print(r.read())
    else:
        url_filtering = str(url_input)[str(url_input).find('.') + 1:str(url_input).rfind('.')]
    name = url_filtering
    tab = history_path + name
    custom_list.append(name)
    if url_input == "exit":
        break
    if "." in url_input:
        print(parse_html(url_input))
        with open(tab, 'w' , encoding="utf-8") as f:
            f.write(parse_html(url_input))
            browser_history.appendleft(parse_html(url_input))
    if url_input == "back":
        if len(browser_history) != 0:
            print(browser_history.pop())
