if not os.path.exists("U{{ u.order }}-{{ u.name }}"):
    os.mkdir("U{{ u.order }}-{{ u.name }}")
os.chdir("U{{ u.order }}-{{ u.name }}")
# ToDo Download the relevant content
os.chdir("..")