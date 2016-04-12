import sys
import linecache


class NotExistFileError(Exception):
    pass


class NotExistSiteError(Exception):
    pass


def get_exce_info():
    exc_type, exc_value, tb = sys.exc_info()
    frame = tb.tb_frame
    lineno = tb.tb_lineno
    filename = frame.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, frame.f_globals)
    return 'Type: [{type}], Info: [{value}], Path: [{file_path}], LineNo: [{lineno}]'.format(
        type=exc_type,
        value=line.strip(),
        file_path=filename,
        lineno=lineno
    )
