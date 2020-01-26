# ihmAdminDjango

**If it's your first time to use Git, please follow instructions bellow**

Turn an existing directory into a git repository
```shell
  git init
```

Configure user information for your local repository
```shell
  git config --global user.name "Your Name"
  git config --global user.email you@example.com
```

**The first part, you will have to do it only once.**<br>
**The second part should be done every time you want to commit your changes.**

Switch to the specified branch
```shell
- git checkout <branch-name>
```
Verify in which branch you are and what are the new modification
```shell
  git status
```
Add the changes
```shell
- git add <file>
 ```
Commit your changes
```shell
  git commit <file> [option -m]
```
The option is for adding a label to the commit 
  
```php
git remote add origin https://github.com/<your-github-username>/my-first-blog.git
```
Updates your current local working branch with all new commits from the corresponding branch on GitHub
```shell
  git pull
```
Before push check if there are no conflicts otherwise they will have to be resolved. If it's OK, then push
```shell
  git push 
```

>**NB. For more information about git command line, browse the following link: https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf**<blockquote>
