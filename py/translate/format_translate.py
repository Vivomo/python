import os
import re
from py.translate import translate
"""
这里的英文可能是一句话, 可能包含- . '
但英文会被双引号引起来, 所以正则是这样的
"""
EnglishExp = '".+?"'
lineNumExp = r'<#--\d+-->'
commentExp = r'<#--.+?-->'
commentStartToken = '<#--'
commentEndToken = '-->'
# commentMarkExp = r'[<>#-]'
enPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en'
zhPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\zh'
writePathZh = r'E:\git\pythonCode\test\translate\write\zh'
writePathEn = r'E:\git\pythonCode\test\translate\write\en'
prefix = r'l_'
langNameExp = r'lang_name\s?=\s?[\'\"]\w+[\'\"]'
chineseReg = u"[\u4e00-\u9fa5\u3040-\u309f\u30a0-\u30ff]+"
noTranslateCount = 0


class Line(object):
    def __init__(self, line='', translate_result=None):
        self.line = line
        if translate_result:
            self.ch = translate_result['src']
            self.en = translate_result['dst']
            self.name = ('l_' + re.sub(r'\W', '', re.sub(r'\s+', '_', self.en.lower()))).strip()
        else:
            en_arr = re.findall(EnglishExp, line)
            if en_arr:
                self.en = en_arr[0].replace('"', '').strip()
                self.name = ('l_'+re.sub(r'\W', '', re.sub(r'\s+', '_', self.en.lower()))).strip()
            else:
                self.en = ''
                self.name = ''

            comment_arr = re.findall(commentExp, line)
            if comment_arr:
                self.ch = filter_comment(comment_arr[0])
            else:
                self.num = ''
                self.ch = ''

    def __str__(self):
        return '\t[en:%s][ch:%s]' % (self.en, self.ch)

    def is_legal(self):
        return self.name != '' and self.en != '' and self.ch != ''

    def to_en(self):
        if self.is_legal():
            return '%s = "%s" <#--%s-->' % (self.name, self.en, self.ch)
        else:
            return self.line.replace('\n', '')

    def to_ch(self):
        if self.is_legal():
            return '%s = "%s"' % (self.name, self.ch)
        else:
            return self.line.replace('\n', '')


def get_all_file(file_path):
    file_list = []

    for p, d, f in os.walk(file_path):
        for f1 in f:
            file_list.append(os.path.join(p, f1))
    return file_list


def filter_comment(filter_str):
    return filter_str.replace(commentStartToken, '').replace(commentEndToken, '')


def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def format_file(file_path):
    en_lines = []
    zh_lines = []
    file_name = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as read_file:
        for item in read_file.readlines():
            try:
                line = Line(item)
                en_lines.append(line.to_en())
                zh_lines.append(line.to_ch())
            except Exception as e:
                en_lines.append(item)
                zh_lines.append(item)
                print(e)
                print('error file is %s and the content of line is %s' % (file_name, item))

    write_to_file(os.path.join(zhPath, file_name), '\n'.join(zh_lines))
    write_to_file(os.path.join(enPath, file_name), '\n'.join(en_lines))


def format_file2(file_path):
    """
        去重
    """
    word_set = set()
    lines = []
    file_name = os.path.basename(file_path)
    if file_name != 'l_global.ftl' and file_name.find('e') == 0:
        with open(file_path, 'r', encoding='utf-8') as read_file:
            for item in read_file.readlines():
                line = Line(item)
                if line.ch:
                    if line.ch not in word_set:
                        word_set.add(line.ch)
                        lines.append(line.to_en())
                else:
                    lines.append(line.to_en())

        write_to_file(os.path.join(enPath, file_name), '\n'.join(lines))
    return word_set


def translate_file(file_path):
    # if file_path in ignorePath or is_ignore_file(file_path):
    #     return
    global noTranslateCount
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        chinese = list(set(re.findall(chineseReg, content)))
        if chinese:
            chinese.sort(key=len, reverse=True)

            lang_name = get_lang_name(content)
            lang_dict = {}
            if lang_name:
                try:
                    lang_dict = get_lang_name_dict(os.path.join(enPath, 'l_%s.ftl' % lang_name))
                except Exception as e:
                    print(e)
                    print(file_path)
            final_dict = dict(globalDict.items() | lang_dict.items())

            for ch in chinese:
                if ch in final_dict:
                    content = content.replace(ch, '${%s}' % final_dict[ch])
                else:
                    if lang_name in noTranslateDict:
                        noTranslateDict[lang_name].add(ch)
                    else:
                        if lang_name:
                            noTranslateDict[lang_name] = set([ch])
                        else:
                            noTranslateDict['global'].add(ch)
                    # if file_path in noTranslateDict:
                    #     noTranslateDict[file_path] += 1
                    # else:
                    #     noTranslateDict[file_path] = 1
                    noTranslateCount += 1
                    print('%s not find in dict in %s and lang_name is %s' % (ch, file_path, str(lang_name)))

    write_to_file(file_path, content)


def get_lang_name(content):
    lang_name_lines = re.findall(langNameExp, content)
    if lang_name_lines:
        split_word = re.split(r'\s+', re.sub(r'\W', ' ', lang_name_lines[0]).strip())
        if len(split_word) == 2:
            return split_word[1]
    return None


def get_lang_name_dict(file_path):
    lang_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            l = Line(line)
            if l.is_legal():
                lang_dict[l.ch] = l.name
    return lang_dict


def is_ignore_file(file_path):
    return file_path.find('shoe') != -1


def add_translate_content(file_path, content):
    with open(file_path, 'r', encoding='utf-8') as file:
        old_content = file.read()
    write_to_file(file_path, content + old_content)


def translate_to_ftl_line(basename, arr):
    file_path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en\l_%s.ftl' % basename
    with open(file_path,
              'r', encoding='utf-8') as r_file:
        content = r_file.read()
    line_arr = list(map(lambda l: Line(translate_result=l), arr))
    line_content = '<#assign\n'
    line_content += '\n'.join(list(map(lambda line: line.to_en(), line_arr)))
    line_content += '>\n'
    write_to_file(file_path, line_content + content)

testFilePath = r'E:\git\pythonCode\test\translate\read\event_order.ftl'
# globalFilePath = ''
# globalSet = format_file2(globalFilePath)
# format_file2(testFilePath)
#
for path in get_all_file(enPath):
    format_file(path)


pc1Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\default'
pc2Path = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\template\saishi'
wapPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\waptemplate\default'
pathArr = [pc1Path, pc2Path, wapPath]
globalPath = r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en\l_global.ftl'
reTranslateFilePath = r'E:\git\pythonCode\test\translate\read\retranslate.txt'

format_file(r'E:\SHT\project\sas-web\src\main\webapp\WEB-INF\views\lang\en\l_global.ftl')

globalDict = get_lang_name_dict(globalPath)
noTranslateDict = {'global': set()}
# translate_file(testFilePath)


# with open(reTranslateFilePath, 'w', encoding='utf-8') as reTranFile:
#     reTContent = []
#     for key in noTranslateDict.keys():
#         reTContent.append('#' + key)
#         for value in noTranslateDict[key]:
#             reTContent.append(value)
#     reTranFile.write('\n'.join(reTContent))

# for path in pathArr:
#     for p in get_all_file(path):
#         translate_file(p)
# for (key, value) in noTranslateDict.items():
#     translate_to_ftl_line(key, translate.translate_word('\n'.join(value)))
print('noTranslateCount=%d' % noTranslateCount)
# print('no translate file length %s' % len(noTranslateDict))





