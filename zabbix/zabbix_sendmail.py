import smtplib
import sys
import string
import mail_info

class MySendmail():
    """docstring for MySendmail"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def sendmail(self, mailTo, subject, body):
        mailFrom = mail_info.mailFrom
        self.body = string.join((
            "From: %s" % mailFrom,
            "To: %s" % mailTo,
            "Subject: %s" % subject,
            "",
            body
            ), "\r\n")
        try:
            self.smtp = smtplib.SMTP()
            self.smtp.connect(self.host, self.port)
            #print self.body
            self.smtp.login(mailFrom, mail_info.password)
            #print mailFrom
            self.smtp.sendmail(mailFrom, mailTo, self.body)
        except Exception, e:
            sys.exit(1)
        finally:
            self.smtp.quit()

if __name__ == "__main__":
    mailTo = sys.argv[1]
    subject= sys.argv[2]
    body= sys.argv[3]

    # Test 使用:
    import mail
    mailTo = mail.mailTo
    subject = mail.subject

    s = MySendmail("smtp.163.com", 25)
    s.sendmail(mailTo, subject, body)

