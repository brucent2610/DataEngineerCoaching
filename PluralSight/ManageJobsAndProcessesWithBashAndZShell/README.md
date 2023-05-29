#Overview
- Identify processes
- Use jobs to your advantage
- Tactically pause processes
- Customize your shell experience

#Understanding Processes

**One Simple Process**
- Every action the operation system undertakes must be executed in a processor to produce the desired output

**Many Processes**
- Serial Processing: The processor would work on each process in turn fully completing one before moving onto another
- Concurrent Processing: The processor switches between each process, completing them in smaller steps. If all three processes take the same amount of work, then the outputs for each will appear in roughly the same time as serial processing, but they will become complete all at once
- Parallel Processing: using more than one processor, so multiple processes can truly execute simultaneously

#Anatomy of a Process

**Process ID (PID)**
- Reference for a process
- Unique at the time
- Reused eventually

**Code and Data**
- Code and Data duality
- We want to know the command

**CPU**
- Expressed in absolute time
- Also expressed as a relative percentage
- Seemingly imposible value

**Memory, RAM**
- Fast storage for data
- Volatile, managed by the operating system
- Messured in MB, GB or a percentage

#Understanding Processes
- Session are used to manage all of the execution that a user may start through running programs
- When session end this means the operating system can easily end all of the related execution

**Process Group (PGID):**
- There can be one or many process groups within a session
- The way to collect related processes together
- All the processes in a process group can receive the same communication from the operating system in the form of signals
- Within the process groups are individual processes, each of these processes will have parent process ID (PPID) inherited from PID of the process that spawned (sinh ra) it.
- Each process is capable of spawning threads
- Creating a thread tends to come with less overhead than starting another process
- Thread are a way of having one process achieve separate tasks while sharing memory and other resources
```
ps aux | head
ps aux | grep python
pgrep -fa python
```

#Understanding Jobs
**Process Group vs Job**
- Job are equivalent to process groups

**Foreground jobs**
- Always a foreground job
- Interactive
- Takes commands as usual
- fg to bring a job to the foreground

**Background jobs**
- Created from the foreground
- Single ampersand at the end
- Continues executing
- Defaulting output is spawning shell
- bg to background a suspended job

**Suspended jobs**
- Pause execution
- Generally suspend foreground jobs
- Ctrl + Z

#Managing Jobs and Processes with Bash and Z Shell

**Variable**
Local
- Standard assignment
- Available only in assigning job
- Resolve using dollar syntax
Global
- Assigned with "export"
- Available in all spawned jobs and subprocesses
- Resolve using dollar syntax

**Process Priority**
Scheduling
- Limited resources, requires a running order
- Higher priority run first
- Identical priority run interchangeably
Priority (PRI)
- Values -100 to 39
- Higher number, yields to lower
- Negative numbers considered "real time"
Nice
- Values -19 to 20
- Higher number, yields to lower
- Maps to underlying priority

**Signals**
- Inter-process communication
- Asynchronous event notification
- Signals have number, different between OS
- Optional signal handlers
- Most signals can be ignored
- Related to interrupts, but different
Common Signals
- Hang up (HUP): sent to a background job, when the spawning foreground job is ended, Related "nohup" utility
- Quit (QUIT): Commonly used for terminating a process, whilst dumping its memory
- Kill (KILL): Terminating stubborn process, cannot be ignored
- Terminate (TERM): Commonly issued by other software for terminating a process
- Stop (STOP): stop (suspend) a running process, can not be ignored
- Continue (CONT): Resume a stopped process

**Suspending Jobs Tactically**
Balacing act of interactive servers
Some jobs require more resources
Jobs being terminated causes frustration
You could try suspending when
- Disk is filling up
- CPU is needed
- More RAM will be available later

**Shells in General**
Just another piece of software
Configurable through commands
System defaults and user level configuration
Interactive Shells
- Attached to the terminal (TTY)
- Submit commands
- See feedback
- SSH or starting "Terminal"
Non-interactive Shells
- Not attached to the TTY
- Cannot receive commands
- Used to run scripts
Login Shells
- Part of the login process
- SSH
- Setup the shell and user's session
Non-login
- Setup the shell only
- Starting "Terminal"
Bash Config files: 
- Interactive Login: 
```
/etc/profile
~/.bash_profile
~/.bash_login
~/.profile
~/.bash_logout
```
- Non Interactive Login
```
/etc/bash.bashrc
~/.bashrc
```
Z-shell Config files: 
- Interactive Login: 
```
/etc/zshenv
~/.zshenv
~/.zprofile
~/.zshrc
~/.zlogin
~/.zlogout
```
- Non Interactive Login
```
/etc/zshenv
~/.zshenv
/etc/zshrc
~/.zshrc
```

**Bash Shell Prompt**
- PS1 variable 
- Intepreted string, with - backslash escaped characters
- Can also contain commands to evaluate
Example 
```
export PS1="\u@\h [\$(date +%k:%M:%S)]> "
```
- Exporting global variable called PS1 and opening the string
- User @ hostname
- Opening square brackets
- Using $() to resolve the "date" command
- Closing the square brackets
- Tranditional right arrow, a square for clarity and closing the string
**Z-Shell Prompt**
- PROMPT variable
- Interpreted string, with percentage escaped characters
- Commands or logic to evaluate
Example
```
PROMPT="%(?.%F{green}?%?.%F{red}?%?)%f %B%F{240}%1~%f%b %# "
```
- A variable called PROMPT and opening the string
- Open logic statement
- True condidition and false condition, separated by a dot
- Reset the text foreground color to default
- Start bold text
- Set the foreground text color to grey
- Show only the last element of the current working directory, with home as ~
- Default the foreground text color, stop writing in bold
- Show a # when root otherwise %, close the string

**Alias**
```
alias short="the long command"
alias ..="cd .."
alias ll="ls -lah"
alias ports="netstat -tulanp"
```

**Default Text Editors**
- Some commands require an editor
- Default often used
- Set the default through EDITOR and VISUAL variables

