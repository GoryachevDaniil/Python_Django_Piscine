from path import Path

def my_program():
    try:
        Path.makedirs('my_dir')
    except FileExistsError as exc:
        print(exc)
    Path.touch('my_dir/my_file.txt')
    f = Path('my_dir/my_file.txt')
    f.write_lines(['COMPLETE!'])
    print(f.read_text(), end='')

if __name__ == '__main__':
    my_program()