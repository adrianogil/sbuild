echo "Latex project detected"

target_file=$1

latex_build_cmd=$(python2 $SMART_BUILD_TOOLS_DIR/latex/build_latex_project.py $target_file)

echo "Let's run: "${latex_build_cmd}

exec ${latex_build_cmd}