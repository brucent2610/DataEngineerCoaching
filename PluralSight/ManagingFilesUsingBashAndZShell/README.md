#UNIX Filesystem
/
    /bin
        /bash
        /chmod
        /cp
        ...
    /etc
        /crontab
        /fstab
        /hosts
        ...
    /home
        /phong
        /bruce
        ...
    /var
        /cache
        /lib
        /log
        ...

#File Types
- Directories - contain other files
- Regular files
- Execute files
- Links - pointers to other files
- Device files - represent devices

#Globbing
```
ls *.*
ls *.?*
ls *.???*
ls [abc]*
ls [A-Z]*[a-z]
ls file*
ls file[1-4]*
ls file[A-Eabc]*
ls file[^A-Eabc]*
ls [mn]*(jpg|mp4|png)
```

#Locating files
```
find ~ -name ${name_of_file}
find ~ -name '${name_of_file}*' -type d
find ~ -name '*.mp4' -or -name '*.jpg'
```

#Processing lines
```
cut -d ':' -f 1 ${filename} | sort | uniq
cut -d ':' -f 1 ${filename} | sort | uniq | tr '[a-z]' '[A-Z]'
```

#Special File Permissions
**SUID (s or S)**
- File: Run file as a file owner
**GUID (s or S)**
- File: Run file as a member of the file group
- Directory: All of the files inside of it will belong to the directory group
**Sticky bit (t or T)**
- Directory: Prevents files inside of it from being removed by anyone but the owner of that file

#Linking Files
- Hard link: another file name that points to same file in memory
- Soft link: are just files that hold a file name of another file

#Grep - Searching text in files
```
grep -i '${string}' file
grep -ir '${string}' dir
```
**Note**
- Grep Mac (FreeBSD) different grep Linux (GNU grep) using different regex engines

#SED - Transform text with SED
- Stream editor
- Stream lines from input to output
- Executing operations on each line
```
sed 's/${find_string}/${replace_string}' file
sed -n 's/${find_string}/${replace_string}' file
sed -n 's/${find_string}/${replace_string}/p' file
sed -i 's/${find_string}/${replace_string}' file
sed -i '/${find_string}/{g;p}; h' file
```

#Diff - See file different
dfff ${file1} ${file2}

#Task Optimization
##Brace Expansion
```
touch file{1..50}
mkdir directory/{A..Z}
//Rename file
mv Documents/my_images/{image.jpg,new.jpg}
//Get many pages in web
wget https://files.example.org/file{001..5}.html
```
##Recursive file operations
```
cat file | xargs touch
find directory/ -name '*.bak' | xargs rm
```
##Cheking for destructive Operations
Using -i option for prompt to make sure operation
##Open Files with External Programs



