from jinja2 import Template

# name = 'Fedor'
#
# tm = Template('Hello {{ name }}')
# msg = tm.render(name=name)
#
# print(msg)
# =====

# можно через классы
# class Person:
#     def __init__(self):
#         self.name = 'Fedor'
#         self.age = 28
#
# per = Person()
# tm = Template('Hi! I am {{ n.name }} and I am {{ n.age * 2  }} years old')
# msg = tm.render(n=per)
# print(msg)

# ======
# через словарь:

per = {'name':'Fedor', 'age': 28}

tm = Template('Hi! I am {{ n.name }} and I am {{ n.age * 2  }} years old')
msg = tm.render(n=per)
print(msg)