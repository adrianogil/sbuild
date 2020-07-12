import sys


def create_latex_build_file(tex_file, bib_file):
    build_file = """

target_tex=TEX_FILE
target_bib=BIB_FILE

pdflatex -interaction nonstopmode -halt-on-error -file-line-error  ${target_tex}
bibtex ${target_bib}
pdflatex -interaction nonstopmode -halt-on-error -file-line-error ${target_tex}
bibtex ${target_bib}
pdflatex -interaction nonstopmode -halt-on-error -file-line-error ${target_tex}
bibtex ${target_bib}
pdflatex -interaction nonstopmode -halt-on-error -file-line-error ${target_tex}

""".replace("TEX_FILE", tex_file).replace("BIB_FILE", bib_file)

    with open("build.sh", "w") as target_file:
        target_file.write(build_file)


def create_build_file(args):
    if args[0].endswith(".tex"):
        create_latex_build_file(*args)


if __name__ == '__main__':
    args = sys.argv[1:]
    create_build_file(args)
