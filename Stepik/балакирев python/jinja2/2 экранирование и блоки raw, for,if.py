from jinja2 import Template



# data = '{{ name }} with Jinja' #без экранирования: Fedor with jinja
# data = '{% raw %}{{ name }} with Jinja{% endraw %}' #с экранированием:{{ name }} with Jinja
#
# tm = Template(data)
# res = tm.render(name='Fedor')
# print(res)

# =========
# В html требуется в определенные моменты сохранять экранирование:

# link = '''в html ссылки отображаются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template(link)
# res = tm.render()
# print(res)
# # вывод в консоли:
# '''в html ссылки отображаются так:
# <a href="#">Ссылка</a>'''
# а в браузере при сохранении файла 2 строчка преобразуется в ссылку, для отображения как текст нужно использовать
# для экранирования флаг 'e'

# link = '''в html ссылки отображаются так:
# <a href="#">Ссылка</a>'''
#
# tm = Template("{{ link | e }}")
# res = tm.render(link=link)
# print(res)
# =
# можно сделать и так:
# link = '''в html ссылки отображаются так:
# <a href="#">Ссылка</a>'''
#
# res = escape(link) # у меня не работает, возможно версия другая. У Сергея все ок, результат как выше
# print(res)


# ==============
# цикл for

# cities = [{'id': 1, 'city': 'Moscow'},
#           {'id': 2, 'city': 'Tver'},
#           {'id': 3, 'city': 'Minsk'}]

# link = '''<select-name="cities">
# {% for c in cities %}
#     <option-value="{{ c['id'] }}">{{c['city']}}</option>
# {% endfor %}
# </select>'''

# чтобы не было на выходе лишнего переноса строки , надо в цикле for перед % поставить минус:
# link = '''<select-name="cities">
# {% for c in cities -%}
#     <option-value="{{ c['id'] }}">{{c['city']}}</option>
# {% endfor -%}
# </select>'''
#
#
# tm = Template(link)
# res = tm.render(cities=cities)
# print(res)

# output:
# <select-name="cities">
#
#     <option-value="1">Moscow</option>
#
#     <option-value="2">Tver</option>
#
#     <option-value="3">Minsk</option>
#
# </select>
#
# с минусом в цикле for:
# <select-name="cities">
# <option-value="1">Moscow</option>
# <option-value="2">Tver</option>
# <option-value="3">Minsk</option>
# </select>



# =============================
# if:
cities = [{'id': 1, 'city': 'Moscow'},
          {'id': 2, 'city': 'Tver'},
          {'id': 3, 'city': 'Minsk'}]

link = '''<select-name="cities">
{% for c in cities -%}
{% if c.id> 1 -%}
    <option-value="{{ c['id'] }}">{{c['city']}}</option>
{% else -%}
    {{ c.city }}
{% endif -%}
{% endfor -%}
</select>'''


tm = Template(link)
res = tm.render(cities=cities)
print(res)

# output:
# <select-name="cities">
# Moscow
# <option-value="2">Tver</option>
# <option-value="3">Minsk</option>
# </select>