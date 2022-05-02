# Turing script
Turing script is interpreted programming language, that emulates turing machine. Its written in python(yes slow interpreted language in slow interpreted language).

Turing machine has infinit tape divided into cells, read/write device for tape and states. All of this gives ability to execute any solvable algorithm. And all of this is implemented in Turing Script.

# Documentation
## Cycles
  Code in turing script is ran at cycles, cycle beggins right after end of previous. But new cycle wont start, if previous cycle wont be finished, so it wont beggin, if halt happend. Cycle just runs all code in file and ends, when execution ended.
## Tape
  ## Left
  To move read/write device 1 cell left `left` keyword is used without any arguments. If cell was never touched before turing script will input this cell from user.

  Example: 
  ```
  left; 
  left; 
  right;
  left; 
  halt;
  ```
  ## Right
  To move read/write device 1 cell right `right` keyword is used without any arguments. If cell was never touched before turing script will input this cell from user.

  Example: 
  ```
  right;
  right;
  left;
  right;
  halt;
  ```
  ## Cell state
  Cell is special state that represents current cell. Can be used in colon operators or with `var` keyword to cnange current cell.

  Example:
  ```
  on (cell : 1) {
    var cell = 0;
    halt;
  };
  var state = cell;
  ```

## States
  ## var
  `var` keyword is used to set regular or special states with syntax `var name = val;`.

  Example:
  ```
  var cell = 1;
  var state = 0;
  halt;
  ```

  ## invert
  `invert` keyword is used for inverting regular or special state values.

  Example:
  ```
  var state = 0;
  invert cell;
  invert state;
  ```

## Conditional handlers
  ## on
  `on` keyword is used for creating conditional handlers with colon operators(: and !:) inside condition.

  Example:
  ```
  on (cell !: 0) {
    halt;
  };
  on (_start : 1) {
    inv cell;
  };
  ```

  ## Colon operators
  In `on` keyword condition colon operators is used, its ":" and ":!". First one checks if state equal to another state or value, second one is reversed ":".

  Example:
  ```
  on (cell !: 0) {
    halt;
  };
  on (_start : 1) {
    inv cell;
  };
  ```

  ## _start special state
  `_start` special state is used to run code in first cycle of pragram or every cycle excpet first. So in first cycle its value will be 1, in all other will be 0.

  Example:
  ```
  on (_start : 1) {
    halt;
  };
  ```