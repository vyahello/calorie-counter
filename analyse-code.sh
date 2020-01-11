#!/usr/bin/env bash

PACKAGE="counter"


--check-box() {
    :<<DOC
    Provides pretty-printer check box
DOC
    printf "Start ${1} analysis ...\n"
}


remove-pycache() {
    :<<DOC
    Removes python cache directories
DOC
    ( find . -d -name __pycache__ | xargs rm -r )
}


check-black() {
    :<<DOC
    Runs `black` code analyser
DOC
    --check-box "black" && ( black --check ${PACKAGE} )
}


check-mypy() {
    :<<DOC
    Runs `mypy` code analyser
DOC
    --check-box "mypy" && ( mypy --package "${PACKAGE}" )
}


check-unittests() {
    :<<DOC
    Runs unittests using `pytest` framework
DOC
    --check-box "unitests" && pytest
}


main() {
    :<<DOC
    Runs main code analyser
DOC
    remove-pycache
    check-black && check-mypy && check-unittests
}


main