import subprocess
from functions import *
data_dir = '/home/shra1/Downloads/data/'
zip_dir = '/home/shra1/Documents/data_zip/'

source_dirs = get_lsout(data_dir,'')#.check_output("ls ../data/",shell=True).strip().split("\n")
zip_dirs    = get_lsout(zip_dir,'')#subprocess.check_output("ls ",shell=True).strip().split("\n")
for i in source_dirs:
	if i+".zip" not in zip_dirs:
		cmd = "zip "+zip_dir+i+".zip " +data_dir+i+"/*"
		subprocess.call(cmd,shell=True)
		print (cmd)
	else: 
		print (i+".zip exists")

