from jinja2 import Environment, FunctionLoader, FileSystemLoader

persons = [
    {'name': 'Alex', 'old': 34, 'weight': 105},
    {'name': 'Maria', 'old': 34, 'weight': 60},
    {'name': 'Vasya', 'old': 30, 'weight': 80}]



file_loader = FileSystemLoader('templates') #из какого подкаталога будем брать шаблон
env = Environment(loader=file_loader)

tm = env.get_template('5page.html') #get_template создает экземпляр класса Template на основе содержимого файла 4main.html
msg = tm.render(domain='http://proproprogs.ru', title='Про Jinja') #здесь берем только первое значение, тк шаблон не проходится по списку

# print(msg)

# Output:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <base href="http://proproprogs.ru">
#     <title>Про Jinja</title>
# </head>
# <body>
# <p>Содержимое страницы</p>
# </body>
# </html>



# =======
# import
# можно не только включать отдельые файлы в шаблон, но и импортировать их

print(msg)
#
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <base href="http://proproprogs.ru">
#     <title>Про Jinja</title>
# </head>
# <body>

# <p>Содержимое страницы</p>
# <div class="dialog">
#   <p class="title">Warning</p>
#   <p class="message">This is test dialog</p>
#   <p><input type="button" value="Закрыть"></p>
# </div>
#
# </body>
# </html>