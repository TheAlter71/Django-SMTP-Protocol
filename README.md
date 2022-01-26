# Django SMTP Protocol with Gmail

This is the free service from gmail to send and receive emails.


> What we need for this things done,
  1. Python/pip install in PC.
  2. A gmail address for sending email.
  
> Configure the gmail,
  1. Go to the link using this gmail, [myaccount.google.com/lesssecureapps]
  2. Turn this on.
  3. I don't recommend that to turn this on in your personal Gmail, instead create a new gmail account for the project.

> Run code in virtual environment
  1. Clone the project and open the folder in terminal and run -- [pip install pipenv]
  2. Then active the environment -- [pipenv shell]
  3. Install all the requirements -- [pipenv install -r requirements.txt]
  4. Run the project -- [python manage.py runserver]

> Configure the settings.py file,
  1. Go to, the_project/settings.py
  2. Remove the comment from line 25 according to its upper instruction.
  3. Enter your email address and password in line 134, 135 according to the instructions. [This email will be use for sending emails]
 
> Configure views.py file,
  1. Go to, the_app/views.py file,
  2. Remove the example@gmail [line: 21] and Enter your gmail that you want to receive email.
  3. You can use multiple email there.
 
 Enjoy!
