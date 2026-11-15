import os 
import platform
import datetime
from pathlib import Path



def main():
    # --- Check Operating System 
    sys:str = platform.system()
    print("Operating System:", sys)

    if sys == "Linux":
        bank_dir: str = "/mnt/shared/Banking/"
    elif sys == "Windows":
        bank_dir: str = "d:\\Banking\\"
        print("This is a Windows system.")

    cwd:str = os.getcwd()
    print("Current Working Directory:", cwd)

    '''year: str = str(datetime.datetime.now().year)
        print("Current Year:", year)
        bank_dir = bank_dir + year
    
        month: str = input("Enter the month: ")
    
        os.chdir(bank_dir)
    
    '''
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


