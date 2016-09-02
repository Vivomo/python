

class Log(object):

    def __init__(self, s):
        info = s.split(' | ')
        self.isLegal = False
        if len(info) == 4:
            self.error = info[3]
            self.url = info[0]
            self.ua = self.format_ua(info[1])
            self.js = info[2]
            self.isLegal = True

    @staticmethod
    def format_ua(ua):
        return ua

logPath = r'E:\qqFile\前端日志\jsmonitor.log.2016-09-01'
logArr = []
errorMap = {}
with open(logPath, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        log = Log(line)
        if log.isLegal:
            logArr.append(log)
            if log.error in errorMap:
                errorMap[log.error] += 1
            else:
                errorMap[log.error] = 1

# logArr.sort(key=lambda l: l.error)
# print(errorMap)
for k, v in errorMap.items():
    print('%s=%s' % (k, v))

with open('formatLog.txt', 'w', encoding='utf-8') as file:
    # file.write('\n'.join(logArr))
    pass