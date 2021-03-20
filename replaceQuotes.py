# Written by : Pentestical
# Simple Python script to replace different quotation marks by the default one (")
# Replacing : left-double (“), right-double quotation marks (“), double-low quotation marks („)
# Useful, when trying to copy exploits with incorrect double quotation marks

# Usage : python3 replaceQuotes.py
# Output inside the same text file you are providing!

#!/usr/bin/env python3
import sys
from colorama import Fore,Style

# try to open the file
try: 
    print(f"{Fore.YELLOW}+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(f"+++++        Welcome to the quotation mark replacer by Pentestical!       +++++\n")
    print(f"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{Style.RESET_ALL}\n")
    fileName=input("Please enter a file name: ")
    with open(fileName,'r',encoding="utf-8") as f:
        filedata=f.read()
    filedata=filedata.replace('\u201d','"')
    filedata=filedata.replace('\u201e','"')
    filedata=filedata.replace('\u201c','"')
    filedata=filedata.replace('\u2033','"')
    with open(fileName,'w',encoding="utf-8") as f:
        f.write(filedata)
    print(f"\n{Fore.GREEN}Finished! All Characters are replaced. Enjoy your file:",fileName)
    f.close()

except:
    print("Could not open the file! Something went wrong.\n")
    sys.exit()
