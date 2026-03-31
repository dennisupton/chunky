from pathlib import Path
import asciiArt
import config
import state

currentDir = 
folderIdx = 0
folders = []
offset = 0
prevFolderIdx = []

def getFolders(path):
    folders = []
    for entry in path.iterdir():
        if entry.is_dir():
            folders.append(entry.name)
    folders.sort()
    return folders

folders = getFolders(currentDir)
def process(term,key):
    global folderIdx, folders, currentDir,offset
    res = []

    while folderIdx-offset <0 and offset> 0:
        offset -= 1
    while folderIdx-offset>= term.height-1 and folderIdx < len(folders):
        offset += 1

    folderIdx = max(0,min(folderIdx,len(folders)-1))

    for i in range(offset,min(term.height+offset-1, len(folders))):
        if i == folderIdx:
            start = term.blue(asciiArt.LCAP)
            end = term.blue(asciiArt.RCAP)
            text = start+term.on_blue(term.white(f" {folders[i]} "))+end   
        else:
            text = "  "+folders[i]
        res.append(text)
    if key:
        if key.code == term.KEY_UP:
            folderIdx  -= 1
        if key.code == term.KEY_DOWN:
            folderIdx  += 1
        if key.code == term.KEY_RIGHT:
            currentDir = currentDir / folders[folderIdx]
            folders = getFolders(currentDir)
            prevFolderIdx.append(folderIdx)
            folderIdx = 0
            offset = 0
        if key.code == term.KEY_LEFT:
            currentDir = currentDir.parent
            folders = getFolders(currentDir)
            if len(prevFolderIdx) > 0:
                folderIdx = prevFolderIdx[-1]
                prevFolderIdx.pop(-1)
            else:
                folderIdx = 0
            offset = 0

        if key == r"\x1b" or key == " ":
            config.setSpaceDir(str(currentDir / folders[folderIdx]))
            state.place = "home"
        if key.code == term.KEY_ESCAPE:
            state.place = "home"

        

            


    return res