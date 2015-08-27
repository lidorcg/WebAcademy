import os
{% if course %}
{% include 'whitenapp/scripts/course-script.py' with c=course %}
{% elif module %}
{% include 'whitenapp/scripts/module-script.py' with m=module %}
{% elif lesson %}
{% include 'whitenapp/scripts/module-script.py' with l=lesson %}
{% elif unit %}
{% include 'whitenapp/scripts/module-script.py' with u=unit %}
{% endif %}