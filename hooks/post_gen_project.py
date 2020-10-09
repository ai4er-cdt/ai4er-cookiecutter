import os
import sys
import shutil
import subprocess
import pathlib

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

if __name__ == "__main__":
        
    # Control flow:  
    # 1. Creating link to data
    link_to_data = query_yes_no("Would you like to link to a data directory on your machine?", default="no")
    if link_to_data:
        while True:
            data_path = query_field("At which path is your data directory located?", default=None)

            if os.path.exists(data_path):
                # Transform into pathlib object for handy operations
                data_path = pathlib.PurePath(data_path)
                
                # Create symlink
                print("Ok, creating the link.")
                subprocess.call(["ln", "-s", data_path, "."])
                
                # Add data path to .gitignore
                with open(".gitignore", "a") as f:
                    f.write("\n\n" + "# Ignore data folder\n" + 
                        data_path.name + "\n" + 
                        data_path.name + "/" + "\n"
                        "." + data_path.name + "/")

                break

            else:
                print(f"The path {data_path} does not exist. Please enter a valid path.")
     
    # 2. Creating link to github repo
    create_repo = query_yes_no("Would you like to link this repository to a repository on github.com?", default="no")
    if create_repo:
        # Query repo name and owner from user
        repo_name = query_field("What is the name of the github.com repository you wish to link to?",
            default="{{cookiecutter.repository_name}}",
            len_limit=100)

        repo_owner = query_field("What is the name of the owner (user/organisation) of the repository?",
            default="ai4er-cdt",
            len_limit=30) 

        # Set user name and email for first commit
        user_name = "ai4er-cookiecutter"
        user_email = "cookiecutter@has-no-mail.org"

        # Derived variables
        repo_url = "git@github.com:" + repo_owner + "/" + repo_name + ".git"
        print(f"Linking to {repo_url}.")

        # Initialize project as git repository
        subprocess.call(['git', 'init'])

        # Configure git username and email
        subprocess.call(['git', 'config', 'user.name', user_name])
        subprocess.call(['git', 'config', 'user.email', user_email])

        # TODO: Automatically create repo (only for users without 2FA) 
        # subprocess.call(["curl", "-u",  user_name,  "https://api.github.com/user/repos",  "-d", "{'name':'%s'}" % repo_name])

        # Add remote at the repository URL
        subprocess.call(['git', 'remote', 'add', 'origin', repo_url])
        subprocess.call(['git', 'add', '-A'])
        subprocess.call(['git', 'commit', '-m', 'Initalization'])
        subprocess.call(['git', 'push', '-f', 'origin', 'master'])

        # Unset the user name and email form "cookiecutter" so user can use his own.
        subprocess.call(['git', 'config', '--unset', 'user.name'])
        subprocess.call(['git', 'config', '--unset', 'user.email'])        

    # 3. Creating conda environment
    create_conda_env = query_yes_no("Would you like to create a project environment using conda?", default="no")
    if create_conda_env:
        # Check that conda command exists
        from distutils.spawn import find_executable
        if find_executable("conda") is None:
            print("No conda executable found. Please first install conda on your machine and add it to the PATH.")
        else:
            # Call conda executable to create environment 
            subprocess.call(["conda", "env", "create", "--prefix=./env", "-f", "environment.yml"])
            env_path = os.path.abspath("./env")
            # Provide user feedback on how to activate
            print(f"Environment successfully created at {env_path}")
            print("To activate your conda environment, navigate to your project directory and call \n\t conda activate ./env")
            
            # Update conda config to show only the short name of the env.
            subprocess.call(["conda", "config", "--set", "env_prompt", "'({name})'"])
         
    os.chdir('..')

        
            