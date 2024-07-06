## hello_pyinstaller-project setup!

Run these commands to get started quickly: <br/>

    $> cd .\hello_pyinstaller\ <br/>
    $> py -m venv .venv <br/>
    $> .\.venv\Scripts\activate <br/>

Optionally upgrade pip package manager: $> python.exe -m pip install --upgrade pip

    $> python -m pip install -r requirements.txt


### Install Hello_PyInstaller as a Local Package

Navigate to the src directory and install your local package: <br/>

    (.venv)$> cd src/ <br/>
    (.venv)$> python -m pip install .

Run the program: <br/>

    (.venv)$> python hello_pyinstaller


### Build Executable file using PyInstaller for Windows 11

    $> pip install pyinstaller <br/>
    $> pyinstaller .\src\hello_pyinstaller\__main__.py --onefile --name "HelloPyInstaller"
