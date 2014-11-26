"""
Any method for sending mail can be used here. My implementation utilizes MailGun
(https://mailgun.com) to send the mail. If you choose to setup your own account
replace MAILBOX_ID, AUTH_KEY, and TO with the appropriate values from your
account.
"""

from requests import post

MAILBOX_ID = ""  # e.g. sandbox434ak3llfk
AUTH_KEY = ""  # e.g. key-8a8f8akd
TO = "" # e.g. Matthew Maclean <email@gmail.com>

FROM = "Mailgun Sandbox <postmaster@%s.mailgun.org>" % MAILBOX_ID


# Function that sends an email
def send_email(subject, content):
    return post(
        "https://api.mailgun.net/v2/%s.mailgun.org/messages" % (MAILBOX_ID),
        auth=("api", AUTH_KEY),
        data={"from": FROM, "to": TO, "subject": subject, "text": content})
