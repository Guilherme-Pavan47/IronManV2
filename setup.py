from cx_Freeze import setup, Executable

setup(
    name="GTA SAN ANDREAS",
    version="1.0",
    description="JOGO GTA SAN ANDREAS",
    executables=[Executable("main.py", base="gui")]
)