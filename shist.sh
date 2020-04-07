history | awk '{first = $1; $1 = ""; print $0, first; }' | awk 'NF{NF--};1' >> history.txt
python ~/Documents/github/global_scripts/remove_duplicates.py ~/history.txt ~/history.txt
