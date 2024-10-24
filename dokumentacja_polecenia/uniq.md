# Linux uniq command 
`uniq`: Uniquify files

uniq writes the unique lines in the given input, or standard input if nothing is given or for an input name of ‘-’. Synopsis:

`uniq [OPTION]... [INPUT [OUTPUT]]`

By default, `uniq` prints its input lines, except that it discards all but the first of adjacent repeated lines, so that no output lines are repeated. Optionally, it can instead discard lines that are not repeated, or all repeated lines.

The input need not be sorted, but repeated input lines are detected only if they are adjacent. If you want to discard non-adjacent duplicate lines, perhaps you want to use ``sort -u.``
