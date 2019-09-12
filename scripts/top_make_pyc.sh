#!/bin/bash

python3.7 -m compileall .

for d in *; do
	if [ -d "$d" ]; then
		( cd "$d" && cd __pycache__ && rename  's/\.cpython-37//' *.pyc && mv ./*.pyc ../ && cd .. && rm -rf ./*.py && rm -rf ./__pycache__)
	fi
done

for d in *; do
        if [ -d "$d" ]; then
                ( cd "$d" && chmod +x ./sub_make_pyc.sh && ./sub_make_pyc.sh)
        fi
done


