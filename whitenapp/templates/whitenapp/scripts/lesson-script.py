if not os.path.exists("L{{ l.order }}-{{ l.title }}"):
    print(" - - opening lesson: {{ l.title }}...")
    os.mkdir("L{{ l.order }}-{{ l.title }}")
os.chdir("L{{ l.order }}-{{ l.title }}")
{% for u in l.get_units %}
{% include 'whitenapp/scripts/unit-script.py' %}
{% endfor %}
print("finished lesson: {{ l.title }}")
os.chdir("..")
