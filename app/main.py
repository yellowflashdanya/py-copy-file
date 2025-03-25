def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command!")
        return

    src, dest = parts[1], parts[2]

    if src == dest:
        print("It is impossible to copy yourself.")
        return

    try:
        with open(src, "r") as f_src, open(dest, "w") as f_dest:
            f_dest.write(f_src.read())
    except Exception as e:
        print(f"Copy error: {e}")
