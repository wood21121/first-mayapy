import os
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

def exportCamera(scene):
    if os.path.isfile(scene):
        cmds.file(scene,open=True, force=True)
        cams = cmds.listRelatives(cmds.ls(type='camera', l = True), p = True, fullPath = True )
        cmds.select(cams)

