import os

def rename_files():
    file_list=os.listdir(r"/Users/ezgi/Desktop/python/prank")
    print(file_list)
    saved_path=os.getcwd()
    print ('Current working directory is '+ saved_path)
    os.chdir(r"/Users/ezgi/Desktop/python/prank")

    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,'0123456789'))



rename_files()









