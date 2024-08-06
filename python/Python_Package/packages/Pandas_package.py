import pandas as pd
import os,time

user_dict = {}

user_dict["id"] = [int(input("Please enter student ID: "))]
user_dict["Name"] = [input("Please enter student Name: ")]
user_dict["Address"] = [input("Please enter student Address: ")]
user_dict["Age"] = [int(input("Please enter student Age: "))]
user_dict["Number"] = [int(input("Please enter student Number: "))]



# Convert the dictionary to a DataFrame
df = pd.DataFrame(user_dict)








if os.path.isfile("datas.xlsx"):
    with pd.ExcelWriter('datas.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name='Sheet1', startrow=writer.sheets['Sheet1'].max_row, index=False, header=False)
    print("Data's successfully Saved in database")
    
else: 
    file_name = input("Enter file name in which you are saving data..")
    print(f"\nCreating file {file_name}.xlsx .....")
    time.sleep(2)
    df.to_excel(file_name+".xlsx", index=False)
    print("Excel file created successfully!")    
    










# # Read an Excel file
# df = pd.read_excel('user_dict.xlsx', sheet_name='Sheet1')  # specify sheet_name if needed

# # Display the DataFrame
# print(df)