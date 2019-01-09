
function smart_build()
{
    project_type=$(p2 $SMART_BUILD_TOOLS_DIR/detect_project.py)
    $SMART_BUILD_TOOLS_DIR/$project_type/smart_build_$project_type.sh $1
}
alias b="smart_build"