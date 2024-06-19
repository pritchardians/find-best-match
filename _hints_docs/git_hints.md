# Git Hints

<!-- TOC -->
* [Git Hints](#git-hints)
  * [Guidelines for good git hygiene](#guidelines-for-good-git-hygiene)
  * [To stash or not](#to-stash-or-not)
  * [Different ways to identify a commit](#different-ways-to-identify-a-commit)
  * [Normal Work Flow (opinionated)](#normal-work-flow-opinionated)
* [Git while the gitting is good](#git-while-the-gitting-is-good)
    * [My favourite logging technique](#my-favourite-logging-technique)
    * [Branching out with branches](#branching-out-with-branches)
    * [Looking at history](#looking-at-history)
      * [Wow! Awesome filtering!](#wow-awesome-filtering)
    * [**Getting to know your files; working area, staging area, HEAD commit**](#getting-to-know-your-files-working-area-staging-area-head-commit)
* [Gitting when things went south](#gitting-when-things-went-south)
  * [Find the issue](#find-the-issue)
          * [Example: git diff --name-only HEAD~5 HEAD~6](#example-git-diff---name-only-head5-head6)
  * [Fix the issue](#fix-the-issue)
  * [Working with remotes flawlessly and easily](#working-with-remotes-flawlessly-and-easily)
  * [Rewriting history](#rewriting-history)
  * [Tools _sometimes_ make life easier](#tools-_sometimes_-make-life-easier)
  * [Remove files from git repo](#remove-files-from-git-repo)
<!-- TOC -->

## Guidelines for good git hygiene
- Turn off unnecessary warnings ```git add . -u```
- Always push to the server when leaving a PC
- Always ```fetch -a``` and ```git pull <current branch>```  before starting
- Always use git log to make sure you are working on the latest code
- Create a branch if you're not sure if you forgot to push work from another PC to the remote
- Create a branch for every experiment
- Commit a lot with solid descriptive names, so you can read the history
  - Commit every time you move from one change to another
    -For instance, if you are adding a class and you see an opportunity to rename another class, finish your original work
  (with frequent commits), commit, make the rename, commit..
- If in doubt, create a branch
- If bringing back files from older branches / commits do so in a new branch
- Tidy up branches by deleting any failed experiments
- Tidy up branches by merging little offshoots back to the branch you branched from and deleting them-when you are 
sure the code is clean
- Never merge to the 'develop' branch without thorough testing
- Never merge to master until you have deployable code
- New branch, commit, commit, commit, repeat...
- Did I mention, **_CREATE A NEW BRANCH_** and **_COMMIT A LOT!_** :smile:

## To stash or not

Not sure why you would do this as the stash does not contain a description of what is in it.
Wouldn't you just want to create a new junk branch from the current state,
checkout the branch you were on before creating the junk branch,
muck about with the current working directory and index (staging area) as you see fit,
and delete the junk branch (aka your system stash) when you don't need it.
If you think all this branching could go wrong, you can always bring an old branch/commit
to life after deleting it with reflog. <br>
Always remembering-don't ever re-write history if that history was saved to a remote!
Bring the old code back as a new branch instead of detaching the head as the detached commits
will be garbage collected and your team will reprimand you-behind your back if not to your face!

## Different ways to identify a commit

Use any of these where you see <commit ID> in this documentation

- HEAD~x \*where x is the number of commits you want behind the current commit
- commit sha
- Date range (\<from\> // \<to\>)
- \-\-after/before="yesterday",}
- \-\-after/befpre="ccyy-mm-dd"
- \<since\>..\<until\>
- \-\-author="\<author name\>"
- \-\-grep="\<message\>"
- tag

## Normal Work Flow (opinionated)

```
git fetch -a
git status
git pull
git status
    <work like a banshee>
git status
git add .
git commit -m "commit message"
git status
git push
```
If you are using **pull requests** on a remote repo, remember to ```git pull <branch>``` the branch you updated in the
pull request to keep your local code synced up!

# Git while the gitting is good

### My favourite logging technique

git log --pretty=format:"%h--%ad--%an--%B" --date=format:'%Y-%m-%d %H:%M' --all --since=2.weeks.ago

git config --global alias.nicelog 'log --pretty=format:"%h--%ad--%an--%B" --date=format:'%Y-%m-%d %H:%M' --all --since=2.weeks.ago

### Branching out with branches

git push origin --delete \<branchName\> _Delete remote branch-CAREFUL!_.

git branch \<branchname\> \<commit ID\> _To create a branch with an old commit_

git remote prune origin _Removes ghosts of deleted branches when listing branches_

git branch -r _List remote branches_

### Looking at history

git log --oneline --decorate

git log -all _Show history across branches_

git log -3 _Show last 3 commits_

git log -p _Show diff of changes_

git log --stat _Shows number of insertions, deletions etc._

git shortlog _Seems fairly pointless :)_

git log \<since\>..\<until\> _and all the variations I listed in the commot ID section_

#### Wow! Awesome filtering!

git log -- \<filename1\>...\<filenamex\> _Show history of chosen files_

git log -S"\<pattern\>" _Show history where files contain this pattern_

git log -S"\<pattern\>" _Show history where files contain this pattern_

git log --pretty=format:"\<options\>" - %cn _Commiter name_ - %h _Abbreviated hash_ - %cd _Commit date_

### **Getting to know your files; working area, staging area, HEAD commit**

git diff _show differences between working directory and staging area_

git diff --cached _show differences between staging area and latest commit_

git diff HEAD _show differences between working directory and latest commit_

git reset --hard \<Commit ID\> _Current branch point, working directory and staging area become \<Commit ID\>._

git reset HEAD _Unstage all files in staging area. Leave working directory untouched_

# Gitting when things went south

## Find the issue

git diff \<branchName\>..remotes/origin/\<branchName\> _Compare the entire fileset between local and remote_

git diff --name-only \<commit ID\> \<commit ID\> _Show filenames that changed between commits_

###### Example: git diff --name-only HEAD~5 HEAD~6

gitk --all -- \<filename\> _graphical interface to see old file versions_

git show \<commit ID\>:path/to/file _See a version from a previous commit_

git rev-list -n 1 HEAD -- \<file*path\> \_show the last commit containing a file-* **to show when it was deleted**

git log --diff-filter=A --\<file*path\> \_show commit when a file was added*

git diff HEAD~10 HEAD _Compare entire project between current and 10 commits ago_

gitk [filename / pattern] _see history of file
## Fix the issue

git checkout \<branchName\>@\<commit ID\> -- <path/to/file> 
_Get an old version of a file back into the current 
working directory, so it can be added and committed after testing_

## Working with remotes flawlessly and easily

git push --set-upstream origin \<branchName\> _Push a new branch to remote_

    git remote add origin \<URL of origin\> _attach your repo to an existing remote_

To create a new remote from a local repo
git push --set-upstream https://gitlab.example.com/namespace/nonexistent-project.git master <br>
git remote add origin https://gitlab.example.com/namespace/nonexistent-project.git <br>

Example
git push --set-upstream https://gitlab.com/WeeMan/newGitRepo.git master <br>
git remote add origin https://gitlab.com/WeeMan/newGitRepo.git <br>

Delete remote branch _git push -d remote <branchname>_

## Rewriting history

git reset --hard \<commit ID / branch\> _Update repo, staging area and working directory_

git reset --mixed [the default]] \<commit ID / branch\> _Update repo and staging area only_

git reset --soft \<commit ID / branch\> _Update repo only. Not sure when you'd want to do this_

If you want to rename a branch while pointed to any branch, do:

    git branch -m <oldname> <newname>
If you want to rename the current branch, you can do:

    git branch -m <newname>
## Tools _sometimes_ make life easier

posh git gives autocompletion and shows number of added, deleted, modified files on current branch in index 
and working tree
[master +1, ~0 -0 | +0 ~5 -0 !]

```
cd ~/
git clone https://github.com/dahlbyk/posh-git

git commit --amend -m "\<new commit message\>

git commit --amend --no-edit _Change files from the previous commit without changinmg the message_
```

## Remove files from git repo
List of files in repo

git ls-tree --full-tree -r --name-only HEAD
git rm [filename / pattern]
git status
git add .
git commit -m 'removed [filename/pattern]'
git push