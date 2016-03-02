import os.path


class GenConfigsPath(object):
    @staticmethod
    def _conf_path(filename):
        return os.path.join(os.path.dirname(__file__), filename).replace('\\', '/')

    def gen_aws_path(self):
        return self._conf_path('aws.conf')

    def gen_scheduler_path(self):
        return self._conf_path('sched.conf')


__gen_instance = GenConfigsPath()
aws_path = __gen_instance.gen_aws_path()
sched_path = __gen_instance.gen_scheduler_path()
