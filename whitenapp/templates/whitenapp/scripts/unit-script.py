if not os.path.exists("U{{ u.order }}-{{ u.name }}"):
    os.mkdir("U{{ u.order }}-{{ u.name }}")
os.chdir("U{{ u.order }}-{{ u.name }}")
print("downloading unit: {{ u.name }}...")
{% if u.type.name == 'Video' %}
video = pafy.new("{{ u.url }}")
best = video.getbest()
best.download(filepath="{{ u.name }}." + best.extension)
{% else %}
urllib.request.urlretrieve("{{ u.url }}")
{% endif %}
print("finished unit: {{ u.name }}")
os.chdir("..")