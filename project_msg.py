import pyfiglet #type:ignore
import cowsay #type:ignore

def figlet_msg(msg):
    fam_msg=pyfiglet.figlet_format(msg)
    return fam_msg
    ...
def cowsay_msg_cow(msg):
    fam_msg=cowsay.cow(msg)
    return fam_msg
    ...
def cowsay_msg_ghost(msg):
    fam_msg=cowsay.ghostbusters(msg)
    return fam_msg
    ...

def cowsay_msg_tux(msg):
    fam_msg=cowsay.tux(msg)
    return fam_msg