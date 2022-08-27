import sys, os
from utils import osUtils
def main(asssetDir):
    scenes = osUtils.getFilesOfTpye(asssetDir, 'mb')
    for scene in scenes:
        print(scene)
dir1= r'G:\projects\XBL3\pytool\dir1'
if __name__ == '__main__':
    main(dir1)