def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w') as text_file:
        text_file.write(file_content)
def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name="test_file"):
    with open(f'{file_name}.txt') as f:
        return f.read()