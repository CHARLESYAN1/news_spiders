"""
This module is suitable for the transfer files between machine, win is local, linux is remote
mainly operate to push file from win to linux, But this operation method is a bit awkward
"""
import paramiko

from .base import Base, logger


class SmoothTransfer(Base):
    """
    Use paramiko module require three packages
    1:windows to linux, as follow blew:
        `MinGW`: windows system , add 'xx\MinGW\bin' to os path
        `PyCrypto`: install pycrypto, before install paramiko
        `paramiko`: install
        Note: if only `Authentication failed` Error, maybe `username` or `passwd` is incorrect.
    2:linux to linux: paramiko and pexpect packages
        details can reference the related document with Internet.
    """
    only_instance_attr = 'sftp'

    def __init__(self, host=None, port=22, user=None, password=None):
        super(SmoothTransfer, self).__init__()

        self.host = host or self.inner_host
        self.port = port or self.inner_port
        self.user = user or self.inner_user
        self.pwd = password or self.inner_pwd

        setattr(self, self.only_instance_attr, self.sftp_client)

    def ssh_command(self, cmds, echo=False):
        commands = cmds if isinstance(cmds, (tuple, list)) else [cmds]

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.host, self.port, self.user, self.pwd, timeout=30)

            for cmd in commands:
                stdin, stdout, stderr = client.exec_command(cmd)
                if echo:
                    logger.info('Cmd <{}>: stdout: {}'.format(cmd, '\t'.join([f for f in stdout])))
        except Exception as e:
            logger.info('Run error: cmd <{}>, type <{}>, info <{}>'.format(cmd, e.__class__, e))
        finally:
            client.close()

    @property
    def sftp_client(self):
        sock = (self.host, self.port)
        t = paramiko.Transport(sock=sock)
        t.connect(username=self.user, password=self.pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        return sftp

    def put(self, local_path, remote_path):
        """
        Notice that use only one sftp object to transfer file when have many files, else
        raise <socket.error [1024] too many open files > error, finally close sftp object

        :param local_path: Absolutely local path. eg: /data/news/csf_news/abc.txt
        :param remote_path: Absolutely server path. eg: /home/daily_news/scf_news/abc.txt
        """
        try:
            sftp = self.__dict__[self.only_instance_attr]
            sftp.put(local_path, remote_path)
        except Exception as e:
            logger.info('Put file error: type <{}>, info <{}>'.format(e.__class__, e))

    def get(self, local_path, remote_path):
        """ Docstring description is the same `put` method """
        try:
            sftp = self.__dict__[self.only_instance_attr]
            sftp.get(local_path, remote_path)
            sftp.close()
        except Exception as e:
            logger.info('Get file error: type <{}>, info <{}>'.format(e.__class__, e))

    def close(self):
        sftp = self.__dict__.get(self.only_instance_attr)
        if sftp is not None:
            sftp.close()

