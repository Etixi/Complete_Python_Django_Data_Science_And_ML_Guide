print()
print("Example - Verifying User Permissions with Decorator Functions" + "\n" +
      "==============================================================")
print()


def is_user_authenticated():
    return True

def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_authenticated():
            print("User is authenticated")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is not authenticated")
    return wrapper

@check_user_auth
def do_sensitive_job():
    # Perform action only if user is authenticated
    print("Some sensitive job results")


do_sensitive_job()