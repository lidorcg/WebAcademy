if not os.path.exists("M{{ m.order }}-{{ m.title }}"):
    print(" - opening module: {{ m.title }}...")
    os.mkdir("M{{ m.order }}-{{ m.title }}")
os.chdir("M{{ m.order }}-{{ m.title }}")
{% for l in m.get_lessons %}
{% include 'whitenapp/scripts/lesson-script.py' %}
{% endfor %}
print("finished module: {{ m.title }}")
os.chdir("..")