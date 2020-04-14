from lib import core
import subprocess, os


def RAR(FILENAME):
    core.RAR_COMPRESSION()

    CR = core.CORE_INPUT()

    if CR == "1":

        pass

    elif CR == "2":

        core.RAR_COMPRESSING()

        os.chdir("output/")

        ARCHIVE = FILENAME.replace('.exe', '.rar')
        ARCHIVE = ARCHIVE.replace('output/', '')

        FILENAME = FILENAME.replace('output/', '')

        COMPRESS = ['rar', 'a', '-m5', ARCHIVE, FILENAME]
        subprocess.run(COMPRESS, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

        core.RAR_COMPRESSED()

    else:
        pass
