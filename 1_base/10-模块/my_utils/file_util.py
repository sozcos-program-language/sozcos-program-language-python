import str_util

def print_file_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        read = f.read()
        print(read)

def append_to_file(file_path, data):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(data)


print(str_util.str_reverse('hello'))