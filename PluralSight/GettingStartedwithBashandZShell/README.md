#What is the shell and why we need it?
- Run programs by typing commands
- Text based UI: *command line*
- **Powertool for almost every task**
**Bash and zsh are popular shells**
**UNIX**
- Huge ecosystem of commandline tools
*Great for automation*

#Who need the shell?
- File management
- System adminstration
- Software development
- Data Filtering, Transform, etc
- Remote Access
- Scripting

#UNIX, LINUX, MAC OS
- sh, ksh, csh, tcsh, and many more
- Bash is most popular
- Zsh is default on Mac
#Windows
- Cmd, Powershell
- Linux subsystem runs bash/zsh

#Bash vs Z Shell
- Bash is most popular
- Z Shell
⋅⋅⋅Similar to bash
⋅⋅⋅More configurable, more features
⋅⋅⋅https://ohmyz.sh/
- **You can configure your default shell**

#Notice
The command line is a powertool
There is no undelete and no undo
**Prevent Problems**
- Read your input twice before executing
- System resources are usually protected
- Setup a safe environment
⋅⋅⋅Virtual Machine
⋅⋅⋅Unprivileged user account

#The Shell and the Terminal
Shell is mostly limited to text
- Enter and edit text
- Return text output
We run the shell in a terminal emulator
- Translate keystrokes for the shell
- **Support fonts, colors**
The prompt
- Shell is waiting for input
- Very configurable

#Navigating the filesystem
- Current location
- Jump to different locations
- Listing files
- *Hidden files*

#Entering commands
- History
- Completion

#Anatomy of a Command
- First word: the command to run
- Other words: arguments
- Options are arguments starting with -
- Change behavior of the command

#Filenames
Best practices
- Use letters, numbers, dots, - and _
- Want to be really safe? Only use lowercase
- Be careful with spaces
- Especially trailing spaces
Characters to Avoid
- Quotes: ` ' "
- Brackets, parens: {} () < > []
- Interpunction: ~ ? & | : ' \ ^
- Other: $ @ ~ * #
- Whitespace: tab delete backspace newline

#Saving Customization
Bash
- .profile read on login
- .bashrc read for interactive shells
- Other files: see manpage
Zsh
- .zshenv read always
- .zshrc read for interactive shells
- Other files: see documentation
- [Check out](https://ohmyz.sh)
Use .-rc file for interactive shells
- alias
- running commands
Use .profile / .zshenv for variables
- like $PATH, $EDITOR