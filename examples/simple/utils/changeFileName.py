import os
path = r'E:\A_py_project\EfficientNet-PyTorch\examples\simple\data\newData\test\2\R'
j=0
files = os.listdir(path)
print(files)
for i in files:
    print(i)
    os.rename(os.path.join(path+"\\"+i),os.path.join(path+"\\"+"R_"+i))
    # print(os.path)
    # os.rename(os)