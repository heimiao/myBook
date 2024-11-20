## git使用场景命令 ##

### 本地代码切换线上其他分支 ### 
1. 当从gitee或者github 克隆一个多分支的项目，默认下载的是主分支main、master,现在想要下载除了默认分支的其他分支时需要执行以下命令

```
//要在本地克隆远程仓库的所有分支，首先你需要执行以下命令来克隆仓库：
git clone git://xxxxxx

//克隆完成后，你可以查看本地有哪些分支，通过运行： 
git branch

//这将列出所有本地分支，包括默认克隆下来的主分支。接下来，如果你想要切换到远程分支，比如origin上的某个分支，你可以使用：
git checkout origin/xxx

//不过，这只会切换到远程分支的本地追踪分支，而不是直接切换到远程分支。如果你想要直接操作远程分支，可以使用：
git checkout -b new-branch-name origin/remote-branch-name

//这将会创建一个新的本地分支，并将其设置为远程分支的追踪分支。如果你想查看所有远程分支，可以运行：
git branch -r
//这将列出所有远程分支。如果你想要更新远程分支到本地，可以运行：
git pull origin remote-branch-name

这将更新本地分支与远程分支的最新更改同步。

```
### 暂存手中代码 ### 

1. 切换分支： 当你正在开发一个功能或修复一个bug，但需要切换到另一个分支来处理其他任务时，使用git stash可以将当前的修改保存起来。这样你可以切换到其他分支并开始另一个任务，而无需提交或放弃你当前的修改。 

2. 合并代码： 在进行代码合并操作之前，你可能需要切换到目标分支并更新代码。使用`git stash`可以保存当前分支的修改，然后切换到目标分支并执行更新操作。完成后，你可以切换回原分支，并使用git `stash pop`来恢复之前的修改。 

3. 临时修复问题： 如果你遇到一个紧急的问题，需要快速切换到其他分支进行修复，但又不想丢失当前的修改，可以使用`git stash`将修改保存起来。然后你可以切换到修复分支，并在修复完成后再回到原分支恢复之前的修改。 

4. 多任务处理： 在开发过程中，你可能会同时处理多个任务或功能。当你想切换到另一个任务时，可以使用`git stash`将当前任务的修改保存起来，然后切换到另一个任务并开始工作。完成后，你可以回到之前的任务并使用`git stash pop`来恢复修改。 

5. 代码审查： 在进行代码审查时，你可能需要将修改保存起来，以便在审查过程中进行对比和讨论。使用`git stash`可以暂时保存你的修改，并切换到源代码分支进行对比和审查。

`git stash`命令用于保存当前工作目录的临时状态，包括暂存区和已修改但未暂存的文件。它会将这些修改保存在一个临时区域（即“堆栈”）中，让你能够回到一个干净的工作目录，可以进行其他操作。等到你完成其他任务后，可以再回到之前的状态，继续之前的开发。
```
	1. git stash save "message" 这将保存当前的工作目录状态到一个新的stash，并添加一条可选的消息来描述这个stash的内容。

	2. git stash list 查看当前保存的所有stash列表，每个stash都有一个唯一的标识符和对应的描述信息。

	3. git stash show [stash] 查看某个特定stash的变更内容。默认情况下，会显示最新的stash。

	4. git stash apply [stash] 将某个stash的变更应用到当前工作目录。这个stash不会从stash列表中移除。如果不指定stash，默认会应用最新的stash。

	5. git stash pop [stash] 与git stash apply类似，但在应用完stash后会将该stash从stash列表中删除。

	6. git stash drop [stash] 删除某个stash，从stash列表中移除。如果不指定stash，默认会删除最新的stash。

	7. git stash clear 删除所有的stash，慎用，它会清除所有保存的stash记录。

	8. git stash branch <branch_name> [stash] 创建一个新分支并将某个stash中的变更应用到新分支上。这样可以在一个干净的环境中继续开发。

	9. git stash -p 交互式地选择要保存的修改，即对每个修改进行确认。

	10. git stash -u 或 git stash --include-untracked 保存除了未跟踪的文件（Untracked files）外的所有修改。

	11. git stash --keep-index 或 git stash --no-keep-index 默认情况下，git stash会保存所有已暂存的修改，使用--keep-index选项可以只保存未暂存的修改。

	12. git stash --all 保存所有的修改，包括暂存区和未暂存的修改，以及未跟踪的文件。
```

### 文件跟踪管理 ### 

**1. 取消对已经被 Git 跟踪的文件的跟踪**

如果某个文件已经添加到 Git 并被提交，但现在不希望 Git 继续跟踪它，同时保留本地文件，可以按照以下步骤操作： 

1.1 将文件添加到 `.gitignore`

首先，将不希望继续跟踪的文件路径添加到项目的 `.gitignore `文件中。例如，要忽略 `config/settings.json` 文件，在 `.gitignore` 中添加：

```
config/settings.json
```

1.2 使用 `git rm --cached` 命令取消文件跟踪

接着，使用 `git rm --cached` 命令移除对该文件的跟踪。此命令会将文件从 `Git` 的索引中删除，但不会删除本地文件。执行以下命令：

```
git rm --cached config/settings.json
```
1.3 提交更改

将更改提交到仓库：

```
git commit -m "Stop tracking config/settings.json"
```
通过上述操作，Git 将不再跟踪该文件，且本地文件不会被删除。 


**2.取消对整个目录的跟踪**


如果不希望 Git 继续跟踪某个目录中的所有文件，可以按照以下步骤操作： 

2.1 将目录添加到 `.gitignore`

将要忽略的目录路径添加到 `.gitignore` 文件中，例如：
```
logs/
```

这样可以忽略 logs 目录中的所有文件。

2.2 使用 `git rm -r --cached` 命令取消目录跟踪

使用 `git rm -r --cached` 命令取消对整个目录的跟踪。此命令会递归地将目录及其所有文件从 Git 的索引中移除。执行以下命令：
```
git rm -r --cached logs/
```

2.3 提交更改

将更改提交到仓库：
```
git commit -m "Stop tracking logs directory"
```

通过这一步，Git 将不再跟踪 logs 目录中的所有文件，但它们会保留在本地文件系统中。

**3.忽略未来的文件更改**

如果不想完全停止跟踪某个文件，而是希望 Git 忽略它的未来改动，可以使用 git update-index 命令。

3.1 使用 `git update-index --assume-unchanged` 忽略更改

要让 Git 忽略某个文件的改动，可以使用以下命令：
```
git update-index --assume-unchanged <file>
``` 
例如：
```
git update-index --assume-unchanged config/settings.json
```

此命令告诉 Git 假定该文件未被修改，即使文件发生了更改，Git 也不会提示该文件有未提交的变动。

3.2 恢复文件的跟踪

如果之后需要恢复对该文件的正常跟踪，可以使用以下命令：
```
git update-index --no-assume-unchanged <file>
```

**4.查看跟踪和未跟踪的文件**

如果你想查看哪些文件被跟踪了根艺执行以下命令：

```
git ls-files
```
查看未被跟踪的所有文件
```
git status --untracked-files
```