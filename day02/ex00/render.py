import sys, os, re

def changer(file):
    print(file)

def error_check(args):
    if len(args) != 2:
        return (print("Wrong number of arguments."), False)
    elif args[1][::-1].split('.')[0][::-1] != 'template':
        return (print("Wrong file extension."), False)
    elif not os.path.isfile(args[1]):
        return (print("Non-existing file."), False)
    return '', True

def render():
    args = sys.argv
    if error_check(args)[1] == False:
        return
    changer(args[1])

if __name__ == '__main__':
    render()