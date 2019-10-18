import subprocess
from lib import core

def main():
	
	print(core.amcolors.OCRA + core.amcolors.BOLD + " [*] Updating system." + core.amcolors.ENDC)
	subprocess.run(["apt", "update"])
	subprocess.run(["apt", "-y", "full-upgrade"])
	subprocess.run(["apt", "-y", "autoremove"])
	subprocess.run(["apt", "update"])
	subprocess.run(["apt", "-y", "full-upgrade"])
	subprocess.run(["apt", "-y", "autoremove"])
	core.Clear()
	print(core.amcolors.GREEN + core.amcolors.BOLD + " [+] System updated." + core.amcolors.ENDC)



	print(core.amcolors.OCRA + core.amcolors.BOLD + " [*] Installing MinGW." + core.amcolors.ENDC)
	subprocess.run(["apt", "-y", "install", "mingw-w64*"])
	core.Clear()
	print(core.amcolors.GREEN + core.amcolors.BOLD + " [+] MinGW installed." + core.amcolors.ENDC)	

	

	print(core.amcolors.OCRA + core.amcolors.BOLD + " [*] Making GCC WINDRES link." + core.amcolors.ENDC)	
	subprocess.run(["ln", "-s", "/usr/bin/x86_64-w64-mingw32-gcc-windres", "/usr/bin/windres"])
	subprocess.run(["ln", "-s", "/usr/bin/i686-w64-mingw32-windres", "/usr/bin/windres_1"])
	print(core.amcolors.GREEN + core.amcolors.BOLD + " [+] GCC WINDRES link created." + core.amcolors.ENDC)

main()


