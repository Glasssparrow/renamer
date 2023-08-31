from tkinter import filedialog as fd
from tkinter import Button, Tk, Label, Entry
from datetime import datetime


INITIAL_DIR = ""  # Начальная папка
WINDOW_WIDTH = 600
ENTRY_WIDTH = 100
FOLDER_BUTTON_WIDTH = 50
ACTION_BUTTON_WIDTH = 80
SHOW_FILES_BUTTON_WIDTH = 20


class Gui:

    title_text = "Переименовыватель файлов 1.0"

    def _choose_folder(self):
        """
        Функция выбора папки в которую будет выводиться файл с выполненными
        расчетами.
        """
        self.folder = (
            fd.askdirectory(title="Выберите папку",
                            initialdir=INITIAL_DIR)
        )
        self._text_folder.configure(text=self.folder)

    def _show_files(self):
        old = self._old_beginning.get()
        new = self._new_beginning.get()
        directory = self.folder
        files_list = self.get_files_list(directory, old, new)
        new_text = ""
        for file in files_list:
            new_text += file + "\n"
        self._files_list.configure(text=new_text)

    def _action(self):
        old = self._old_beginning.get()
        new = self._new_beginning.get()
        directory = self.folder
        self.rename_files(directory, old, new)
        time = datetime.now()
        self._files_list.configure(
            text=f"Успешно! Время {str(time.hour)}:"
                 f"{str(time.minute)}:{str(time.second)}"
        )

    def __init__(self, renaming_function, getting_files_list_function):
        self.rename_files = renaming_function
        self.get_files_list = getting_files_list_function
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry(f"{WINDOW_WIDTH}x220")

        # Текст пути к папке
        self._text_folder = Label(text=INITIAL_DIR)
        self._text_folder.grid(columnspan=6, column=0, row=0)

        self._old_beginning = Entry(width=ENTRY_WIDTH, justify="center")
        self._old_beginning.grid(columnspan=6, column=0, row=1)

        self._new_beginning = Entry(width=ENTRY_WIDTH, justify="center")
        self._new_beginning.grid(columnspan=6, column=0, row=2)

        # Кнопка выбора папки
        self._folder_selection_button = (
            Button(self._window, text="Выбрать папку",
                   width=FOLDER_BUTTON_WIDTH,
                   command=self._choose_folder)
        )
        self._folder_selection_button.grid(columnspan=4, column=0, row=3)

        # Кнопка просмотра выбранных файлов
        self._folder_selection_button = (
            Button(self._window, text="Посмотреть файлы",
                   width=SHOW_FILES_BUTTON_WIDTH,
                   command=self._show_files)
        )
        self._folder_selection_button.grid(columnspan=2, column=4, row=3)

        # Кнопка переименования файлов
        self._action_button = (
            Button(self._window, text="Переименовать файлы",
                   width=ACTION_BUTTON_WIDTH,
                   command=self._action)
        )
        self._action_button.grid(columnspan=6, column=0, row=4)

        # Текст пути к папке
        self._files_list = Label(text="Файлы не выбраны")
        self._files_list.grid(columnspan=6, column=0, row=5)

        # Запускаем окно
        self._window.mainloop()
