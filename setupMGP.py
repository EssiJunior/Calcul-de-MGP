from cx_Freeze import setup,Executable

setup(
    name = "MGP",
    version = "0.2",
    description = "Calcul de MGP",
    executables = [Executable("MGP.py")]
)