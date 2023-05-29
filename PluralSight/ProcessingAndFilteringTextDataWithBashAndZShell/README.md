# Overview
- Searching for files and directories
- Searching for text patterns
- Filter, process, format, and output
- Reading and writing to text files

# Searching for Files and Text
## Linux find command
- There are few Linux commands which can search for files
- "find" is the most common one: it is a powerful command
- "man" page shows "find" has a lot of options
## Find files with find and locate
```
find / -type f -name *.log
find / -type f -name '.*'
find / -type d -name www
find / -type d -perm 777
find / -type d -empty

find / -user apache
find / -group apache
find /var/log -type f -amin -60 #accessed in the last hour
find /var/log -type f -size +1024M #size more than 1GB
```
### find vs locate
- "find" searchs directories in real-time
- "locate" searchs its internal database
-- Depending on size and depth of file system, "locate" can find files quicker
-- Need to keep its database updated
-- Daily cron job runs "updatedb"
- "locate" is not pre-installed in Red Hat or Ubuntu

## Reading File with cat, more and less
### Linux cat Command
- cat: Short for "concatenate"
- Write: Used to combine multiple files into one
- Read: Can also read files
### Linux System Log
- Known as "syslog", it is important file where Linux records its events.
- Many apps write here too
- Usually this file first place to start troubleshooting
```
cat /var/log/messages
more /var/log/messages
less /var/log/messages
```
```
cat > weekdays1
cat > weekdays2
cat weekdays1 weekdays2
cat -b weekdays1 weekdays2
cat -b weekdays1 weekdays2 > weekdays
```

# Reading Files with head and tail
## Linux head and tail Commands
- head: Reads a number of lines or bytes from beginning of file
- tail: Reads a number of lines or bytes from end of file
```
head /var/log/messages
tail /var/log/messages
tail -n 250 /var/log/messages | less
```
## "Busy" Files
- Files like the system log can be very busy with applications always writing to it
- The "tail" command by itself may not always show the latest data
```
tail -f /var/log/messages
tail -v /var/log/messages /var/log/cloud-init.log
```

# Searching Text with grep
## Linux grep Command
- Global Regular Expression Print (grep)
- Powerful command for searching text without opening files
## Why grep?
- Problem: find an event from a set of log files
- Open log file in editor (large files can take long time to load)
- Search through the file for each occurrence of the event
- Repeat the process for every log file
## Basic grep Syntax
```
grep <option_1> <option_2> ... <option_n> <search_text_pattern> <file_1> ... <file_n>
grep "System" /var/log/messages
grep -i "system" /var/log/messages
grep -i -w "system" /var/log/messages
grep -i "shut*down" /var/log/messages
grep -i -n "shut*down" /var/log/messages
grep -i -n -B 2 -A 3 "shut*down" /var/log/messages
grep -v "system" /var/log/messages # Search not system
grep -v -c "system" /var/log/messages # Search not system and count line
grep -i -w -r "apache" /var
grep -i -w -r -l "apache" /var
```

# Running Basic Text Handling Commands
## Linux diff Command
- Compares two or more files line by line
- Reports the difference
- Example 1: app configuration file
-- File with latest timestamp not necessarily the correct one
-- Use diff to find the difference
- Example 2: shell script file
-- Use diff to compare with previous version
```
diff <option_1> <option_2> ... <option_n> <file_1> ... <file_n>
```
**Output**
```
file 1 line# a/c/d file2 line# 
</> Changed line's content
```
- Line number from first file, followed by "a", "c", or "d", followed by number from second file
-- a line needs to be added in this position in first file
-- c line needs to be changed in first file
-- d line needs to be deleted in the first file
- "<" mean: this line needs to be removed or changed in first file
- ">" mean: this line needs to be added to first file
**Example**
```
7a8
> Contents of line 8 from second file
```
- In the first file, after line 7, add the content of line 8 from the second fie
- The content of line 8 from the second file show after ">" symbol
```
1d0
< Contents of line 1 from first file
```
- In the first file, delete line 1, so both files can start with a common line
- The content of line 1 from the first file is shown after the "<" symbol
```
7c7
< Contents of line 7 from first file
> Contents of line 7 from second file 
```
- Change line 7 of the first file to make it same as line 7 of the second file
- The contents of line 7 from first file is shown after the "<" symbol
- The contents of line 7 from second file is shown after the ">" symbol

```
diff --color=always file1 file2
diff -y file1 file2
diff -c file1 file2
diff -u file1 file2
diff -q file1 file2
diff -i file1 file2
diff -B file1 file2
diff -w -c file1 file2
```

## Counting with wc
wc is Word Count - counts the number of words, lines and characters in a text file, or show its size in bytes. Can be used to quickly analyze a file
```
wc files
wc -m files # total number of characters in the file
wc -w files # total number of words in the file
wc -l files # total number of lines in the file
wc -L files # the length of the longest line in the file
wc -c files # size of the file in the number of bytes
wc files01 files02
```

