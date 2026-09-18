from pathlib import Path
import shutil as sh
import os


# Print files and dir present in the main dir
def readFileAndFolder():
    path = Path('Files-Folders')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")
        
    print("-------------------------------------------")

    
# Create new file
def createFile():
    try:
        readFileAndFolder()
        name = input("Enter new file name:- ")
        p = Path('Files-Folders')/name
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in that file:- ")
                fs.write(data)
                
            print("FILE CREATED SUCCESSFULLY")
            print("-------------------------------------------")
            
        else:
            print("This file already exist.")
            print("-------------------------------------------")
            
    except Exception as err:
        print(f"An error occured as {err}")
        

# Read file content
def readFile():
    try:
        name = input("Enter file name you want to read:- ")
        p = Path('Files-Folders')/name
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
                
            print("READ SUCCESSFULLY")
            print("-------------------------------------------")
            
        else:
            print("File dosen't exists.")
            print("-------------------------------------------")
            
    except Exception  as err:
        print (f"An error occured as {err}")
        
        
# Rename File
def renameFile(p):
    nName = input("Enter new name:- ")
    newP = Path('Files-Folders')/nName
    if not newP.exists():
        p.rename(newP)
        
        print("RENAME SUCCESSFULLY")
        print("-------------------------------------------")
        
    else:
        resp = input("Are you soure overwrite the file (y)")
        if resp.lower() == 'y':
            p.rename(newP)
            
            print("RENAME SUCCESSFULLY")
            print("-------------------------------------------")
            
        else:
            print("-------------------------------------------")
            return
            
        
# Overwrite the file
def overwriteFile(p):
    with open(p, "w") as fs:
        data = input("Tell what you want to write this is overwrite the data:- ")
        ores = input("Are you want to overwrite (y):- ")
        if ores == 'y':
            fs.write(data)
        
            print("OVERWRITE SUCCESSFULLY")
            print("-------------------------------------------")
            
        else:
            print("-------------------------------------------")
            return
            
        
# Append the file
def appendFile(p):
    with open(p, "a") as fs:
        data = input("Tell what you want to append:- ")
        fs.write(" " + data)
        
    print("APPEND SUCCESSFULLY")
    print("-------------------------------------------")
        
        
# Update file name / overwritr file / append file
def updateFile():
    readFileAndFolder()
    try:
        name = input("Enter file name you want to update:- ")
        p = Path('Files-Folders')/name
        if p.exists() and p.is_file():
            print("Press 1 for rename")
            print("Press 2 for overwriting data")
            print("Press 3 for append data")
            
            res = int(input("Enter your responce:- "))
            
            if res == 1:
                renameFile(p)
                
            elif res == 2:
                overwriteFile(p)
                
            elif res == 3:
                appendFile(p)
                
            else:
                print("INVALID INPUT")
                print("-------------------------------------------")
        
        else:
            print("File dosen't exists.")
            print("-------------------------------------------")
            
    except Exception as err:
        print("An error occured as {err}")


#Delete the file
def deleteFile():
    readFileAndFolder()
    try:
        print("Press 1 for remove file")
        print("Press 2 for remove folder")
                
        dres = int(input("What you want to delete:- "))
        name = input("Enter which file/folder you want to delete:- ")
        cmf = input("You want to delete this file (y):- ")
        
        p = Path('Files-Folders')/name
        if dres == 1:
            if p.exists() and p.is_file:
                if cmf.lower() == 'y':
                    os.remove(p)
                    
                    print("REMOVE SUCCESSFULLY")
                    print("-------------------------------------------")
                    
                else:
                    print("-------------------------------------------")
                    return

            else:
                print("No such file exists.")
                print("-------------------------------------------")
                
        elif dres == 2:
            if cmf.lower() == 'y':
                sh.rmtree(p)
                
                print("REMOVE SUCCESSFULLY")
                print("-------------------------------------------")
            else:
                print("-------------------------------------------")
                return
            
        
    except Exception as err:
        print(f"An error occured as {err}")
        

while 1:
    try:
        print("Press 1 for creating a file")
        print("Press 2 for reading a file")
        print("Press 3 for updating a file")
        print("Press 4 for deletion a file")
        print("Press 0 for exit")

        check = int(input("Please tell your response :- "))
        print("-------------------------------------------")

        if check == 0:
            break
            
        elif check == 1:
            createFile()
            
        elif check == 2:
            readFile()
            
        elif check == 3:
            updateFile()

        elif check == 4:
            deleteFile()
            
        else:
            print("INVALID INPUT")
            print("-------------------------------------------")
            
    except Exception as err:
        print(f"An error occured as {err}")
