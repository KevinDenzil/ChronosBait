import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, subject, body):
    # Email credentials (Use an App Password for security)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'rhjananiya@gmail.com'  # Replace with your email
    smtp_password = 'dqdy pbav ztyn mjdv'  # Replace with your App Password

    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # HTML body with a clickable hyperlink
    html_body = f"""
    <html>
    <body>
        <p>This is an automated email sent by a Python script.<br>
        Click <a href="{body}" target="_blank">here</a> to visit the link.</p>
    </body>
    </html>
    """

    # Attach the HTML content
    msg.attach(MIMEText(html_body, 'html'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS for security
        server.login(smtp_user, smtp_password)

        # Send the email
        server.sendmail(smtp_user, recipient_email, msg.as_string())
        print('Email sent successfully')

        # Disconnect from the server
        server.quit()

    except Exception as e:
        print(f'Failed to send email: {e}')

# Example usage
if __name__ == '__main__':
    recipient_email = 'h0r402040@gmail.com'
    subject = 'Automated Email'
    link = 'https://chronosbait.onrender.com/'  # The link you want to send
    send_email(recipient_email, subject, link)
