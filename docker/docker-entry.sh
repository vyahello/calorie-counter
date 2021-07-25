#!/bin/bash

IMAGE_REPO="vyahello/calorie-counter"

function help {
:<< DOC
  Shows 'help' message
DOC
  cat <<HELP
  The tool provides a unified executor of calorie-counter application via docker.

  Please use the following commands:
    Please use next command:
      - 'help' to see tool help
         docker run ${IMAGE_REPO}:${IMAGE_VERSION} --help

      - 'counter' to run quotes web application
         docker run -it -p {local-port}:${SERVER_PORT} ${IMAGE_REPO}:${IMAGE_VERSION} counter

HELP
}


counter() {
:<<DOC
    Entrypoint to launch 'counter' web application
DOC
    python -m counter --bind 0.0.0.0:${SERVER_PORT}
}


main() {
:<<DOC
    Launches 'main' tools executor
DOC
    if (
        [[ "$1" == "-h" ]] ||
        [[ "$1" == "--help" ]] ||
        [[ "$1" == "help" ]] ||
        [[ $# -eq 0 ]]
    ); then
        help
        exit 0
    fi
    local cmd=$1; shift
    eval "${cmd} $@"
}


main $@