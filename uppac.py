print("uppac by Technochips")

import os

is_root = (os.geteuid() == 0)

UPDATE_BEFORE = "Upgrading "
UPDATE_AFTER = "..."
SKIP_BEFORE = "Skipping "
SKIP_AFTER = "..."
SKIP_NOTROOT = "Reason: You need root privileges."
SKIP_DOESNTEXIST = "Reason: Doesn't exists."

if os.path.exists("/bin/apt") or os.path.exists("/usr/bin/apt"):
    if is_root:
        print(UPDATE_BEFORE + "apt" + UPDATE_AFTER)
        os.system("apt update -y")
        os.system("apt upgrade -y")
        os.system("apt auto-remove -y")
    else:
        print(SKIP_BEFORE + "apt" + SKIP_AFTER)
        print(SKIP_NOTROOT)
else:
    print(SKIP_BEFORE + "apt" + SKIP_AFTER)
    print(SKIP_DOESNTEXIST)

if os.path.exists("/bin/pacman") or os.path.exists("/usr/bin/pacman"):
    if is_root:
        print(UPDATE_BEFORE + "pacman" + UPDATE_AFTER)
        os.system("pacman -Syu")
    else:
        print(SKIP_BEFORE + "pacman" + SKIP_AFTER)
        print(SKIP_NOTROOT)
else:
    print(SKIP_BEFORE + "pacman" + SKIP_AFTER)
    print(SKIP_DOESNTEXIST)
