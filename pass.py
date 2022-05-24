import zipfile

#nama file
pwd_filename = "wordlist.txt"
zip_filename = "ass.zip"

#membaca password list yang dibuat
with open(pwd_filename, "rb") as passwords:
    
    #mengubah semua password dalam bentuk list dan mencari total list
    passwords_list = passwords.readlines()
    total_passwords = len(passwords_list)

    #load zipfile
    my_zip_file = zipfile.ZipFile(zip_filename)
    
    for index, password in enumerate(passwords_list):
        #jika password berhasil
        try:
            my_zip_file.extractall(path="Extracted Folder",  pwd=password.strip())
            print("\n +++++++++++++++++++CRACK SUCCESS+++++++++++++++++++++++")
            print("Password : ", password.decode().strip())
            print("file zip sudah di ekstrak ke dalam Extracted folder")
            break
        
        #jika password gagal
        except:
            print(f"Trying password {password.decode().strip()} ")
            print(f"!..................................Scanning complete {round((index/total_passwords)*100, 2)}%")
            print("FAIL!\n")
            continue