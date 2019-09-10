# Github Guide 
**Author: Isabel Warner**
**Init: 10Sept2019**

Adapted from `https://dzone.com/articles/top-20-git-commands-with-examples` 

### Setting Up a Git Repository for the first time 

First, configure git to your account 
```
git config --global user.name "name"
git config --global user.email "email@email.com"
```

Then, initialize the repository 
`git init [repository name]`

You can leave the repository name blank if you want to initialize the repository you're already in 

### Setting up a new Git Repository 

Any time you want to make a new repository, you'll have to `git init` it 

If you need to connect your machine to the remote server, use `git remote add [variable name] [Remote Server Link]`

To see your remote repositories use `git remote -v` (v flag = verbose) and it will print them in terminal 

### Staging and Committing Changes 

Use `git add [file]` to add that file to the staging area 

Use `git add *` to add all files in a directory (you'll probably want to do this when you first set up your repository)

Use `git commit -m "[Commit message]"`

`git push [variable name] master` pushes the changes, or sends them to your remote repository 

This commits all these files to your git repository, like taking a snapshot of the staging area 

_You must add things to the staging area before you can commit them_ 

`git commit -a` will commit any files you've added along with any files that have been changed since the last commit 

Check what's been committed using `git status` to list all the files 

Check which version of the files you're using by running `git log` 

To check a specific file version, use `git log -follow[file]`

### Visualizing differences 

`git diff` will show you what differences exist between the files on your computer and the ones in the repository 

`git diff -staged` will show you the differences you're about to push with `git commit`

`git show [commit]` will show the metadata and content changes of a specific commit 

`git tag [commitID]` will tag a specific commit, and make it easier to track 

`git branch` lists all the local branches in the current repository but `git branch [branch name]` will create a new branch, while `git branch -d [branch name]` deletes the feature branch 


### Resetting Changes

`git reset [file]` will unstage the file, but preserve the changes

`git reset [commit]` will undo all the commits after the specified commit, but preserve the local changes 

`git rm [file]` deletes the file from your working directory, and stages the removal to be committed 

`git checkout [branch name]` can be used to switch from one branch to another 

`git checkout -b [branch name]` will create a new branch and also switch to it 


