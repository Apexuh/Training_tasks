# файл для работы в templates: 4main.html

from jinja2 import Environment, FileSystemLoader


# link = '''<select name="cities">
# {% for c in cities %}
#     <option value="{{c['id']}}">{{c['city']}}</option>
# {% endfor %}
# </select>
# '''

# persons = [
#     {'name': 'Alex', 'old': 34, 'weight': 105},
#     {'name': 'Maria', 'old': 34, 'weight': 60},
#     {'name': 'Vasya', 'old': 30, 'weight': 80}]
#
#
# file_loader = FileSystemLoader('templates') #из какого подкаталога будем брать шаблон
# env = Environment(loader=file_loader)
#
# tm = env.get_template('4main.html') #get_template создает экземпляр класса Template на основе содержимого файла 4main.html
# msg = tm.render(users=persons) #к экземпляру класса выше применится рендер для получения текстовой строки
#
# print(msg)

# Output:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <base href="https://proproprogs.ru">
#     <title>про программирование</title>
# </head>
# <body>
# <ul>
#     <li>Alex</li>
#     <li>Maria</li>
#     <li>Vasya</li>
#     </ul>
# </body>
# </html>


# Существуют разные загрузчики в пакете jinja:

# PackageLoader - для заргузки шаблонов из пакета
# DictLoader - для загрузки шаблонов из словаря
# FunctionLoader - для загрузки на основе функции
# PrefixLoader - загрузчик, использующий словарь для построения каталогов
# ChoiceLoader - загрузчик, содержащий список дрягих загрузчиков(если один не сработает, то выбирается сдедующий)
# ModuleLoader - загрузчик для скомпилированных шаблонов

# FunctionLoader - для загрузки на основе функции:

from jinja2 import FunctionLoader

persons = [
    {'name': 'Alex', 'old': 34, 'weight': 105},
    {'name': 'Maria', 'old': 34, 'weight': 60},
    {'name': 'Vasya', 'old': 30, 'weight': 80}]

def loadTp(path):
    if path == "4main":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные {{ u }}'''


file_loader = FunctionLoader(loadTp) #из какого подкаталога будем брать шаблон
env = Environment(loader=file_loader)

tm = env.get_template('4main') #get_template создает экземпляр класса Template на основе содержимого файла 4main.html
msg = tm.render(u=persons[0]) #здесь берем только первое значение, тк шаблон не проходится по списку

print(msg)