def select_storage(mode: str) -> str:
    if mode == 'to sign':
        selected_path = 'data/hashes_to_sign.txt'
    elif mode == 'signed':
        selected_path = 'data/signed_hashes.txt'
    else:
        selected_path = None

    return selected_path

def read_first_line(mode: str) -> str:
    with open(select_storage(mode), 'r') as file:
        lines = file.readlines()
        return lines[0]

def save_hash_to_file(hash: str, mode: str) -> None:
    with open(select_storage(mode), 'a') as file:
        file.write(hash + '\n')
        file.truncate()

def remove_hash_from_file(mode: str) -> None:
    with open(select_storage(mode), 'a+') as file:
        # read an store all lines into list
        lines = file.readlines()
        # move file pointer to the beginning of a file
        file.seek(0)
        # truncate the file
        file.truncate()
        
        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        file.writelines(lines[1:])
