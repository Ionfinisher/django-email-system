from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def send_email_view(request):
    form = ContactForm(request.POST or None)
    success = False

    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        html = f"""
<html>
  <body style="margin: 0; padding: 0; font-family: Arial, sans-serif;">
    <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse;">
      <!-- Header -->
      <tr>
        <td align="center" bgcolor="#007BFF" style="padding: 40px 0 30px 0;">
          <h1 style="color: #fff; margin: 0; font-size: 36px;">Bienvenue !</h1>
        </td>
      </tr>
      <!-- Main Content -->
      <tr>
        <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
          <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
              <td style="color: #153643; font-size: 24px;">
                <b>Salut 👋 {email},</b>
              </td>
            </tr>
            <tr>
              <td style="padding: 20px 0 30px 0; color: #153643; font-size: 16px; line-height: 24px;">
                Merci d'avoir envoyé un message depuis notre site: LIVE CODING SITE. Ceci est juste un petit test
              </td>
            </tr>
            <tr>
              <td align="center">
                <a href="https://example.com" style="background-color: #007BFF; color: #ffffff; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-size: 16px;">Découvrir Plus</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <!-- Footer -->
      <tr>
        <td bgcolor="#ee4c50" style="padding: 30px 30px;">
          <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
              <td style="color: #ffffff; font-size: 14px;" width="75%">
                &copy; 2025 Notre Entreprise<br/>Tous droits réservés.
              </td>
              <td align="right" width="25%">
                <table border="0" cellpadding="0" cellspacing="0">
                  <tr>
                    <td>
                      <a href="http://www.twitter.com/">
		Twitter
                      </a>
                    </td>
                    <td style="font-size: 0; line-height: 0;" width="20">&nbsp;</td>
                    <td>
                      <a href="http://www.facebook.com/">
                        Facebook
                      </a>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
"""
        send_mail(
            "TEST D'ENVOI DE MAIL",
            message,
            email,
            ["Pain@gmail.com"],
            html_message=html
        )
        success = True
    context = {'form': form, 'success': success}
    return render(request, 'mailer/contact.html', context)
