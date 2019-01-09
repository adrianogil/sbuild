import os

# Verify Unity project
current_dir = os.getcwd()


def is_unity_project():
    return os.path.exists(current_dir + "/Assets") and os.path.exists(current_dir + "/ProjectSettings")


if is_unity_project():
    print("unity")
else:
    print("undefined")
