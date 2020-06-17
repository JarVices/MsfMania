from lib import core
import subprocess, os


def rar(filename):
    os.chdir("output/")

    archive = filename.replace('.exe', '.rar')
    archive = archive.replace('output/', '')

    filename = filename.replace('output/', '')

    compress = ['rar', 'a', '-m5', archive, filename]
    subprocess.run(compress, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

    core.rar_compressed()
