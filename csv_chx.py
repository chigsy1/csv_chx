import os 
import platform
import datetime



def main():
    # --- Check Operating System 
    sys:str = platform.system()
    print("Operating System:", sys)

    if sys == "Linux":
        bank_dir: str = "/mnt/shared/Banking/"
    elif sys == "Windows":
        print("This is a Windows system.")

    year: str = str(datetime.datetime.now().year)
    print("Current Year:", year)
    bank_dir = bank_dir + year

    month: str = input("Enter the month: ")
    #bank_dir = bank_dir + "/" + month

    os.chdir(bank_dir)

    files:list = os.listdir()
    print("Files in Current Directory:")
    for file in files:
        i: int = file.find(month)
        if i != -1:
            bank_dir = bank_dir + "/" + file
            os.chdir(bank_dir)
            print(file)

    cwd:str = os.getcwd() 
    print("Current Working Directory:", cwd)


if __name__ == "__main__":
    main()


