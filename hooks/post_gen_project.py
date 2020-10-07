import os
import sys
import shutil
import subprocess
from utils import query_yes_no, query_field

# Control flow:
create_repo = query_yes_no("Would you like to link this repository to a repository on github.com?")

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

    os.chdir('..')