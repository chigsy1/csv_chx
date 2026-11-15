import os 
import platform
import datetime
from pathlib import Path
import calendar

zDebug: bool = True

def get_os():
    sys:str = platform.system()
    if zDebug:
        print("Operating System:", sys)
    return sys

def get_month_list(month_no:int, month_list:list = []):
    if month_no < 10:
        month_name:str = "0" + str(month_no) + " " + calendar.month_name[month_no]
    else:
        month_name = str(month_no) + " " + calendar.month_name[month_no]
  
    month_list.append(month_name)
    
    return month_list
    

def main():
    # --- Check Operating System 
    sys:str = get_os()

    if sys == "Linux":
        bank_dir: str = "/mnt/shared/Banking/"
    elif sys == "Windows":
        bank_dir: str = "d:\\Banking\\"
        print("This is a Windows system.")

    cwd:str = os.getcwd()
    print("Current Working Directory:", cwd)

    year: str = str(datetime.datetime.now().year)
    print("Current Year:", year)

    month: str = str(datetime.datetime.now().month)
    month_list: list = []
    month_list = get_month_list(int(month), month_list)
    month_list = get_month_list(int(month)-1, month_list)
    month_list = get_month_list(int(month)-2, month_list)
      #month_list = get_month_list(calendar.month, month_list)
      
    print("Current Months:", month_list)
  
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


