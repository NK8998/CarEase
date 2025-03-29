# using SendGrid's Python Library
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
load_dotenv()  

async def sendMail(email, name, subject, receipt_id):
    """
    Send a crafted appointment confirmation email using SendGrid API.

    :param email: Recipient's email address
    :param subject: Subject of the email
    :param receipt_id: Unique receipt ID for the appointment
    """
    html_content = f"""
    <div style="font-family: Arial, sans-serif; padding: 20px;">
        <h2 style="color: #2c3e50;">Hello, {name}</h2>
        <p>Your appointment for <strong>car servicing</strong> has been successfully added!</p>
        <p>You can track the progress of your service by visiting:</p>
        <p><a href="https://CarEase.com/progress" style="color: #3498db;">CarEase.com/progress</a></p>
        <p>Then, simply paste this receipt ID:</p>
        <p style="font-size: 18px; font-weight: bold; color: #27ae60;">{receipt_id}</p>
        <p>Have a great day and drive safe!</p>
        <img src="https://dxm.content-center.totalenergies.com/api/wedia/dam/transform/xysh7dg731tahpw133wmjuk8by/roadside-vehicle-repair-service-workers-change-mount-tires-garage-car-341509-3419-jpeg.webp?option=default" 
             alt="Car Service" style="width:100%; max-width:600px; margin-top:20px; border-radius:8px;" />
        <p style="color: #95a5a6; font-size: 12px;">CarEase Team</p>
    </div>
    """

    try:
        key = os.getenv("SENDGRID_API_KEY")
        if key is None:
            raise ValueError("SENDGRID_API_KEY not found in environment variables")
        sg = SendGridAPIClient(api_key=key)
        message = Mail(
            from_email='hello@streamgrid.site',
            to_emails=email,
            subject=subject,
            html_content=html_content
        )
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
