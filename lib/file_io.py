def write_file(file_name, file_content):
    # Ensure the file has a .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    # Write the content to the file
    with open(file_name, 'w') as file:
        file.write(file_content)
    pass

def append_file(file_name, append_content):
    
    pass

def read_file(file_name):
    pass
