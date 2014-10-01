def ascii_case_change(line, flag):
    newline = ""
    for i in line:
        try:
            k = ord(i)
            if k in range(0, 32) or k >= 127:
                print i, 'is not legal ascii character.'
                continue
            elif k in range(32, 65) or k in range(91, 97) or k in range(123, 127):
                newline = newline + i
            elif k in range(65, 91):
                if not flag:
                    newline = newline + chr(k + 32)
                else:
                    newline =  newline + i
            elif k in range(97, 123):
                if flag:
                    newline = newline + chr(k - 32)
                else:
                    newline = newline + i
        except TypeError:
            print i, 'is not a legal character.'
    return line, newline

def cml_parser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', default= '159&^*%^$asdfHGFSL~`\|')
    parser.add_argument('--flag', dest='flag', action = 'store_true', default=True)
    op=parser.parse_args()
    return op

op = cml_parser()
print ascii_case_change(op.input, op.flag)
