import string

def create():
    for l in string.ascii_uppercase:
        file_name = f"{l}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {l}")

create()