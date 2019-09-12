#!/bin/bash

for d in *; do
	if [ -d "$d" ]; then
		( cd "$d" && cd __pycache__ && rename  's/\.cpython-37//' *.pyc && mv ./*.pyc ../ && cd .. && rm -rf ./*.py && rm -rf ./__pycache__)
	fi
done


