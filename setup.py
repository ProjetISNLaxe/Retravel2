from cx_Freeze import setup, Executable
setup(
    name="Retravel",
    version="1.0",
    description="Retravel",
    executables=[Executable(script="launcher.py", icon="icone.ico", base="Win32GUI",)])
