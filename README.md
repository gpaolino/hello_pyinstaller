hello_pyinstaller-project setup!

Run these commands to get started quickly:
  $> cd .\hello_pyinstaller\
  $> py -m venv .venv
  $> .\.venv\Scripts\activate

Optionally upgrade pip package manager: $> python.exe -m pip install --upgrade pip

  $> python -m pip install -r requirements.txt


Install Hello_PyInstaller as a Local Package

Navigate to the src directory and install your local package:
  (.venv)$> cd src/
  (.venv)$> python -m pip install .

Run the program:
  (.venv)$> python hello_pyinstaller


Build Executable file using PyInstaller for Windows 11

  $> pip install pyinstaller
  $> pyinstaller .\src\hello_pyinstaller\__main__.py --onefile --name "HelloPyInstaller"
