
import os
import time

days = 5
folders = ['C:\XXX']

deleted_size = 0
deleted_file = 0
deleted_dirs = 0


now_time = time.time()                       # берет время в секундах
past_time = now_time - 60 * 60 * 24 * days   # от текущего вермени переменную дни в секундах


def delete_old_files(folder):
    global deleted_size
    global deleted_file
    for path, dirs, files in os.walk(folder):
        for file in files:
            file_name = os.path.join(path, file)       # полный путь к фаилу
            file_update = os.path.getmtime(file_name)
            if file_update < past_time:
                size_file = os.path.getsize(file_name)
                deleted_size += size_file              # освободившаяся память
                deleted_file += 1                      # сколько файлов удалилось
                print(f'Удаление файла: {str(file_name)}')
                os.remove(file_name)                   # удаление файлов


def delete_empty_dir(folder):
    global deleted_dirs
    count = 0
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            deleted_dirs += 1
            count += 1
            print(f'Удаление пустой папки: {str(path)}')
            os.rmdir(path)
    if count > 0:
        delete_empty_dir(folder)


start_time = time.asctime()

for folder in folders:
    delete_old_files(folder)
    delete_empty_dir(folder)


finish_time = time.asctime()

print('------------------------------------------------------------------')
print(f'START TIME:                   {start_time}')
print(f'TOTAL DELETED SIZE:           {round(deleted_size/1024/1024, 2)} MB')
print(f'TOTAL DELETED FILES:          {deleted_file} ea')
print(f'TOTAL DELETED EMPTY FOLDERS:  {deleted_dirs} ea')
print(f'FINISH TIME:                  {finish_time}')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
