import sys
import msvcrt

def get_userchoice((prompt, choices), exitnums, preload):
    inp = preload
    p = '\r' + prompt
    print p + inp,
    while True:
        x = msvcrt.getch()
        y = ord(x)
        out = ''
        if y in exitnums:
            print
            return (inp,y)
        elif y == 8:        # backspace
            if len(inp) > 0:
                inp = inp[:-1]
                out = chr(8) + ' ' + chr(8)
        elif y == 9:        # tab
            print '\r',
            matches = [c for c in choices if inp.lower() == c.lower()[:len(inp)]]
            if len(matches) == 1:
                inp = matches[0]
            else:
                chlist = ' ( ' + ' '.join(matches) + ' )'
                print chlist + ' '*( len(prompt)+len(inp)-len(chlist) ) 
            print prompt + inp,
        elif y == 27:       # blank (start over)
            print p + ' '*(len(prompt)+len(inp)) + p,
            inp = ''
        elif 32 < y < 127:  # printable
            out = x
            inp += x
        elif y == 224:
            y = ord(msvcrt.getch())
            if y == 72:     # up
                print
                return (inp,y+256)
            if y == 75:     # left
                pass
            if y == 77:     # right
                pass
            if y == 80:     # down
                pass
        sys.stdout.write(out)

def nav_userchoices(ls):
    names = [''] * len(ls)
    idx = 0
    while idx < len(names):
        (choice, ecode) = get_userchoice(ls[idx], {3, 10, 13}, names[idx])
        if ecode == 328:
            idx -= 1 if idx > 0 else 0
        else:
            names[idx] = choice
            idx += 1
    return names
