import sys

if sys.platform[:3].lower() == 'lin':
    # between Linux machine
    import pexpect as transfer
else:
    # Linux machine is remote, Win islocal
    import paramiko as transfer
