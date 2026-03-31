from blessed import Terminal
import homepage
import state
import selectSpace
term = Terminal()



def render(text):
    for i in text:
        print(i)
lastKey = None
def main():
    global lastKey
    with term.fullscreen(), term.cbreak():
        while True:
            key = term.inkey(timeout=0.01)
            print(term.home + term.clear,end="",flush=True)
            if state.place == "home":
                print(term.hide_cursor, end="")
                render(homepage.process(term,key))
            
            elif state.place == "selectSpace":
                print(term.hide_cursor, end="")
                render(selectSpace.process(term,key))

            elif state.place == "quit":
                break

main()