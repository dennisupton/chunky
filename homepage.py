import asciiArt
import state
import time

optionIdx = 0
def drawAscii(term,art):
    art = art.split("\n")
    res = []
    offset = len(art)//2
    for line in range(len(art)):
        res.append(term.move_yx(round(term.height /2)-offset+line, 0) + term.center(art[line]))
    return res

configDir = "None"
def process(term,key):
    global optionIdx,configDir
    options = ["Open Space ("+str(configDir)+")","Select Space","Quit"]

    res = []

    res += drawAscii(term,asciiArt.TITLELOGOS[round(time.time()/3)%len(asciiArt.TITLELOGOS)])

    for i in range(len(options)):
        if i == optionIdx:
            start = term.blue(asciiArt.LCAP)
            end = term.blue(asciiArt.RCAP)
            text = start+term.on_blue(term.white(f" {options[i]} "))+end   
        else:
            text = ""+options[i]
        res.append(term.move_yx(round(term.height /2)+10+i, 0) + term.center(text))

    if key:
        if key.code == term.KEY_UP:
            optionIdx  -= 1
        if key.code == term.KEY_DOWN:
            optionIdx  += 1
        if key.code == term.KEY_ENTER or key == " ":
            if optionIdx == 0 and configDir:
                pass
            elif optionIdx == 1:
                state.place = "selectSpace"
            elif optionIdx == 2:
                state.place = "quit"
            
    optionIdx = max(0,min(optionIdx,len(options)-1))

    return res

