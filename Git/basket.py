"""
Создайте класс  File, у которого есть:

1) метод __init__, который должен принимать на вход имя файла и записывать его в атрибут name. Также необходимо
создать атрибуты in_trash , is_deleted  и записать в них значение False

2)метод  restore_from_trash, который печатает фразу «Файл {name} восстановлен из корзины» и проставляет атрибут in_trash в значение False

3)метод  remove, который печатает фразу «Файл {name} был удален» и проставляет атрибут is_deleted  в значение True

4)метод read, который
печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Прочитали все содержимое файла {self.name}» если файл не удален и не в корзине

5)метод write, который принимает значение content для записи и
печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истин, и выходит из метода
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истин, и выходит из метода
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине

Часть 2:
Далее создайте класс  Trash у которого есть:

1)атрибут класса  content изначально равный пустому списку

2)статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить
его в атрибут content и проставить файлу атрибут in_trash значение True.
Если в метод add передается не экземпляр класса File, необходимо вывести сообщение «В корзину добавлять можно только файл»

3) статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов, хранящийся в
атрибуте content , в порядке их добавления в корзину вызвать метод файла remove.
 Атрибут content  после очистки должен стать пустым списком.
Сама процедура очистки должна начинаться фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»

4)статик-метод  restore, который запускает процесс восстановления файлов из корзины.
Необходимо для всех файлов, хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash.
Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться
фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»




"""










class File:
    def __init__(self, name, in_trash=False, is_deleted=False):
        self.name = name
        self.in_trash = in_trash
        self.is_deleted = is_deleted

    def restore_from_trash(self):
        self.in_trash = False
        print(f"Файл {self.name} восстановлен из корзины")

    def remove(self):
        self.is_deleted = True
        print(f"Файл {self.name} был удален")

    def read(self):
        if self.is_deleted == True:
            print(f"ErrorReadFileDeleted({self.name})")
            return
        if self.in_trash == True:
            print(f"ErrorReadFileTrashed({self.name})")
            return
        if self.is_deleted == False and self.in_trash == False:
            print(f"Прочитали все содержимое файла {self.name}")

    def write(self, content):
        if self.is_deleted == True:
            print(f"ErrorWriteFileDeleted({self.name})")
            return
        if self.in_trash == True:
            print(f"ErrorWriteFileTrashed({self.name})")
            return
        if self.is_deleted == False and self.in_trash == False:
            print(f"Записали значение {content} в файл {self.name}")




class Trash:
    content = []

    @staticmethod
    def add(self):
        if not isinstance(self,File):
            print(f"В корзину добавлять можно только файл")
        else:
            Trash.content.append(self)
            self.in_trash=True


    @staticmethod
    def clear():
        print("Очищаем корзину")
        for files in Trash.content:
            File.remove(files)
        Trash.content.clear()
        print("Корзина пуста")




    @staticmethod
    def restore():
        print(f"Восстанавливаем файлы из корзины")
        for files in Trash.content:
            File.restore_from_trash(files)
        Trash.content.clear()
        print("Корзина пуста")

f1 = File('puppies.jpg')
print(f1.__dict__)  # {'name': 'puppies.jpg', 'in_trash': False, 'is_deleted': False}
f1.read()  # Прочитали все содержимое файла puppies.jpg
f1.remove()  # Файл puppies.jpg был удален
f1.read()  # ErrorReadFileDeleted(puppies.jpg)

f2 = File('cat.jpg')
f2.write('hello')  # Записали значение hello в файл cat.jpg
f2.remove()  # Файл cat.jpg был удален
f2.write('world')  # ErrorWriteFileDeleted(cat.jpg)


f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() #