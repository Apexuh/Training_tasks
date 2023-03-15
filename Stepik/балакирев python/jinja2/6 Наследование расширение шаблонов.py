from jinja2 import Environment, FunctionLoader, FileSystemLoader

persons = [
    {'name': 'Alex', 'old': 34, 'weight': 105},
    {'name': 'Maria', 'old': 34, 'weight': 60},
    {'name': 'Vasya', 'old': 30, 'weight': 80}]



file_loader = FileSystemLoader('templates') #из какого подкаталога будем брать шаблон
env = Environment(loader=file_loader)

tm = env.get_template('6about.html') #get_template создает экземпляр класса Template на основе содержимого файла 4main.html
msg = tm.render()
print(msg)