import os

def shotList(txtfile):
    filename = txtfile
    filelist = []
    with open(filename,'r') as fp:
        lines = fp.readlines()

        for line in lines:
            filelist.append(line.rstrip())
            if not line:
                break
    return filelist

##debug
#txtfile = r'G:\projects\XBL3\X26\shotlist.txt'
#shotList(txtfile)
