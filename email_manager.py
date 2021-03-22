from mail import Mail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

bot_mail = "pizarro.representaciones.bot@gmail.com"
bot_pass = "Emilia2021"

port = 465  # For SSL

def newMail(client):
    new_mail = Mail(bot_mail,client.get("email"))
    return new_mail

def send(m):
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Prueba bot"
    message["From"] = m.address_from
    message["To"] = m.address_to

    # Create the plain-text and HTML version of your message
    html = """\
    <html>
    <body>
    <p>Hi,<br>
        {}
    </p>
    </body>
    </html>
    """.format(m.message)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(html, "html")
    message.attach(part1)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(bot_mail, bot_pass)
        server.sendmail(m.address_from, m.address_to, message.as_string())
