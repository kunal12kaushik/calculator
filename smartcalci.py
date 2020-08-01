from cx_Freeze import *

includefiles = ['cal.ico']
base = None
if sys.platform == "win32":
    base = "win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "my calculator",
     "TARGETDIR",
     "[TARGETDIR]\smartcalci.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data', msi_data}

setup(
    version="0.1",
    description = "my calculator",
    author = "Kunal Kaushik",
    options = {'build_exe': {'include_files':includefiles}, "bdist_msi": bdist_msi_options, },
    Executable=[
        Executable(
            script="smartcalci.py",
            base=base,
            icon= 'cal.ico',
        )
    ]
)