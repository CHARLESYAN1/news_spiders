import sys

from ...utils import Logger

if sys.platform[:3].lower() == 'lin':
    # between Linux machine
    import pexpect as transfer
else:
    # Linux machine is remote, Win islocal
    import paramiko as transfer

logger = Logger('transfer')
