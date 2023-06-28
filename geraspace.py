import cx_Freeze

executables = [
    cx_Freeze.Executable(script="spacemarker.py", icon="space.ico")
]

cx_Freeze.setup(
    name="SpaceMarker",
    options={
        "build_exe": {
            "packages": ["pygame", "tkinter", "pickle", "math"],
            "include_files": [
                "bg.jpg",
                "space.png",
                "Space_Machine_Power.mp3"
                "space-0.png"
                "space.ico"
            ]
        }
    },
    executables=executables
)

# python geraSetup.py build
# python geraSetup.py bdist_msi