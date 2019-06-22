import os

# Verify Unity project
current_dir = os.getcwd()


def is_android_project():
    return os.path.exists(os.path.join(current_dir, "gradlew"))


def is_unity_project():
    return os.path.exists(current_dir + "/Assets") and os.path.exists(current_dir + "/ProjectSettings")


def is_latex_project():
    files = os.listdir(current_dir)

    latex_count = 0

    for name in files:
        if name.endswith(".tex") or name.endswith(".bib"):
            latex_count += 1
    return latex_count >= 1


if __name__ == "__main__":
    if is_unity_project():
        print("unity")
    elif is_latex_project():
        print("latex")
    elif is_android_project():
        print("android")
    else:
        print("undefined")
