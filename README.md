# BraceDepth

# Purpose

This program will take an input file called input.txt which will contain a Java program and parse it and output an annotated version.
This program will track the nesting depth of the braces of the input file and will output an annotated version of the file. 

# Requirements

1. List the nesting depth of curly braces

2. Ignore braces inside quotes or comments

3. Test for unmatched braces (expected ‘}’ but found EOF); output an error message

4. Allow for multiple braces on the same line, for example “}}” ending a loop and a function

5. Handle block comments that cross multiple lines of the input file.

example: 
/* comment with 
ignored brace { */

Sample INPUT:
-------------------
import blah;
class Foo
{
     void Foo()
    {
       System.out.println("braces are fun! {{{{{");    // ignored
       if (condition)
       {
          // also ignored: { 
          int a = 1;
          // as is this: }
          if (condition){   int b = 1; } a = 42; 

      // what if this were on one line?  }}}
    }
} 
//end of program 


Sample annotated OUTPUT:
-------------
0 import blah;
0 class Foo
1 {
1    void Foo()
2    {
2        System.out.println("braces are fun! {{{{{"); // ignored
2        if (condition)
3        {
3            // also ignored: { 
3            int a = 1;
3            // as is this: }
3        }
2    }
1 }
0 // end of program

# Compile Instructions
