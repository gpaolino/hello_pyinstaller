from setuptools import setup

setup(
      name='hello_pyinstaller',
      version='1.0',
      description='Hello PyInstaller Test App',
      author='Paolo Guglielmino',
      author_email='gp.guglielminopaolo@gmail.com',
      packages=["hello_pyinstaller"],
      entry_points={
          "console_scripts": ["hello_pyinstaller=hello_pyinstaller:main"],
      },
)