import os
if not os.path.exists("white"):
	print("opening white folder...")
	os.mkdir("white")
os.chdir("white")
file = open('__init__.py', 'w+')

import urllib.request
if not os.path.exists("pafy.py"):
	url = 'https://raw.githubusercontent.com/np1/pafy/master/pafy/pafy.py'
	print("downloading pafy.py...")
	urllib.request.urlretrieve(url, "pafy.py")
from white import pafy

{% if course %}
{% include 'whitenapp/scripts/course-script.py' with c=course %}
{% elif module %}
{% include 'whitenapp/scripts/module-script.py' with m=module %}
{% elif lesson %}
{% include 'whitenapp/scripts/lesson-script.py' with l=lesson %}
{% elif unit %}
{% include 'whitenapp/scripts/unit-script.py' with u=unit %}
{% endif %}

