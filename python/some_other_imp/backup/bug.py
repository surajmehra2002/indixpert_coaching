import os
import shutil

file_path = r"S:\indixpert_coaching\python\some_other_imp\backup\temp.txt"

backup_file_path = r"S:\indixpert_coaching\python\some_other_imp\backup\backup_temp.txt"




def delete_file():
    try:        
        response = input("Are you want to remove this? Y/N ")
        if response=="Y":
            shutil.copy2(file_path, backup_file_path)
            os.remove(file_path)
            print(f"file has been removed.")
            response1 = input("Your file unfortunately deleted?  and want to backup? Y/N ")
            if response1=="Y":
                shutil.copy2(backup_file_path, file_path)
                os.remove(backup_file_path)
                print("Successfully recorver your file")
            else:
                 os.remove(backup_file_path)
                 print("Your file permanentaly deleted..")
            
        else:
            print("your request denied!")
            

    except Exception as e:
        print(f"Error: Could not remove the file '{file_path}'. This Error: {e}")

def backup_file(backup_line):
            
        try:
            with open(backup_file_path, 'w') as file:
                file.write(backup_line)
                print(f"File created successfully at: {backup_file_path}")


        except Exception as e:
            print(f"file not backuped because Error:{e}")
    
# we will check file exists or not
if os.path.exists(file_path): 
    delete_file() # this method will delete file

    
    
       
    
else:
    print(f"file not found.")



