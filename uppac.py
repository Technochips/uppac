print("uppac by Technochips")

import os

is_root = (os.geteuid() == 0)

import config

if os.path.exists("/bin/apt") or os.path.exists("/usr/bin/apt"):
    if is_root:
        print(config.UPDATE_BEFORE + "apt" + config.UPDATE_AFTER)
        os.system("apt update -y")
        os.system("apt upgrade -y")
        os.system("apt auto-remove -y")
    else:
        print(config.SKIP_BEFORE + "apt" + config.SKIP_AFTER)
        print(config.SKIP_NOTROOT)
else:
    print(config.SKIP_BEFORE + "apt" + config.SKIP_AFTER)
    print(config.SKIP_DOESNTEXIST)

if os.path.exists("/bin/pacman") or os.path.exists("/usr/bin/pacman"):
    if is_root:
        print(config.UPDATE_BEFORE + "pacman" + config.UPDATE_AFTER)
        os.system("pacman -Syu")
    else:
        print(config.SKIP_BEFORE + "pacman" + config.SKIP_AFTER)
        print(config.SKIP_NOTROOT)
else:
    print(config.SKIP_BEFORE + "pacman" + config.SKIP_AFTER)
    print(config.SKIP_DOESNTEXIST)
