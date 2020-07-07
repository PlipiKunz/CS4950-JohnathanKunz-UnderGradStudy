import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame","HitBox", "DoorWay", "GameCharacter", "GameObject","GameSprites", "Room", "RoomObjectWrapper"],
                           "include_files":["Images", "Characters", "Images", "Objects", "Rooms"] }},
    executables = executables

    )