import os
import re

from py.utils import IO_util
from py.translate import line

newWordsPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\temp\new_words.txt'
fileNameReg = re.compile(r'f=(\w+)')
wordReg = re.compile(r'(l_\w+)\|(.+?)\|(.+)')
assignReg = re.compile(r'<#assign')
enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
zhPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'


def get_words_dict(file_path, check_path=''):
    chinese = []
    if check_path != '':
        with open(check_path, 'r', encoding='utf-8') as check_file:
            for l in check_file.readlines():
                if line.EnglishExp.match(l):
                    chinese.append(line.Line(l).ch)

    with open(file_path, 'r', encoding='utf-8') as f:
        words_dict = {}
        file_name = ''
        for l in f.readlines():
            result = re.search(fileNameReg, l)
            if result:
                file_name = result.groups()[0]
                words_dict[file_name] = {
                    "zh": [],
                    "en": []
                }
            else:
                result = re.search(wordReg, l)
                if result is None:
                    print(l)
                    continue
                groups = result.groups()
                ch = groups[2]
                if result and file_name in words_dict and ch not in chinese:
                    words_dict[file_name]['zh'].append("%s = '%s'" % (groups[0], ch))
                    words_dict[file_name]['en'].append("%s = '%s'<#--%s-->" % (groups[0], groups[1], ch))
    return words_dict


def write_word_dict(word_dict):
    for k, v in word_dict.items():
        assign_index = -1
        language_path = [os.path.join(enPath, 'l_%s.ftl' % k), os.path.join(zhPath, 'l_%s.ftl' % k)]
        key_arr = ['en', 'zh']
        for j, path in enumerate(language_path):
            with open(path, 'r', encoding='utf-8') as f:
                readlines = f.readlines()
                for i, l in enumerate(readlines):
                    if re.search(assignReg, l):
                        assign_index = i + 1
                        break
            if assign_index != -1:
                write_content = ''.join(readlines[:assign_index] +
                                        ['\n'.join(v[key_arr[j]]) + '\n'] +
                                        readlines[assign_index:])
                IO_util.write_to_file(path, write_content)

wordDict = get_words_dict(newWordsPath)
write_word_dict(wordDict)
