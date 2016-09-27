#!/usr/bin/env bash

SMALL_INPUT_ONLY=0

for arg in "$@"
do
    case $arg in
        -s|--small-input-only)
            SMALL_INPUT_ONLY=1
            shift
            ;;

        *)
            ;;
    esac
done

if [ ${SMALL_INPUT_ONLY} -eq 1 ]
then
    input_files=$(ls samples/input0[0135678].txt)
else
    input_files=$(ls samples/input??.txt)
fi

for prog in $(ls euler148?.py)
do
    echo
    echo "Testing ${prog}"

    for sample in ${input_files}
    do
        echo "=> Sample: ${sample}"

        expected=${sample/input/output}

        ./${prog} < $sample | cmp --silent - ${expected}
        if [ ${PIPESTATUS[1]} -eq 0 ]
        then
            echo "  OK"
        else
            echo "  *** FAIL ***"
        fi
    done
done
