import os
from utils import getList
from shutil import copyfile

def main(sourcepath, targetpat , txtfile ):
    mylist = getList.shotList(txtfile)
    shotlist =[]
    for newlist in mylist:
        shotlist.append(newlist[4:])

    cnt = len(mylist)
    #print(cnt)
    i = 0
    while(i<cnt):
        targetdir = os.path.join(targetpat,mylist[i])
        sourcedir = os.path.join(sourcepath,shotlist[i])
        targetfile = os.path.join(targetdir, mylist[i]) + '.mb'
        sourcefile = os.path.join(sourcedir, mylist[i]) + '.mb'

        if not os.path.exists(targetdir):
           os.makedirs(targetdir)

        copyfile(sourcefile,targetfile)
        print('Copied',mylist[i])
        i +=1


txtfile = r'G:\projects\XBL3\X26\shotlist.txt'
source = r'H:\Projects\XBL3\anim\scenes\X26'
target = r'G:\projects\XBL3\X26\mbs'
if __name__ == '__main__':
    main(source,target, txtfile)