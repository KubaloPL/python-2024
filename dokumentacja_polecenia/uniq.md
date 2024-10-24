# Linux uniq command 
`uniq`: Uniquify files

uniq writes the unique lines in the given input, or standard input if nothing is given or for an input name of ‘-’. Synopsis:

`uniq [OPTION]... [INPUT [OUTPUT]]`

By default, `uniq` prints its input lines, except that it discards all but the first of adjacent repeated lines, so that no output lines are repeated. Optionally, it can instead discard lines that are not repeated, or all repeated lines.

The input need not be sorted, but repeated input lines are detected only if they are adjacent. If you want to discard non-adjacent duplicate lines, perhaps you want to use `sort -u.`

***

```
‘-f n’
‘--skip-fields=n’
```
Skip n fields on each line before checking for uniqueness. Use a null string for comparison if a line has fewer than n fields. Fields are a sequence of blank characters followed by non-blank characters. Field numbers are one based, i.e., -f 1 will skip the first field (which may optionally have leading blanks).

---
```
‘-s n’
‘--skip-chars=n’
```
Skip n characters before checking for uniqueness. Use a null string for comparison if a line has fewer than n characters. If you use both the field and character skipping options, fields are skipped over first.
***
```
‘-c’
‘--count’
```
Print the number of times each line occurred along with the line.
***
```
‘-i’
‘--ignore-case’
```
Ignore differences in case when comparing lines.
***
```
‘-d’
‘--repeated’
```
Discard lines that are not repeated. When used by itself, this option causes uniq to print the first copy of each repeated line, and nothing else.
***
```
‘-D’
‘--all-repeated[=delimit-method]’
```
Do not discard the second and subsequent repeated input lines, but discard lines that are not repeated. This option is useful mainly in conjunction with other options e.g., to ignore case or to compare only selected fields. The optional delimit-method, supported with the long form option, specifies how to delimit groups of repeated lines, and must be one of the following:


`‘none’`
Do not delimit groups of repeated lines. This is equivalent to --all-repeated (-D).

`‘prepend’`
Output a newline before each group of repeated lines. With --zero-terminated (-z), use a zero byte (ASCII NUL) instead of a newline as the delimiter.

`‘separate’`
Separate groups of repeated lines with a single newline. This is the same as using ‘prepend’, except that no delimiter is inserted before the first group, and hence may be better suited for output direct to users. With --zero-terminated (-z), use a zero byte (ASCII NUL) instead of a newline as the delimiter.

***
```
‘--group[=delimit-method]’
```
Output all lines, and delimit each unique group. With --zero-terminated (-z), use a zero byte (ASCII NUL) instead of a newline as the delimiter. The optional delimit-method specifies how to delimit groups, and must be one of the following:

`‘separate’`
Separate unique groups with a single delimiter. This is the default delimiting method if none is specified, and better suited for output direct to users.

`‘prepend’`
Output a delimiter before each group of unique items.

`‘append’`
Output a delimiter after each group of unique items.

`‘both’`
Output a delimiter around each group of unique items.

***

```
‘-u’
‘--unique’
```
Discard the last line that would be output for a repeated input group. When used by itself, this option causes uniq to print unique lines, and nothing else.

```
‘-w n’
‘--check-chars=n’
```
Compare at most n characters on each line (after skipping any specified fields and characters). By default the entire rest of the lines are compared.
