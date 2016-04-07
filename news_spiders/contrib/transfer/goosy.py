"""
This module is suitable for the transfer files between Linux machine,
mainly use the SCP command to operate, But this operation method is a bit awkward
"""
from os.path import abspath as _abs

from .base import transfer, logger
from ...conf import news_config


class Base(object):
    def __init__(self):
        self.config = news_config.settings

    @property
    def host(self):
        return self.config['ANALYSIS_SERVER_INNER_IP']

    @property
    def pwd(self):
        return self.config['ANALYSIS_SERVER_PASSWORD']


class GoosyTransfer(Base):
    def __init__(self, host=None, password=None):
        super(GoosyTransfer, self).__init__()
        self._host = host or self.host
        self._password = password or self.pwd

    def ssh_command(self, cmd):
        ssh = transfer.spawn('ssh root@%s "%s"' % (self._host, cmd))

        try:
            i = ssh.expect(['password:', 'continue connecting(yes/no)?'], timeout=5)
            if i == 0:
                ssh.sendline(self._password)
            elif i == 1:
                ssh.sendline('yes\n')
                ssh.expect('password:')
                ssh.sendline(self._password)
            ssh.sendline(cmd)
            r = ssh.read()
            ret = 0
        except transfer.EOF as e:
            ret = -1
            logger.info('Run ssh command error: cmd <{}>, type <{}>, msg <{}>, file <{}>'.format(
                cmd, e.__class__, e, _abs(__file__)))
        except transfer.TIMEOUT as e:
            ret = -2
            logger.info('Run ssh command error: cmd <{}>, type <{}>, msg <{}>, file <{}>'.format(
                cmd, e.__class__, e, _abs(__file__)))
        finally:
            ssh.close()
        return ret

    def put(self, local, remote):
        """
        Make local file push remote path
        :param local: local machine absolutely file path
        :param remote: remote machine absolutely directory path
        """
        self.ssh_command('mkdir -p %s' % remote)
        child = transfer.spawn('scp %s root@%s:%s' % (local, self._host,  remote))

        try:
            while True:
                index = child.expect(["root@%s's password:" % self._host, transfer.TIMEOUT])

                if index == 0:
                    child.sendline('%s\n' % self._password)
                    break
                elif index == 1:
                    pass
        except (transfer.EOF, transfer.TIMEOUT) as e:
            logger.info('Transfer file error: type <{}>, msg <{}>, file <{}>'.format(e.__class__, e,_abs(__file__)))
        finally:
            child.interact()
            child.close()
