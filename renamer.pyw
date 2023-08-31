from os import rename, listdir

BEGINNING_OF_THE_NAME = "new"
NEW_BEGINNING_OF_THE_NAME = "old"
DIRECTORY = "folder"

# rename("folder/test.txt", "folder/newtest.txt")

files_list = listdir(DIRECTORY)

for file_name in files_list:
    if file_name[0:len(BEGINNING_OF_THE_NAME)] == BEGINNING_OF_THE_NAME:
        new_name = f"{NEW_BEGINNING_OF_THE_NAME}{file_name[len(BEGINNING_OF_THE_NAME):]}"
        if new_name not in files_list:
            rename(f"{DIRECTORY}/{file_name}", f"{DIRECTORY}/{new_name}")
