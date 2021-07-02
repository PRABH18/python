import os
#os.system('notepad')
#os.system('calc')
#os.system('mkdir ram')
#os.system('rmdir ram')
for i in range(1,10):
    t= path='E:\\new\\'
    folder_name='prabhakar'+str(i)
    print(path+folder_name)
    create_folder='mkdir'+t
    os.system(create_folder)