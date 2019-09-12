from os import walk

from . import config

def getFilesNames():
    f = []
    for (dirpath, dirnames, filenames) in walk(config.INDEXDATA_DIRECTORY):
        for fi in filenames:
            fi.strip()
            splits = fi.split('.')
            if len(splits) > 1:
                if splits[1] == 'csv':
                    f.append(dirpath + fi)
        break
    print(f)
    return f

def getArchivedFilesNames():
    f = []
    for (dirpath, dirnames, filenames) in walk(config.ARCHIVED_INDEXDATA_DIRECTORY):
        for fi in filenames:
            fi.strip()
            splits = fi.split('.')
            if len(splits) > 1:
                if splits[1] == 'csv':
                    f.append(dirpath + fi)
        break
    print(f)
    return f

if __name__ == '__main__':
    getFilesNames()