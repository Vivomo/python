import re
from py.translate.line import Line
from py.utils import IO_util

globalVarFilePath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en\l_global.ftl'
chineseReg = u"[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+"
langNameExp = r'lang_name\s?=\s?[\'\"](\w+)[\'\"]'
langModePath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en\l_%s.ftl'


def get_file_line(file_path):
    line_arr = []
    if file_path is None:
        return line_arr
    with open(file_path, 'r', encoding='utf-8') as file:
        for l in file.readlines():
            line = Line(l)
            if line.is_legal():
                line_arr.append(line)
    return line_arr


def get_lang_path(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        read_content = file.read()
        lang_name_match = re.search(langNameExp, read_content)
        if lang_name_match:
            return langModePath % lang_name_match.groups()[0]
    return None


def replace_chinese(file_path):
    lang_path = get_lang_path(file_path)
    file_var = get_file_line(lang_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        result = re.sub(chineseReg, lambda ch: get_var(ch.group(), file_var, file_path), content)
    IO_util.write_to_file(file_path, result)


def get_var(chinese, lines, file_path=''):
    for line in lines:
        if line.ch == chinese:
            return '${%s}' % line.name
    for line in globalVar:
        if line.ch == chinese:
            return '${%s}' % line.name
    print('Not found %s of %s' % (chinese, file_path))
    return chinese


globalVar = get_file_line(globalVarFilePath)
fileList = [r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default\recruit_job_view.ftl',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default\recruit_jobs.ftl',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\saishi\recruit_job_view.ftl',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\saishi\recruit_jobs.ftl',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default\recruit_job_view.ftl',
            r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default\recruit_jobs.ftl']

for f in fileList:
    replace_chinese(f)
