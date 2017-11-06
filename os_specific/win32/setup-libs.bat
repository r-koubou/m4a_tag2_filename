@echo off

pushd ..\..\

call venv\Scripts\activate.bat
pip install -r os_specific\win32\requirements.txt

popd
