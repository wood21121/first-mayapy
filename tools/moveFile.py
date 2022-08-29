import os
import shutil
from utils import osUtils
def main(sourcedir, distination, fileType):
    dirlist = osUtils.moveAbcFile(sourcedir,fileType)

    for mydir in dirlist:
        mypath = os.path.normpath(mydir)
        filename = mypath.split(os.sep)[-1]
        target = os.path.join(distination,filename)
        shutil.move(mydir, target)
        print('moved:', target)


source = r'G:\projects\XBL3\X26\mbs'
dist = r'G:\projects\XBL3\X26\X26_crowd\abc\cam'
if __name__ == '__main__':
    main(source, dist, fileType='abc')