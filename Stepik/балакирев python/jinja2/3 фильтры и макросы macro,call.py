from jinja2 import Template

# cars = [{'car': 'Audi', 'price': 22800},
#         {'car': 'Skoda', 'price': 17600},
#         {'car': 'Volvo', 'price': 44900},
#         {'car': 'Volkswagen', 'price': 26000}]
#
# tmp = "Summary cost of cars: {{ cs | sum(attribute='price') }}"
# tm = Template(tmp)
# res = tm.render(cs=cars)
# print(res)
# output:
# Summary cost of cars: 111300
# ===
# аналогично со списком

# digs = [1,2,3,4,5]
#
# tmp = "Total: {{ cs | sum }}"
# tm = Template(tmp)
# res = tm.render(cs=digs)
# print(res)
# output:
# Total: 15


# ===
# max

# cars = [{'car': 'Audi', 'price': 22800},
#         {'car': 'Skoda', 'price': 17600},
#         {'car': 'Volvo', 'price': 44900},
#         {'car': 'Volkswagen', 'price': 26000}]

# tmp = "Max: {{ (cs | max(attribute='price')).car }}"

# tmp = "Min: {{ (cs | min(attribute='price')).car }}"

# tmp = "Random: {{ (cs | random).car }}"

# tmp = "Replace: {{ cs | replace('o', 'O') }}"
#
#
# tm = Template(tmp)
# res = tm.render(cs=cars)
# print(res)
# output:
# Max: Volvo
# Min: Skoda
# Random: Skoda
# Replace: [{'car': 'Audi', 'price': 22800}, {'car': 'SkOda', 'price': 17600}, {'car': 'VOlvO', 'price': 44900}, {'car': 'VOlkswagen', 'price': 26000}]



#
# persons = [
#     {'name': 'Alex', 'old': 34, 'weight': 105},
#     {'name': 'Maria', 'old': 34, 'weight': 60},
#     {'name': 'Vasya', 'old': 30, 'weight': 80}]
#
# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor -%}'''
#
# tm = Template(tpl)
# res = tm.render(users=persons)
# print(res)

# ALEX
# MARIA
# VASYA


# =======
# модуль jinja поддерживает макроопределение шаблонов
# DRY - don't repeat yourself'

# хотим создать несколько полей input

# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value | e }}" size={{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''
# tpl = Template(html)
# res = tpl.render()
# print(res)
# #
# <p><input type="text" name="username" value="" size=20">
# <p><input type="text" name="email" value="" size=20">
# <p><input type="text" name="password" value="" size=20">

# ===============

# call - вложенные макросы
# persons = [
#     {'name': 'Alex', 'old': 34, 'weight': 105},
#     {'name': 'Maria', 'old': 34, 'weight': 60},
#     {'name': 'Vasya', 'old': 30, 'weight': 80}]
#
#
# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
#     <li>{{ u.name }}
# {%- endfor %}
# </ul>
# {% endmacro %}
#
# {{list_users(users) }}
# '''
#
# tm = Template(html)
# res = tm.render(users=persons)
# print(res)
#
# output:
# <ul>
# <li>Alex<li>Maria<li>Vasya
# </ul>

# output:
# <ul>
# <li>Alex<li>Maria<li>Vasya
# </ul>

# теперь добавим блок call

persons = [
    {'name': 'Alex', 'old': 34, 'weight': 105},
    {'name': 'Maria', 'old': 34, 'weight': 60},
    {'name': 'Vasya', 'old': 30, 'weight': 80}]


html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{ u.name }} {{ caller(u) }}
{%- endfor %}
</ul>
{% endmacro %}

{% call(user) list_users(users) -%}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{%- endcall -%}
'''

tm = Template(html)
res = tm.render(users=persons)
print(res)
#
# output:
# <ul>
# <li>Alex <ul>
#     <li>age: 34
#     <li>weight: 105
#     </ul><li>Maria <ul>
#     <li>age: 34
#     <li>weight: 60
#     </ul><li>Vasya <ul>
#     <li>age: 30
#     <li>weight: 80
#     </ul>
# </ul>