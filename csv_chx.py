import os 
import platform
import datetime
from pathlib import Path
import calendar
import sys

zDebug: bool = True
slash: str = os.sep

def get_os():
    # --- Get Operating System
    sys_type:str = platform.system()
    if hasattr(sys, "getandroidapilevel"):  # - Workaround pydroid thinks it's on linux.'
        sys_type = "Android"
    if zDebug:
        print("Operating System:", sys_type)
    return sys_type


def get_month_list(month_list:list = []) -> list: 
    for month_no in range(1, 13):
        month_str: str = calendar.month_name[month_no]
        if month_no < 10:
            month_name:str = "0" + str(month_no) + " " + month_str
        else:
            month_name = str(month_no) + " " + month_str
  
        month_list.append(month_name)

    return month_list


def get_run_env() -> dict:
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Get Run Environment
    # -----------------------------------------------------------------------------------------------------------------------------
    run_env: dict = {"OS": "Unknown", "Bank_Dir": "Unknown", "CWD": "Unknown", "Year": "Unknown", "Month": "Unknown"}

    # --- Get Operating System
    sys_type:str = get_os()
    run_env["OS"] = sys_type

    # --- Set current year and month.
    year: str = str(datetime.datetime.now().year)
    run_env["Year"] = year

    # ---  Get month number and name.
    month: str = str(datetime.datetime.now().month - 1) # Use previous month.
    if int(month) < 10:
        month_prefix = "0" + month
    else:
        month_prefix = ""
    month_name: str = calendar.month_name[int(month) ]  
    month: str = month_prefix + str(month) + " " + month_name
    run_env["Month"] = month

    # --- Set banking root directory
    if sys_type == "Linux":
         bank_dir: str = "/mnt/shared/Banking" 
    elif sys_type == "Windows":
         bank_dir: str = "d:\\Banking"
    else:
         bank_dir: str = "/storage/emulated/0/ICh/scratch"
         #bank_dir: str = "/data/data/com.termux/files/home/storage/shared/ICh/scratch"
    run_env["Bank_Dir"] = bank_dir

    return run_env


def get_args() -> list:
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Get Command Line Arguments
    # -----------------------------------------------------------------------------------------------------------------------------
    args: list = sys.argv
    if zDebug:
        print("Command Line Arguments:", args[1:])
    return args


def set_option_defaults(run_env: dict) -> dict:
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Set Option Defaults
    # -----------------------------------------------------------------------------------------------------------------------------
    option_defaults: dict = {"Bank_Dir": run_env["Bank_Dir"], "Year": run_env["Year"], "Month": run_env["Month"]}
    return option_defaults


def set_bank_dir(options: dict):
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Set Banking Root Directory
    # -----------------------------------------------------------------------------------------------------------------------------
    print("Setting Banking Root Directory...")

    bank_dir: str = options["Bank_Dir"] + slash + options["Year"] + slash + options["Month"]
         
    print("Accounts Directory:", bank_dir)

    return bank_dir
    
    
def process_args(args: list, options: dict):
    iArg: int = 0
    print("len of Args:", len(args))
    for arg in args:
        print("----- Arg ", arg)
        match arg:
            case '-y':
                print("Arg ", iArg, "Set Year")
                options["Year"] = args[iArg + 1]
            case '-m':
                print("Arg ", iArg, "Set Month")
                month_part: str = args[iArg + 1]
                month_found: str = check_month(month_part)
                if month_found != "":
                    options["Month"] = month_found
                    print("Month set to:", month_found)
                else:
                    print("Error:", month_part, "does not uniquely identify a month.")
                    sys.exit(1)
        iArg += 1 

def check_month(user_month: str) -> str:
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Check user-supplied month is part of a month string in the month list.  
    #     Return True if a single match is found, otherwise return False.
    # -----------------------------------------------------------------------------------------------------------------------------
    month_list: list = get_month_list()
    Nmatch: int = 0

    for month in month_list:
        month_lc: str = month.lower()
        if month_lc.find(user_month.lower()) != -1:
            Nmatch += 1
            month_found = month
 
    return month_found if Nmatch == 1 else ""

def main():

    program_name:str = sys.argv[0]
    print("Program Name:", program_name)

    run_env: dict = get_run_env()
    print("Run Environment:", run_env)

    some_dir: str = Path('/')
    print("Some Dir:", some_dir)

    args: list = get_args()
    options: dict = set_option_defaults(run_env)

    print("Args = ", sys.argv)
    process_args(sys.argv, options)
 
    bank_dir: str = set_bank_dir(options)
    os.chdir(bank_dir)
    cwd:str = os.getcwd()
    print("Current Working Directory:", cwd)
 
    files:list = os.listdir()
    print("Files in Current Directory:")
    for file in files:
        i: int = file.find("Current")
        if i != -1:
            #bank_dir = bank_dir + "/" + file
            #os.chdir(bank_dir)
            print(file)


if __name__ == "__main__":
    main()


