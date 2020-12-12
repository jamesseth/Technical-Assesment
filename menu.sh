#!/bin/bash

PS3="Select the operation: "

SENTENCE=""
EXIT=false
DIR="./.venv"
if [ -d "$DIR" ]; then
    echo "Creating virtual environment: ${DIR}..."
    python3 -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt


while ! $EXIT; do
    # clear
    echo "current sentence: ${SENTENCE}"
    select opt in sentence replace quit; do
        
        case $opt in
            sentence)
                clear
                read -p "Enter a sentence: " user_sentence
                SENTENCE=${user_sentence}
                break
            ;;
            replace)
                clear
                SENTENCE=$(python3 src/user_input.py "${SENTENCE}")
                break
            ;;
            quit)
                clear
                deactivate
                exit
                break
            ;;
            *)
                echo "Invalid option $REPLY"
                break
            ;;
        esac
    done
done