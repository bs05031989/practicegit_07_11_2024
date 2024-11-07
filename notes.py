
"""
git config --global user.name
git config --global user.email

need to establish ssh connection of the remote system and GitHub

need user email of GitHub account

Key Generation : Use git bash terminal

ssh-keygen -t ed25519 -C "your_email@example.com"

It will generate a key in .ssh folder inside user

clip < ~/.ssh/id_ed25519.pub  : This will copy the key contents

In git browser add new ssh key paste the key.

Starting :   Git Init

             Git add readme.md
             Git add .

             Git Branch -M main
             

git commit -m " Commit Message"

git push origin main

git ignore


git pull origin main

To create a new virtual environment

conda create -p venv python==3.9 -y

To activate virtual environment

conda activate venv/

sometimes environment causes issues in activating :

1. Please always use CMD as a terminal
2. use Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

Multiple Branches 

to make new branch a copy of main : git branch developer

to work on new branch : git checkout developer

after committing the work on developer branch , shift to main branch

git branch main

to merge the developer branch work with main : git merge developer

to delete the developer branch : git branch -d developer

Resolving conflicts

git checkout commit name : matches with the last commit change

if there are multiple changes unwanted : git checkout -f

to get file untracked from staging : git rm --cached filename

to show latest commits : git log -p -2

git status -s : short summary using green and red color (staging & working tree)

git commit -a -m " both staging & Commit" 

git checkout -b newbranchname : branch generation & checkout both at once






"""