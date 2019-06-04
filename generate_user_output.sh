#!/usr/bin/env bash

OUTPUT="$1"
if [ -z "$OUTPUT" ]
then
	echo "Please set what data to generate, use --help for help"

else
    if [ "$OUTPUT" == "--help" ] || [ "$OUTPUT" == "-h" ]
    then
        echo "Generates correct --correct (-c) or --incorrect (-i) data to test user's output"
    fi
    if [ "$OUTPUT" == "--correct" ] || [ "$OUTPUT" == "-c" ]
    then
        python $PWD/solutions/student_A/correct_solution.py > user_output.txt
    fi

    if [ "$OUTPUT" == "--incorrect" ] || [ "$OUTPUT" == "-i" ]
    then
        python $PWD/solutions/student_A/incorrect_solution.py > user_output.txt
    fi

fi
