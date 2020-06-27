---
title: While Loops
order: 15
type: lesson
---

A lot of the time, we also want the computer to do the same actions over and over again.

Maybe we're...

- Printing out a message for the user repeatedly
- Playing a game over and over again
- Repeat an error message until the user gives valid input

To do this, we can use "while loops". While loops let us repeat the same code over and over if a condition is true. They use the following structure:

```java
while (condition) {
  // Repeat code in here
}
```

This is very similar to if statements! In fact, the way we make conditions is the same as with if statements.

## Example Code

```java
package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    Scanner myScanner = new Scanner(System.in);

    boolean userLikesIt = true;

    // Keep repeating until the userLikesIt is not true
    while (userLikesIt == true) {
        System.out.print("Input 1 to stop: ");
        int userNumber = myScanner.nextInt();

        // If the user inputted 1, make userLikesIt false
        if (userNumber == 1) {
            userLikesIt = false;
            }
        }
    }
}
```
