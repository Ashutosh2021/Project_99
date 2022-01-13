import time,os,shutil
from typing import final

days=30
path = input("Enter the path : ")+"/"
days=time.time()

path_exists=os.path.exists(path)

if path_exists :
    file_list=os.walk(path)
    for file in file_list:
        
        stat_info=os.stat(path).st_ctime
        if stat_info>days :
            if os.path.isfile(path) :
                os.remove(path)
            else :
                shutil.rmtree(path)
else : 
    print("Path doesn't exist")