def write_to_file(name: str, data: str, mode: str = "w") -> None:
    """Writes data to filename."""
    with open(name, mode) as file:
        file.write(data)
