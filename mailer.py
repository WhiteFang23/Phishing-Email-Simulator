import smtplib
from email.mime.text import MIMEText
from jinja2 import Template

# ✅ Mailtrap SMTP configuration (from your screenshot)
SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587

SMTP_USERNAME = "YOUR_MAILTRAP_USERNAME"
SMTP_PASSWORD = "YOUR_MAILTRAP_PASSWORD"


SENDER_EMAIL = "security@company.com"


def send_phishing_email(to_email):
    # Load phishing email HTML template
    with open("templates/phishing_email.html", "r", encoding="utf-8") as file:
        template = Template(file.read())

    html_content = template.render(email=to_email)

    msg = MIMEText(html_content, "html")
    msg["Subject"] = "Urgent: Verify Your Email Account"
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()

    print(f"✅ Phishing email (simulation) sent to {to_email}")
