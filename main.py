from tkinter import filedialog
from tkinter import *
import xml_to_csv_bank


def browse_file_button():
    file_name = filedialog.askopenfilename()
    start_file_text.set(file_name)


def ok(window):
    window.destroy()


def browse_dir_button():
    file_name = filedialog.askdirectory()
    end_file_text.set(file_name)


def convert():
    # result_window = Toplevel(root)
    # result_window.geometry('200x100')
    # result_window.resizable(False, False)
    # Grid.rowconfigure(result_window, 0, weight=1)
    # Grid.columnconfigure(result_window, 0, weight=1)
    #
    # label = Label(result_window, text='Готово')
    # label.grid(row=0, column=0)

    # button = Button(result_window, text='OK', command=ok(result_window))
    # button.grid(row=1, column=0)
    start = start_file_entry.get()
    end = end_file_entry.get()
    xml_to_csv_bank.xml_to_csv_bank(start, end)


root = Tk()
root.title('Из XML в CSV для ПАО ВТБ')
root.geometry('500x120')
root.resizable(False, False)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Label(text='Выберите файл для конвертации').grid(row=0, column=0, sticky=W, padx=5)
start_file_text = StringVar()
start_file_entry = Entry(root, textvariable=start_file_text)
start_file_entry.grid(row=0, column=1, sticky=W, ipadx=20)
browse1 = Button(root, text='Обзор', command=browse_file_button)
browse1.grid(row=0, column=2, ipadx=30, padx=10)

Label(text='Укажите путь для конечного файла').grid(row=1, column=0, sticky=W, padx=5)
end_file_text = StringVar()
end_file_entry = Entry(root, textvariable=end_file_text)
end_file_entry.grid(row=1, column=1, sticky=W, ipadx=20)
browse2 = Button(root, text='Обзор', command=browse_dir_button)
browse2.grid(row=1, column=2, ipadx=30, padx=10)

calculate = Button(root, text='Сконвертировать', command=convert)
calculate.grid(row=2, column=2, sticky=S+E+N+W, pady=10, padx=10)

root.mainloop()
