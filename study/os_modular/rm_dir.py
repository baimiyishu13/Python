import os

# path = 'images'
# file_list = os.listdir(path)    # ['test1', 'test2', 'test_dir']
# for file in file_list:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)

# 切换目录
os.chdir('../images')
print(os.getcwd())  # C:\Users\admin\Desktop\Python\study\images