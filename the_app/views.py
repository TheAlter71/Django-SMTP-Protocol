from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        actual_message = 'Boss,\nYou did it, you successfully send mail!\n\nName: ' + name + '\nEmail : ' + email + '\nSubject : ' + subject + '\nMessage :\n' + message 
        
        # SEND EMAIL
        send_mail(
            'Public Response!' , # Subject
            actual_message, # Message
            email , # From Email
            ['example2@gmail.com'], # To Email [Enter the mail you want to receive email, you can use multiple email using comma (,)]
        )

        context = {
            'success' : 'Message Sent successfully!',
        }

        return render(request, 'index.html', context)


    return render(request, 'index.html')
