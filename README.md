# Turing script
Turing script is interpreted programming language, that emulates turing machine. It's written in python(yes slow interpreted language in slow interpreted language).

Turing machine has infinite tape divided into cells, read/write device for the tape and states. All of this gives ability to execute any solvable algorithm. And all of these features are in Turing Script.

# Documentation
## Cycles
  Code in turing script runs in cycles, cycle begins right after the end of a previous one. But new cycle won't start, if previous cycle won't be finished, so it won't beggin, if halt happend. Cycle just runs all code in file and ends, when file ends or the halt is encountered.
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
  Cell is special state that represents current cell. Can be used in colon operators or with `var` keyword to change the current cell.

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
    invert cell;
  };
  ```

  ## Colon operators
  In `on` keyword condition colon operators is used, colon operators are ":" and "!:". First one checks if state equal to another state or value, second one is reversed ":".

  Example:
  ```
  on (cell !: 0) {
    halt;
  };
  on (_start : 1) {
    invert cell;
  };
  ```

  ## _start special state
  `_start` special state is used to run code in the first cycle of program or every cycle excpet first one. So in the first cycle its value will be 1, in all other ones it will be 0.

  Example:
  ```
  on (_start : 1) {
    halt;
  };
  ```
