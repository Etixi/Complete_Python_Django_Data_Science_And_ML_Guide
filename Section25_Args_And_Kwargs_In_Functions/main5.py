def send_email(to, subject):
    print(f"Sending an email to : {to} ...")
    print(f"Email subject: {subject}")

def send_email_args(to, subject, *args):
    print(f"Sending an email to : {to} ...")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients.")
        for recipient in args:
            print(recipient)

def send_email_args_kwargs(to, subject, *args, **kwargs):
    print(f"Sending an email to : {to} ...")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients.")
        for recipient in args:
            print(recipient)


    if kwargs:
        print("Additional details for the email.")
        for key in list(kwargs):
            print(f"{key} : {kwargs[key]}")



send_email('test@test.com', 'Hello There')
print("**"*30)

send_email_args('test@test.com', 'Hello There', 'other@test.com', 'someone@gmail.com')
print("**"*30)

send_email_args_kwargs('test@test.com', 'Hello There', 'other@test.com', 'someone@gmail.com',
                       bcc='etienne@gmail.com', img='test.png')

print("**"*30)
send_email_args_kwargs('test@test.com', 'Hello There', bcc='etienne@gmail.com', img='test.png')
