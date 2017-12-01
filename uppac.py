print("uppac by Technochips")

import os

if os.path.exists("/bin/apt") or os.path.exists("/usr/bin/apt"):
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt auto-remove -y")

if os.path.exists("/bin/pacman") or os.path.exists("/usr/bin/pacman"):
    os.system("pacman -Syu")
