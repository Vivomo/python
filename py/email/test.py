from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

fromAddr = '851721548@qq.com'
password = input('Password: ')
toAddr = '929992114@qq.com'
smtpServer = 'smtp.qq.com'

msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % fromAddr)
msg['To'] = _format_addr('管理员 <%s>' % toAddr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

server = smtplib.SMTP(smtpServer, 587)
server.set_debuglevel(1)
server.login(fromAddr, password)
server.sendmail(fromAddr, [toAddr], msg.as_string())
server.quit()
