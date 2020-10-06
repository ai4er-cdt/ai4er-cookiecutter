import os
import sys
import shutil
import subprocess

# Variables replaced by cookiecutter
repository_name = "{{cookiecutter.repository_name}}"
user_name = "{{cookiecutter.github_username}}"
user_email = "{{cookiecutter.github_email}}"
organisation = "{{cookiecutter.github_organisation}}"

# Derived variables
repository_url = "git@github.com:" + organisation + "/" + repository_name + ".git"

# Initialize project as git repository
subprocess.call(['git', 'init'])

# Configure git username and email
subprocess.call(['git', 'config', 'user.name', user_name])
subprocess.call(['git', 'config', 'user.email', user_email])

# Add remote at the repository URL
subprocess.call(['git', 'remote', 'add', 'origin', repository_url])
subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', 'Initalization'])
subprocess.call(['git', 'push', '-f', 'origin', 'master'])

# Unset the user name and email
subprocess.call(['git', 'config', '--unset', 'user.name'])
subprocess.call(['git', 'config', '--unset', 'user.email'])

os.chdir('..')