## Line Numbering with nl
- Display file content with line numbers
- Without file name, diplays standard input value with line number
- Can help identify line breaks in files
- Can be useful for checking specific lines in program code for errors
```
nl files
nl -b a files
nl -v 10 -b a files
nl -v 10 -i 8 -b a files
nl -b a -s ". " files
nl -b a -s ". " -n rz files
nl -b a -s ". " -n rz -w 3 files
```

## Line Numbering with tr
- tr stands for translate
- Used for translating or deleting characters
- Does not translate between languages
- Transforms or formats text characters
```
cat file.txt | tr \[:lower:] \[:upper:]
```
### tr SETS
SETS are groups of characters that tell tr what to translate and how to translate it
```
cat file.txt | tr \[:lower:] \[:upper:] | tr \\t \,
cat file.txt | tr \[:lower:] \[:upper:] | tr \\t \, | tr -s \\n 
cat file.txt | tr \[:lower:] \[:upper:] | tr \\t \, | tr -s \\n > new_file.txt
```
## Ordering Text with sort
### Linux sort Command
- Sort text files: Both ascending and descending order
- Text and number: sort can order both types of data
- Columnar text files: Can sort by a specific column
### Sort Order
- Line starting with number appears before starting with letter
- Line starting with lowercase letter precedes line starting with uppercase letter
- Sort concatenates multiple file input before sorting
```
sort files.csv
sort -r files.csv
sort -k 1,2 files.csv | sort -o new_files.csv
sort -M month.csv
sort -n -k 2 -t \, files.csv
sort -n -k 2 -t \, -r files.csv
sort -u -f files.csv # find unique value
sort -c files.csv # Check file sorted
```
### Power of sort
- Basic: Can be used for basic text processing
- Advanced: Can be used with other commands for advanced functionality

## Finding Uniqueness with uniq
### Linux uniq Command
- Used to report or remove repeated lines of text
- Useful for cleansing data files before processing
- Comes with a number of options
```
uniq files.txt
```
**Remove Non-adjacent Repeats**
- Uniq can not remove non-adjacent repeated values
- Workaround: Sort the text and remove repeated values with uniq
```
sort files.txt | uniq
sort files.txt | uniq -i
sort files.txt | uniq -i -c
sort files.txt | uniq -i -c | sort -r
sort files.txt | uniq -i -d # Lines repeat in the files
sort files.txt | uniq -i -u # Lines not repeat in the files
```
### Other uniq Options
Scenario: file with multiple fields
- Ignore number of columns from beginning
- Use -f switch
Scenario: Ignore number of characters from beginning of each line
- Use -s switch with number of characters
- Useful for parsing time-stamped lines
- Use -c swich for number of repeats
- Pipe to "grep" for searching text

## Extracting text with cat
### Linux cut Command
- Cut: Used to extract selected parts of lines from one or more files
- CSV file: Created before
```
cut -f 1 -d \, files.csv
cut -f 1 -d \, files.csv | sort | uniq
cut -f 2 -d \, files.csv
cut -f 2,3 -d \, files.csv
```
- Files with non-columnar text content. Example: header or footer rows
- Default behavior of cut. Extract text from all lines. Result may not look nice
- Exclude non-delimited text content. Use "s" option with cut

## Merging Lines with paste
### Linux parse Command
- Used to merge lines from multiple files
- Not that paste - Not like the "paste" we know in Word
- Handy little tool - Can create new dataset from input files
- cat - Can also add up multiple file contents
- But paste - Merges lines vertically or horizontally
```
paste file1 file2
paste -d : file1 file2
paste -s file1 file2 #horizontally
```

## Joining files with join
### Linux join Command
- Special way of merging lines from two files
- Similar to SQL join command
- Lines from two files merged based on a common field
- Both files must be sorted by the common field
```
join --nocheck-order files1 files2
join -a 1 files1 files2
```

#Running Advanced Text Handling Commands
## Advanced Text Processing Needs
Complex filtering or sophisticated transformations need something more powerful
- Example 1: Selectively search and replace string in text file
- Example 2: Insert line at specific location in text file
- Example 3: Calculate total size of files in directory

## sed and awk
- Part of Unix-based systems since 1970s, also available for Linux
- sed: text stream editor with powerful search and replace capability
- awk: scripting language for text filtering, processing, reporting

