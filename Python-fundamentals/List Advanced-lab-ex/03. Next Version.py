version = input().split(".")
version_1 = "".join(version)
needed_version = int(version_1) + 1
needed_version_as_needed = str(needed_version)
print(f"{needed_version_as_needed[0]}.{needed_version_as_needed[1]}.{needed_version_as_needed[2]}")


