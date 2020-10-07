import sys

def query_yes_no(question: str, default: str="yes") -> bool:
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


def query_field(question: str, default: str = None, len_limit: int = 100) -> str:
    """Ask a question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be a string or None (meaning
        an answer is required of the user).
    "len_limit" is the maximal number of characters that an answer
        can have and still be accepted.

    The "answer" return value is the string typed by the user.
    """
    if default is None:
        prompt = "  "
    elif isinstance(default, str):
        prompt = f" [{default}] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        user_answer = input()
        if default is not None and user_answer == '':
            return default
        elif len(user_answer) < len_limit:
            return user_answer
        else:
            sys.stdout.write(f"Please respond with a non-empty answer that has less than {len_limit} characters.\n")