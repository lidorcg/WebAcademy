if not os.path.exists("L{{ l.order }}-{{ l.title }}"):
    os.mkdir("L{{ l.order }}-{{ l.title }}")
os.chdir("L{{ l.order }}-{{ l.title }}")
{% for u in l.get_units %}
{% include 'whitenapp/scripts/unit-script.py' %}
{% endfor %}
os.chdir("..")