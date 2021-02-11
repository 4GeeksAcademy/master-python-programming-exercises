  # `134` Access rights

## 📝 Instructions:

The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. For each file there is a known set of operations which may be applied to it:

write W,
read R,
execute X.

The first line contains the number N — the number of files contained in the filesystem. The following N lines contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files. For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

**Example input**
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog

**Example output**
OK
Access denied
Access denied
OK
OK

**Theory**
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/