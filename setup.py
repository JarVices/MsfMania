import subprocess
import time
from lib import core

def main():
	
	print(core.MMCOLORS.OCRA + core.MMCOLORS.BOLD + "[*] Updating system." + core.MMCOLORS.ENDC)
	subprocess.run(["apt", "update"])
	subprocess.run(["apt", "-y", "full-upgrade"])
	subprocess.run(["apt", "-y", "autoremove"])
	subprocess.run(["apt", "update"])
	subprocess.run(["apt", "-y", "full-upgrade"])
	subprocess.run(["apt", "-y", "autoremove"])
	core.CLEAR()
	print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] System updated." + core.MMCOLORS.ENDC)

	time.sleep(5)

	print(core.MMCOLORS.OCRA + core.MMCOLORS.BOLD + "[*] Installing Gnome-terminal." + core.MMCOLORS.ENDC)
	subprocess.run(["apt", "-y", "install", "gnome-terminal"])
	core.CLEAR()
	print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] Gnome-terminal installed." + core.MMCOLORS.ENDC)

	time.sleep(5)

	print(core.MMCOLORS.OCRA + core.MMCOLORS.BOLD + "[*] Installing MinGW." + core.MMCOLORS.ENDC)
	subprocess.run(["apt", "-y", "install", "mingw-w64*"])
	core.CLEAR()
	print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] MinGW installed." + core.MMCOLORS.ENDC)
	print(core.MMCOLORS.OCRA + core.MMCOLORS.BOLD + "[*] Making GCC WINDRES link." + core.MMCOLORS.ENDC)
	subprocess.run(["ln", "-s", "/usr/bin/x86_64-w64-mingw32-windres", "/usr/bin/windres"])
	subprocess.run(["ln", "-s", "/usr/bin/i686-w64-mingw32-windres", "/usr/bin/windres_1"])
	print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] GCC WINDRES link created." + core.MMCOLORS.ENDC)

	time.sleep(5)

	print(core.MMCOLORS.OCRA + core.MMCOLORS.BOLD + "[*] Installing RAR." + core.MMCOLORS.ENDC)
	subprocess.run(["apt", "-y", "install", "rar"])
	core.CLEAR()
	print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] RAR installed.\n" + core.MMCOLORS.ENDC)

	print(print(core.MMCOLORS.GREEN + core.MMCOLORS.BOLD + "[+] MsfMania is ready :) ." + core.MMCOLORS.ENDC))

main()


