if not os.path.exists("{{ c.title }}"):
    os.mkdir("{{ c.title }}")
os.chdir("{{ c.title }}")
{% for m in c.get_modules %}
{% include 'whitenapp/scripts/module-script.py' %}
{% endfor %}
os.chdir("..")