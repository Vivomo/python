import os
import re

from py.utils import IO_util

newWordsPath = r'../../src/new_words.txt'
fileNameReg = re.compile(r'f=(\w+)')
wordReg = re.compile(r'(l_\w+)\|(.+?)\|(.+?)')
assignReg = re.compile(r'<#assign')
enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
zhPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'


def get_words_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words_dict = {}
        file_name = ''
        for line in f.readlines():
            result = re.search(fileNameReg, line)
            if result:
                file_name = result.groups()[0]
                words_dict[file_name] = {
                    "zh": [],
                    "en": []
                }
            else:
                result = re.search(wordReg, line)
                groups = result.groups()
                if result and file_name in words_dict:
                    words_dict[file_name]['zh'].append("%s = '%s'" % (groups[0], groups[2]))
                    words_dict[file_name]['en'].append("%s = '%s'<#--%s-->" % (groups[0], groups[1], groups[2]))
    return words_dict


def write_word_dict(word_dict):
    for k, v in word_dict.items():
        assign_index = -1
        language_path = [os.path.join(enPath, 'l_%s.ftl' % k), os.path.join(zhPath, 'l_%s.ftl' % k)]
        key_arr = ['en', 'zh']
        for j, path in enumerate(language_path):
            with open(path, 'r', encoding='utf-8') as f:
                readlines = f.readlines()
                for i, line in enumerate(readlines):
                    if re.search(assignReg, line):
                        assign_index = i + 1
                        break
            if assign_index != -1:
                write_content = ''.join(readlines[:assign_index] +
                                        ['\n'.join(v[key_arr[j]]) + '\n'] +
                                        readlines[assign_index:])
                IO_util.write_to_file(path, write_content)

wordDict = get_words_dict(newWordsPath)
write_word_dict(wordDict)
