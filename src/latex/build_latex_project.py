import os
import sys
import subprocess
from subprocess import *
import pyperclip


def get_git_root(p):
    """Return None if p is not in a git repo, or the root of the repo if it is"""
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w'), cwd=p) != 0:
        return None
    else:
        root = check_output(["git", "rev-parse", "--show-toplevel"], cwd=p)
        root = root.strip()
        return root

def figure_out_target_file(current_dir):
    target_file = ""

    git_root_path = get_git_root(current_dir)

    get_file_from_git_cmd = 'git log --pretty=format: --name-only -10 | grep ".tex" | head -1'
    get_file_from_git_output = subprocess.check_output(get_file_from_git_cmd, shell=True)
    get_file_from_git_output = get_file_from_git_output.strip()

    target_file = get_file_from_git_output

    target_file = target_file[len(current_dir) - len(git_root_path):]

    return target_file


current_dir = os.getcwd()

if len(sys.argv) > 1:
    target_file = sys.argv[1]
else:
    target_file = figure_out_target_file(current_dir)

print("Let's build latex file: " + target_file)

# latex_files = []
# bib_files = []

# files = os.listdir(current_dir)
# for name in files:
#     if name.endswith(".tex")
#         latex_files.append(name)
#     elif name.endswith(".bib"):
#         bib_files.append(name)

target_file_name = target_file

if target_file.endswith('.tex'):
    target_file_name = target_file[:-4]

latex_cmd = "pdflatex " + target_file_name + ".tex && "
latex_cmd += "bibtex " + target_file_name + " && "
latex_cmd += "pdflatex " + target_file_name + ".tex && "
latex_cmd += "bibtex " + target_file_name + " && "
latex_cmd += "pdflatex " + target_file_name + ".tex && "
latex_cmd += "bibtex " + target_file_name + ""
print(latex_cmd)
latex_output = subprocess.check_output(latex_cmd, shell=True)
latex_output = latex_output.strip()
print(latex_output)

print("Copied to clipboard command to open generated PDF file:")

open_pdf_cmd = "o " + target_file_name + ".pdf"
print(open_pdf_cmd)

pyperclip.copy(open_pdf_cmd)
