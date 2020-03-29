import requests
import pandas as pd
import datetime


def write_str_to_file_with_mode(str1,file1, mode, print_log):
    F = open(file1,mode)
    F.write(str1)
    F.close()
    if(print_log):
        print "created the file ", file1
    return

def get_time(html):
	index_min = html.find('min\\"]')
	index_min = html.find('min\\"]', index_min+3)
	index_start = html.rfind('\\"', 0,index_min+3)
	time = html[index_start+2:index_min+3]
	return time

url = "https://www.google.com/maps/dir/AMD+Research+%26+Development+Centre+India+Private+Limited,+8th+-11th+Floor,+Bldg.+No:11,+Raheja+Mindspace,+APIIC+Software+Layout,+Madhapur,+Hyderabad,+Telangana+500081,+India/G.P.Rao+Estates,+Rd+Number+2,+KPHB+Phase+I,+K+P+H+B+Phase+1,+Kukatpally,+Hyderabad,+Telangana+500072,+India/@17.4609282,78.3701546,14z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x3bcb93e23889a8b1:0x6eb581e2947a72ae!2m2!1d78.3821501!2d17.4380946!1m5!1m1!1s0x3bcb9192ff743d09:0x7191b8306899fbf4!2m2!1d78.398309!2d17.4898841!3e0" 

html = requests.get(url).content
write_str_to_file_with_mode(html, "temp.html", "w", True)
time = get_time(html)
print time, "at ",datetime.datetime.now()