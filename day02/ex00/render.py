import sys, os, re, settings

def changer(data):
    return re.sub(r'{(\w*)}', lambda x: getattr(settings, x.group(1)), data)

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
    my_file = open(args[1], 'r')
    data = my_file.read()
    data = changer(data)
    result_file = open('myCV.html', 'w')
    result_file.write(data)

if __name__ == '__main__':
    render()