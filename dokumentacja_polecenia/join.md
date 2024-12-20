
# linux join command - Documentation

`join`: Join lines on a common field

join writes to standard output a line for each pair of input lines that have identical join fields. Synopsis:

```join [option]… file1 file2```

Either file1 or file2 (but not both) can be ‘-’, meaning standard input. file1 and file2 should be sorted on the join fields.

```
$ cat file1
a 1
b 2
e 5

$ cat file2
a X
e Y
f Z

$ join file1 file2
a 1 X
e 5 Y
```

`join`’s default behavior (when no options are given):

-   the join field is the first field in each line;
-   fields in the input are separated by one or more blanks, with leading blanks on the line ignored;
-   fields in the output are separated by a space;
-   each output line consists of the join field, the remaining fields from file1, then the remaining fields from file2.