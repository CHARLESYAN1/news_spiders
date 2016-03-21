"""
This module is suitable for the transfer files between machine, win is local, linux is remote
mainly operate to push file from win to linux, But this operation method is a bit awkward
"""

from .base import transfer


class WinTransfer(object):
    """ This class is suitable for pushing files from win machine to linux machine """
    def __init__(self, ssh_host, ssh_user, ssh_pwd, ssh_port=22):
        self.__host = ssh_host
        self.__user = ssh_user
        self.__pwd = ssh_pwd
        self.__port = ssh_port
        self.__client = None
        self.__conn = None
        self.__sftp = None

    def __cmd_connect(self):
        if self.__conn is not None:
            self.__conn.close()
            self.__conn = None

        try:
            self.__conn = transfer.SSHClient()
            self.__conn.set_missing_host_key_policy(transfer.AutoAddPolicy())
            self.__conn.connect(self.__host, self.__port, self.__user, self.__pwd)
        except Exception as e:
            raise e.__class__('Connect error: %s'.format(e))
        return self.__conn

    def __client_connect(self):
        if self.__client is not None:
            self.__client.close()

        try:
            self.__client = transfer.Transport((self.__host, self.__port))
            self.__client.connect(username=self.__user, password=self.__pwd)
            self.__sftp = transfer.SFTPClient.from_transport(self.__client)
        except Exception as e:
            raise e.__class__('Client connect error: %s'.format(e))
        return self.__sftp

    def exec_command(self, command):
        ssh = self.__cmd_connect()
        stdin, stdout, stderr = ssh.exec_command(command)
        out = stdout.readlines()
        err = stderr.readlines()
        self.disconnect()

    def put(self, local_path, remote_path, disc_key=True):
        """
        :param local_path: Absolutely local path. eg: abc.txt
        :param remote_path: Absolutely server path. eg: /home/daily_news/scf_news/abc.txt
        :param disc_key: bool
        """
        if self.__sftp is None:
            self.__sftp = self.__client_connect()
        self.__sftp.put(local_path, remote_path)
        if disc_key:
            self.disconnect()

    def get(self, local_path, remote_path, disc_key=True):
        if self.__sftp is None:
            self.__sftp = self.__client_connect()
        self.__sftp.get(remote_path, local_path)
        if disc_key:
            self.disconnect()

    def disconnect(self):
        if self.__conn is not None:
            self.__conn.close()
            self.__conn = None

        if self.__client is not None:
            self.__client.close()
            self.__client = None
