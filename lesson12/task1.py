# створити об'єкт p - Path на нашу робочу директорію, пробігтись по всіх файлах і папках які лежать
# всередині нашої робочої папки, і якщо ми зустрінемо файл вивести на екран 'МИ ЗНАЙШЛИ ФАЙЛ' і навпаки
from pathlib import Path

# C:/Users/pc/Desktop/заняття/hw_maks/lesson12/task1.py
def check_files_directories(p: Path) -> None:
    for i in p.iterdir():
        if i.is_file():
            print('МИ ЗНАЙЛИ ФАЙЛ')
        else:
            print('МИ ЗНАЙШЛИ ПАПКУ')


check_files_directories(Path())