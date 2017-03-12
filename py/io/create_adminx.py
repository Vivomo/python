from py.utils import IO_util

appsPath = r'G:\code\MxOnline\apps'
models = filter(lambda path: path.endswith('models.py'), IO_util.get_all_file(appsPath))

