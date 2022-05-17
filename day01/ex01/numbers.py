def my_numbers():
    my_list = [c for c in open('numbers.txt', 'r').read().strip().split(',')]
    for elem in my_list: 
        print(elem)
        
if __name__ == '__main__':
    my_numbers()