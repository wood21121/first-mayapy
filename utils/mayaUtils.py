import os
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

def exportCamera(scene):
    if os.path.isfile(scene):
        cmds.file(scene, open=True, force = True, loadNoReferences=True,rer = True)

        cams = cmds.listCameras(p = True)
        start, end = cmds.playbackOptions(q=True, minTime=True), cmds.playbackOptions(q=True, maxTime=True)
        cmds.select(cams,visible=True)
        abcStr = ''
        for obj in cmds.ls(sl=True, l =True):
            abcStr += '-root' + obj


        cmds.loadPlugin("AbcExport.so")

        name_start = scene[:36]
        name_end = scene[36:]
        name = name_start + 'cam_' + name_end
        framerang = '_' + str(int(start)) + '-' + str(int(end)) + '.abc'
        export =name.replace('.mb', framerang)
        abcStr = '%s -frameRange %s %s -uvWrite -file %s' % (abcStr, start, end, export)
        cmds.AbcExport(j=abcStr)
        return export
        #return print(abcStr)
#file = r'G:\projects\XBL3\pytool\dir1\01_002\X25_01_002.mb'
#exportCamera(file)
