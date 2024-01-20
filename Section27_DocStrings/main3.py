def send_email_args_kwargs(to, subject, *args, **kwargs):
    """
    Sends email to different recipients

    :param str to: Recipient address
    :param str subject: Email Subject
    :param str args: Additional recipients
    :param str kwargs: Additional details
    :return None:
    """

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

# Print the docstring
print(send_email_args_kwargs.__doc__)
print("**"*30)


send_email_args_kwargs('test@test.com', 'Hello There', 'other@test.com', 'someone@gmail.com',
                       bcc='etienne@gmail.com', img='test.png')

print("**" * 30)

send_email_args_kwargs('test@test.com', 'Hello There', bcc='etienne@gmail.com', img='test.png')