## sed
- sed Stream Editor
- Powerful command for
-- Search and replace
-- Delete
-- Insert
-- Append
-- In-place edit
- Input stream can be a file
- Redirected command output
- Standard input from keyboard
**Advanced Feature**
- Searching for text using regular expression (like grep)
- Selectively applying changes to target text
- Editing file contents in single pass without opening in editor
- Fast and efficient operation
**sed Workflow**
- Input Stream -> (Read and Store) -> Pattern buffer -> (Apply) -> sed commands -> (Output) -> Standard output
**sed Learning Goal**
- Many options and commands available for sed
- Allows branching and looping like programming languages
- Advanced text processing with sed not covered in course
**Basic sed Syntax**
Inline sed commands examples
```
sed -e '<inline_sed_commands>' <target_file_name> 
sed -f '<sed_command_file>' <target_file_name>
```
**Filtering and Processing Text with sed**
```
sed -e 's/<regex_search_string>/<replacement_s_string>/<flags>' <file_name>
```
- sed's own command is within single quotes
- "s" is for substitude
- Regular expression after the first slash ("/") is the text pattern to search for
- Text after the second slash ("/") will replace any matching text
- Flags after the third slash ("/") controls how the change will be applied
- The target file is specified in the end
```
sed -e 's/Book: //' file
sed -e 's/book: //I' file # Case sensitive
sed -e '1,3 s/book: //I' file # 1 to 3 lines changed
sed -n '1,3 s/book: //Ip' file # printing of lines from pattern buffer, printing replace lines
sed -e 's/book: //I' -e 's/author: //I' file
sed -e '$ <string text>' file # Add new line in the end of file
sed -e '1 i <string text>' file # Add new line in the line 1 of file
```
```
sed \
-e 's/Book: //' \
-e 's/Author: //' \
-e 's/-/by/' \
-e '1 i test1' \
-e '1 i test2' \
file
```
```
sed -e '10,30d' file #delete line 10 to 30
sed -e '10,15p' file #show line 10 to 15
```

## awk
**Use Cases**
Not just for simple text processing
- Advanced filtering
- Data validations
- Custom transformations
- Formatted reports
- Mathematical functions
Linux shell scripts
- Condition branching, looping, variables, arrays
- Features present in awk as well
- Useful for specialized text handling
- awk scripts similar to shell scripts
**Basic awk Syntax**
awk can also process text from other input streams like stdin or pipes
```
awk <option_1>...<option_n> '/pattern/' {awk commands} <target_file1>...<target_filen>
awk <option_1>...<option_n> '/pattern/' -f <awk_command_file> <target_file1>...<target_filen>
```
**How awk works**
- An awk program is one or more pattern(s) and their associated action(s)
- Patterns can be regular expressions (e.g similar to one used with "grep")
- Data read one line at a time from input stream and pattern matched
- Associated action for the pattern performed on the matched line
**Awk Command**
```
{ aws commands }

BEGIN { initial awk commands }

{ main action block }

/regex pattern to be matched/

END { commands }
```
- awk commands are specified within "blocks", enclosed by curly brackets
- An optional "starter" block is created with the keyword "BEGIN"
- The commands in the main action block are run against the target text stream
- awk checks if there are text patterns to be matched
- Actions performed on matching records
- Original file remains intact
- Optional "END" block actions performed after main block of commands
```
BEGIN { var1="" } { command1; command2; } 
END { print "message" }
```
**Some awk Built-in Variables**
- Some can be assigned value at run time
- FS: field separator. Default value "\t"
-- awk considers each value separated by FS as a field
-- $0 = whole line, $1 = 1st field, $2 = 2nd field
- NF: Number of fields in current record
- NR: Current line number
- RS: Record separator. Default value "\n"
- FILENAME: Cureent file being processed
**Some awk Built-in Functions**
- print(): display message on screen
- length(): calculate length of an input string
- substr(): extract portion of a string
- gsub(): replace part of a string with another string
- index(): find position of a string within another string
- tolower(): convert text to lowercase
- toupper(): convert text to uppercase

```
awk 'BEGIN { print "Hello Learners!" }'
awk 'BEGIN { FS=":"; OFS="\t" } { print $1, $6 }' /etc/passwd
ls -l | awk 'BEGIN { sum=0 } { sum=sum+$5 } END { print sum }' /etc
ls -lR | awk 'BEGIN { sum=0 } { sum=sum+$5 } END { print sum }' /etc
date | awk 'BEGIN { print "Local Time UTC"; print "----------" } { print $4 }'
echo "Mary had a little lamb, little lamb, little lamb" | awk '{ print substr($0,1,4) }'
echo "Mary had a little lamb, little lamb, little lamb" | awk '{ print length($0) }'
echo "Mary had a little lamb, little lamb, little lamb" \
| awk '{ if(length($0) > 10) print "String too long"; else print length($0) }'
head file.csv | awk "BEGIN { FS="." } { print toupper($2) }"
awk "BEGIN { FS="." } /fiji/ { print $0 }" file.csv | sed -e 's/Fiji Dollar/Fijian Dollar/'
cat apache_logs | awk '{ print $9 }' | sort | uniq -c
```

# Reading and Writing to Text Files
## Shell Scripting
- A file with a series of Linux commands
- No structure, but needs to start with a pointer to shell executable
- Example script uses Bash shell, so need to point to the bash interpreter
- First executable line of script start with a #!. Example #!/bin/sh
## A Text Processing Shell Script Walkthrough
### Sample Shell Script
- File name: file.sh
- File extenstion: Based on shell (e.g .sh, .zsh, .csh)
