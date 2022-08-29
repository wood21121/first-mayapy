import os, tarfile, glob


def getFilesOfTpye(destinationDir, fileType):
    """

           Get files of given type in given location.

           Parameters:
           destinationDir (str): Directory to search through
           fileType (str): Type of file extension to search for

           Returns:
           fils (list): List of files of found

       """
    fils =[]
    for x in os.walk(destinationDir):
        for y in glob.glob(os.path.join(x[0], '*%s' % fileType)):
                fils.append(y)
    return fils

def moveAbcFile(sourcedir,fileType):
    fils =[]
    for x in os.walk(sourcedir):
        for y in glob.glob(os.path.join(x[0], '*%s' % fileType)):
            fils.append(y)
    return fils




