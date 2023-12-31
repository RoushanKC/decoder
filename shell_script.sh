#!/bin/bash
read -p "path:" inp_path
if ![-d "$inp_path"]; then
	echo:"error :path does not exist"
	exit 1
fi
venv_dir="$inp_path/venv"
if [! -d "venv_dir"]; then
	python -m venv "venv_dir"
fi
source "$venv_dir/Scripts/activate"
pyrcc6 resource.qrc -o resource.py

echo ".py created!"
