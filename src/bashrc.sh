
function smart_build()
{


    if [ -z "$1" ]
    then
        echo "SMART BUILD!!!"
        START=$(date +%s);
        project_type=$(p2 $SMART_BUILD_TOOLS_DIR/detect_project.py)

        $SMART_BUILD_TOOLS_DIR/$project_type/smart_build_$project_type.sh $1

        END=$(date +%s);
        echo $((END-START)) | awk '{print int($1/60)":"int($1%60)}'
    else
        echo "Smart Build Tool - version 0.0.1"
        echo "Usage: go to a project directory and enter: \$ b"
    fi


}
alias b="smart_build"