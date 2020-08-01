from cx_Freeze import *

includefiles = ['calce.ico']
base = None
if sys.platform == "Win-amd64-3.8":
    base = "win64GUI"

shortcut_table = [
    ("DesktopShortcut", #shortcut
     "DesktopFolder", #dictionary
     "my calculator", #name
     "TARGETDIR", #COMPONENT
     "[TARGETDIR]\kunal.exe",   #target
     None,  #argument
     None,  #descriton
     None,  #hotkey
     None,  #icon
     None,  #icnindex
     None,  #showcmd
     "TARGETDIR", #WKDIR
      )
]

msi_data = {"Shortccut": shortcut_table}
#some default msi options anmd specify the use of the defined table
bdist_msi_options = {'data': msi_data}
setup(
    version = "3.8",
    description ="kunal",
    author = "Kunal Kaushik",
    name = "my calculator",
    options = {'build.exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options,},
    executables = [
        Executable(
            script="kunal.py",
            base=base,
            icon='calce.ico',
        )
    ]

)