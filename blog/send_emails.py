from django.conf import settings
from django.template.loader import render_to_string

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import re

from_addr = settings.EMAIL_USER
password = settings.EMAIL_PASSWORD
smtp_server = settings.SMTP_SERVER

# format for the sender and subject
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#define the template for sending email 
def send_email(recipient,html_template,context,subject):
    to_addr = recipient
    html = render_to_string(html_template,context=context)
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = _format_addr('Blog <%s>' % from_addr)
    msg['To'] = _format_addr('主人 <%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 587) # The default port for the SMTP protocol is 25
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def myblog_message(args):
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\.(.*)$')
    create_time = pattern.search(args['create_time'])
    context = {
        'content':args['message'],
        'create_time':create_time.group(1)+" "+create_time.group(2),
        'client_ip':args['client_ip']
    }
    html_template = 'message.html'
    subject = 'My blog message'
    recipient = 'chenshaobo272@gmail.com'
    try:
        send_email(recipient,html_template,context,subject)
    except Exception as e:
        print(e)