echo "Latex project detected"

DEFAULT_BUILD_FILE=build.sh

if test -f "${DEFAULT_BUILD_FILE}"; then
    echo "Let's run: "${DEFAULT_BUILD_FILE}
    ./${DEFAULT_BUILD_FILE}
elif test -f "Makefile"; then
    echo "Let's run from Makefile "
    make
else
    target_file=$1

    latex_build_cmd=$(python2 $SMART_BUILD_TOOLS_DIR/latex/build_latex_project.py $target_file)

    echo "Let's run: "${latex_build_cmd}

    exec ${latex_build_cmd}
fi
