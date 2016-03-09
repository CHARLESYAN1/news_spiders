import os.path


class GenConfigsPath(object):
    @staticmethod
    def _conf_path(filename):
        return os.path.join(os.path.dirname(__file__), filename).replace('\\', '/')

    @property
    def aws_path(self):
        return self._conf_path('aws.conf')

    @property
    def scheduler_path(self):
        return self._conf_path('sched.conf')

    @property
    def module_path(self):
        return self._conf_path('module.conf')


__gen_instance = GenConfigsPath()
aws_path = __gen_instance.aws_path
sched_path = __gen_instance.scheduler_path
module_path = __gen_instance.module_path
