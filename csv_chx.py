import os 
import platform
import datetime
from pathlib import Path
import calendar
import sys

zDebug: bool = True

def get_os():
    # --- Get Operating System
    sys_type:str = platform.system()
    if zDebug:
        print("Operating System:", sys_type)
    return sys_type


def get_month_list(month_no:int, month_list:list = []):
    if month_no < 10:
        month_name:str = "0" + str(month_no) + " " + calendar.month_name[month_no]
    else:
        month_name = str(month_no) + " " + calendar.month_name[month_no]
  
    month_list.append(month_name)
    return month_list


def get_run_env():
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
    run_env["Bank_Dir"] = bank_dir

    return run_env


def get_args():
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Get Command Line Arguments
    # -----------------------------------------------------------------------------------------------------------------------------
    args: list = sys.argv
    if zDebug:
        print("Command Line Arguments:", args[1:])
    return args


def set_bank_dir(args:list, run_env:dict):
    # -----------------------------------------------------------------------------------------------------------------------------
    # --- Set Banking Root Directory
    # -----------------------------------------------------------------------------------------------------------------------------
    print("Setting Banking Root Directory...")
    print("len of Args:", len(args))
    if len(args) == 1:
        bank_dir: str = run_env["Bank_Dir"] + "/" + run_env["Year"] + "/" + run_env["Month"]
    elif len(args) == 2:
        month: str = args[1]
        bank_dir: str = run_env["Bank_Dir"] + "/" + run_env["Year"] + "/" + month
    else:
         year: str = args[2]
         month: str = args[1]
         bank_dir: str = run_env["Bank_Dir"] + "/" + year + "/" + month
    print("Banking Root Directory:", bank_dir)

    return bank_dir


def main():

    run_env: dict = get_run_env()
    print("Run Environment:", run_env)

    some_dir: str = Path('/')
    print("Some Dir:", some_dir)

    args: list = get_args()

    program_name:str = sys.argv[0]
    print("Program Name:", program_name)
    print("Args = ", sys.argv)
 
    bank_dir: str = set_bank_dir(args, run_env)
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


