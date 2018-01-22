import os



rootfilepath = os.path.abspath(__file__)

dirname = os.path.dirname(rootfilepath)



testpath = os.path.join(dirname,'readme.md')
print(testpath)

print(os.path.isfile(testpath))

testdir = os.path.dirname(testpath)
print(testdir)


dir = '/Users/zack-zhao/Desktop/2018-01-21/selenium-framework/src/library'

# dirs = dir.split('/')

print(os.path.sep)



# print(dirs)

# while(rootpath):
#     if(os.path.isfile(os.path.join(rootpath,'readme.md'))):
#         break