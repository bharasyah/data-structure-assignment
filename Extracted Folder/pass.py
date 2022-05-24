import zipfile

#file names 
pwd_filename = "passwords_list.txt"
filename="chromedriver_win32.zip"
zip_filename = "my_locked.zip"

#read passwords_list file in binary mode
with open(pwd_filename, "rb") as passwords:
    
    #convert all the passwords into a list 
    passwords_list = passwords.readlines()
    
    #total number of passwords
    total_passwords = len(passwords_list)

    #load zipfile
    my_zip_file = zipfile.ZipFile(zip_filename)
    
    for index, password in enumerate(passwords_list):
        #try if password is correct
        try:
            my_zip_file.extractall(path="Extracted Folder",  pwd=password.strip())
            print("\n +++++++++++++++++++SUCCESS+++++++++++++++++++++++")
            print("Password Found: ", password.decode().strip())
            print("All Files has been Extracted inside the New DIrectory Extracted Folder")
            break
        
        #if password fails
        except:
            
            print(f"!..................................Scanning complete {round((index/total_passwords)*100, 2)}%")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"Trying password {password.decode().strip()} ")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            continue