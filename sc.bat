set /p in_path="path:"
if not exist "%in_path%"(
echo error:path not exist.
exit /b 1
)

set venv_dir="%in_path%\venv"
if not exist "%venv_dir"(
	python -m venv "%venv_dir%"
)
call %venv_dir%\Scripts\activate.bat

pyrcc6 resources.qrc -o resources.py

echo py file created.

