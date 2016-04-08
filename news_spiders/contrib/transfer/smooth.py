"""
This module is suitable for the transfer files between machine, win is local, linux is remote
mainly operate to push file from win to linux, But this operation method is a bit awkward
"""
import paramiko

from .base import Base, logger


def cache_decorator(method):
    def decorator(*args, **kwargs):
        self = args[0]
        if not self.__dict__.get(self.only_instance_attr):
            self.__dict__[self.only_instance_attr] = getattr(self, self.only_instance_attr)
        return method(*args, **kwargs)
    return decorator


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

        self._host = host or self.inner_host
        self._port = port or self.inner_port
        self._user = user or self.inner_user
        self._pwd = password or self.inner_pwd

    def ssh_command(self, cmd, echo=False):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self._host, self._port, self._user, self._pwd, timeout=10)

            stdin, stdout, stderr = client.exec_command(cmd)
            if echo:
                logger.info('Cmd <{}>: stdout: {}'.format(cmd, '\t'.join([f for f in stdout])))
        except Exception as e:
            logger.info('Run error: cmd <{}>, type <{}>, info <{}>'.format(cmd, e.__class__, e))
        finally:
            client.close()

    @property
    def sftp(self):
        sock = (self._host, self._port)
        t = paramiko.Transport(sock=sock)
        t.connect(username=self._user, password=self._pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        return sftp

    @cache_decorator
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

    @cache_decorator
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
