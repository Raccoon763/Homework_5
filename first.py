import os
import shutil
import platform

def create_dir():
   dir_true = input('Введите имя создаваемой директории:')
   if os.path.exists(dir_true):
      print('Директория уже существует')
   else:
      os.mkdir(dir_true)

def remove_dir():
   dir_true = input('Введите наименование удаляемого файла/папки:')
   if os.path.exists(dir_true):
      if os.path.isdir(dir_true):
         os.removedirs(dir_true)
      else:
         os.remove(dir_true)
   else:
      print('Указанные файл/папка не найдены')

def copy_dir():
   dir_true = input('Введите наименование копируемого файла/папки:')
   dir_copy = input('Назовите новую копию:')
   if os.path.exists(dir_true):
      if os.path.isdir(dir_true):
         shutil.copytree(dir_true, dir_copy)
      else:
         shutil.copy(dir_true, dir_copy)
   else:
      print('Указанные файл/папка не найдены')

def show_dir():
   myfolder = os.listdir(os.getcwd())
   print(myfolder)

def show_dir_file():
   myfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
   print(myfiles)

def show_dir_pap():
   mypap = [f for f in os.listdir(os.getcwd()) if os.path.isdir(f)]
   print(mypap)

def os_inf():
   x = platform.machine()
   y = platform.platform()
   print(y, x)

def me():
   print('Raccoon, greatest pythoneer of the century')

