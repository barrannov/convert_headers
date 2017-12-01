import pyperclip

def header_to_dict(str):
    dict = {}
    for x in str.splitlines():
        t = x.split(':', 1)
        dict[t[0].strip()] = t[1].strip()
    return dict

if __name__ == "__main__":
    str = pyperclip.paste()

    try:
        res = header_to_dict(str)
        head = 'headers = {\n'
        for i, key in enumerate(res, start=1):
            if i == len(res):
                head += "\t'" + key + "':'" + res[key] + "'\n"
            else:
                head += "\t'" + key + "':'" + res[key] + "',\n"
        head += '}'
        print(head)
        print('Headers successfully copied to your clipboard!')
        pyperclip.copy(head)
    except Exception:
        print('Seems like no valid headers found')
