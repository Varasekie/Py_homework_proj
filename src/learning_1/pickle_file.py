import pickle

dict = {'key1':'value1',
        'key2':'value2',
        'key3':'value3'
        }

####用二进制方法打开（创建）文件
temp_file = open('test.pkl','wb')
####dump（）函数没有返回值，直接操作即可,注意操作的文件名
pickle.dump(dict ,temp_file)
temp_file.close()

