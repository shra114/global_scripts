import sys
from functions import *
infile = sys.argv[1]
outflile = sys.argv[2]

outlist = []
inlist = parse_file_as_list(infile)
for i in inlist:
    if i not in outlist:
        outlist.append(i)
instr = "\n".join(outlist)
write_str_to_file_with_mode(instr,outflile,"w")
