import os
import subprocess
import datetime
from statistics import median
from random import randrange
#print(randrange(10))


def search_list_elements_in_order_in_str(str1, start_list, end_str):
    index = str1.find(start_list[0])
    for i in start_list[1:]:
        index = str1.find(i,index+1)
    index += len(start_list[-1])
    end_index = str1.find(end_str, index+1)
    return str1[index: end_index]
def remove_things_from_str(str1, list1):
    for i in list1:
        str1 = str1.replace(i,"")
    return str1

def parse_csv(file_name, delimeter=","):
    list1 = parse_file_as_list(file_name)
    return_list= list()
    for i in list1:
        if(i.strip()==""):
            continue
        return_list.append(i.split(delimeter))
    return return_list

def average(list1):
    return(sum(list1)/len(list1))

def get_req_col_csv(list1, no):
    ret_lst = []
    for i in list1:
        ret_lst.append(i[no])
    return ret_lst
def get_weights(list1):
    ret_lst = []
    fl_list1 = [float(i) for i in list1]
    ret_lst = [ round(100*(i/sum(fl_list1)),2) for i in fl_list1]
    return ret_lst
def get_str_bw(str1, start, end, search_start=0,print_error=False):
    index_start = str1.find(start,search_start)
    index_end   = str1.find(end,index_start)
    str_return = str1[index_start+len(start):index_end]
    if((index_start == -1) or (index_end == -1)):
        if(print_error):
            print ("start : ",start)
            print ("end : ",end)

    if((str_return == "") or (index_start == -1) or (index_end == -1)):
        str_return = "-"

    return str_return,index_end

def parse_file_as_str(file0):
    F = open(file0,'r')
    str0 = F.read()
    F.close()
    return str0

def parse_file_as_list(file0):
    F = open(file0,'r')
    str0 = F.read()
    list1 = str0.split("\n")
    F.close()
    return list1
def replace_in_list(l1, old_str, new_str):
    l2 = list()
    for i in l1:
        l2.append(str(i).replace(old_str,new_str))
    return l2
def get_cagr(list1):
    cagr = 1.0
    for i in list1:
        cagr = cagr * (1+i*0.01)
    return cagr**(1.0/len(list1))
#print (get_cagr([10,20,30]))  ##Ans: 1.1972

def search_str_in_list(str1,list1):
    for i in list1:
        if(str1 in i):
            return list1.index(i)
    return  None

def subtwo_lists(l1,l2):
    l3 = list()
    for i in range(len(l1)):
        try:
            l3.append(float(l1[i]) - float(l2[i]))
        except:
            l3.append(l1[i])
    return l3
def divtwo_lists(l1,l2):
    l3 = list()
    for i in range(len(l1)):
        l3.append(float(l1[i])/l2[i])
    return l3

def get_date():
    'retuns as 19_12_31'
    now = datetime.datetime.now()
    #'2019-12-09 22:03:51.676886' --str format
    l=str(now).split()[0].split('-')
    l[0] =l[0][2:]
    return '_'.join(l)

def all_greater(list1,val):
    retval = True
    for i in list1:
        retval &= i > val
    return retval
#print(all_greater([1,2,4],1))

def moving_averages(l1,n=2):
    ma = list()
    ma = l1[:n]
    for i in range(n,len(l1)):
        list1 = l1[i-n:i]
        ma.append(round(sum(list1)/len(list1),2))
    return ma
#print (moving_averages([1,2,3,4,5,6]))
#[1, 1.5, 2, 2.5, 3, 3.5]


def all_less(list1,val):
    retval = True
    for i in list1:
        retval &= i < val
    return retval
#print(all_less([1,2,4],5))

def get_diffs(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    return [set1==set2, list(set1-set2), list(set2-set1), list(set1&set2)]
#print (get_diffs([1,2,3,4],[6,5,4,3]))

def get_lsout(directory, grep_txt = None):
    ls_lst = os.listdir(directory)
    if(grep_txt==None):
        return ls_lst
    ls_lst_grep = list()
    for i in ls_lst:
        if (".swp" in i):
            continue
        if (grep_txt in i):
            ls_lst_grep.append(i)
    ls_lst_grep.sort()
    return ls_lst_grep


def create_dir(path):
    cmd='mkdir -p '+str(path)
    subprocess.call(cmd,shell=True)
    return None

def cmd_call(cmd):
    subprocess.call(cmd, shell=True)
    print ("Running command",cmd)
    return None

def write_str_to_file_with_mode(str1,file1, mode, print_log=True):
    F = open(file1,mode)
    F.write(str1)
    F.close()
    if(print_log):
        if(mode =="w"):
            print ("created the file ", file1)
        elif (mode=="a"):
            print("appended to the file ", file1)
    return
