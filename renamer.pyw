from os import rename, listdir
from gui import Gui


def choose_files(directory, old, new):
    files_list = listdir(directory)
    result = []
    for file in files_list:
        if (
                file[0:len(old)] == old and
                edit_name(old, new, file) not in files_list
        ):
            result.append(file)
    return result


def edit_name(old, new, filename, only_in_beginning=True):
    if only_in_beginning:
        result = f"{new}{filename[len(old):]}"
    else:
        result = filename.replace(old, new)
    return result


def renaming(directory, old_beginning, new_beginning):

    files_list = choose_files(directory, old_beginning, new_beginning)
    for file_name in files_list:
        new_name = edit_name(old_beginning, new_beginning, file_name)
        rename(f"{directory}/{file_name}",f"{directory}/{new_name}")


gui = Gui(renaming, choose_files)
