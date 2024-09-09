#!/bin/bash

set -e
errors=0

# Run unit tests
python AGI_demo/AGI_demo_test.py || {
    echo "'python python/AGI_demo/AGI_demo_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E AGI_demo/*.py || {
    echo 'pylint -E AGI_demo/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
