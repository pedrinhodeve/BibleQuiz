from cx_Freeze import setup, Executable

# Informações do projeto
setup(
    name="BibleQuiz",
    version="1.0.2",
    description="Quiz sobre a bíblia",
    executables=[Executable("biblequiz/app.py", base='Win32GUI')]  # Arquivo principal
)
