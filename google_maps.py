import requests
import pandas as pd
import datetime
from functions import *


def write_str_to_file_with_mode(str1,file1, mode, print_log):
    F = open(file1,mode)
    F.write(str1)
    F.close()
    if(print_log):
        print ("created the file ", file1)
    return

def get_time(html):
    html = parse_file_as_str(html)
    index_min = html.find('min\\')
    index_min = html.find('min\\', index_min+3)
    index_start = html.rfind('\\"', 0,index_min+3)
    time = html[index_start+2:index_min+3]
    return time


url = "https://www.google.com/maps/dir/Hyderabad,+Telangana/Goa+Velha,+Goa+403110/@16.6660585,73.9542639,7z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x3bcb99daeaebd2c7:0xae93b78392bafbc2!2m2!1d78.486671!2d17.385044!1m5!1m1!1s0x3bbfbe8cf00e90a1:0x9c3d04969bd13976!2m2!1d73.9100068!2d15.501984!3e0"
html = requests.get(url).content
write_str_to_file_with_mode(str(html), "temp.html", "w", True)
time = get_time("temp.html")
print (time, "at ",datetime.datetime.now())