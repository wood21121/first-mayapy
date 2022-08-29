import sys, os
from utils import osUtils
from utils import mayaUtils
def main(asssetDir):
    scenes = osUtils.getFilesOfTpye(asssetDir, 'mb')
    for scene in scenes:
        abc = mayaUtils.exportCamera(scene)
        print('Exported:', abc)
dir1= r'G:\projects\XBL3\X26\mbs'
main(dir1)
