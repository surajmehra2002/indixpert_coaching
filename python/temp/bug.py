import os

file_path = r"S:\indixpert_coaching\python\temp\bug\temp.txt"



def delete_file():
    try:        
        response = input("Are you want to remove this? Y/N ")
        if response=="Y":
            os.remove(file_path)
            print(f"file has been removed.")
            response1 = input("Your file unfortunately deleted?  and want to backup? Y/N ")
            if response1=="Y":
                backup_file(backup_line)
            else:
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
    

if os.path.exists(file_path):   
    backup_file_path = file_path    
    with open(file_path) as file:
                backup_line = file.read()
    delete_file() # this method will delete file

    
    
       
    
else:
    print(f"file not found.")



