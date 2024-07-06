## hello_pyinstaller-project setup!

Run these commands to get started quickly: <br/>

    $> cd .\hello_pyinstaller\
    $> py -m venv .venv
    $> .\.venv\Scripts\activate

Optionally upgrade pip package manager: <br/>

    $> python.exe -m pip install --upgrade pip

Install all the dependencies: <br/>

    $> python -m pip install -r requirements.txt


### Install Hello_PyInstaller as a Local Package

Navigate to the src directory and install your local package: <br/>

    (.venv)$> cd src/
    (.venv)$> python -m pip install .

Run the program: <br/>

    (.venv)$> python hello_pyinstaller


### Build Executable file using PyInstaller for Windows 11

    $> pip install pyinstaller
    $> pyinstaller .\src\hello_pyinstaller\__main__.py --onefile --name "HelloPyInstaller"
