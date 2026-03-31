def process(term):
    txt_content = [""]
    cursor_x, cursor_y = 0, 0

    for i, line in enumerate(txt_content):
        print(term.move_yx(i, 0) + line)
    print(term.move_yx(cursor_y, cursor_x), end='', flush=True)

    status = f"--- chunky | pos : {cursor_x},{cursor_y} | Press ESC to quit ---"
    print(term.move_yx(term.height - 1, 0) + term.black_on_white(status.ljust(term.width)))
    
    # Place the cursor
    print(term.move_yx(cursor_y-1, cursor_x), end='', flush=True)

    # 2. THE INPUT HANDLER (Manual Logic)
    key = term.inkey()

    if key.code == term.KEY_ESCAPE:
        break
    elif key.code == term.KEY_ENTER:
        txt_content.append("")
        cursor_y += 1
        cursor_x = 0
    elif not key.is_sequence: # Standard character
        line = list(txt_content[cursor_y])
        line.insert(cursor_x, key)
        txt_content[cursor_y] = "".join(line)
        cursor_x += 1
    elif key.code == term.KEY_RIGHT:
        cursor_x += 1
    elif key.code == term.KEY_LEFT:
        cursor_x -= 1
    elif key.code == term.KEY_UP:
        cursor_y -= 1
    elif key.code == term.KEY_DOWN:
        cursor_y += 1
    

    cursor_x = max(0, min(term.width - 1, cursor_x))
    cursor_y = max(0, min(term.height - 1, cursor_y))