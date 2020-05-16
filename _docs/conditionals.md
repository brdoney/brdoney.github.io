---
title: If Statements
order: 5
type: lesson
---

Sometimes we want the computer to be able to make decisions on its own. Maybe we want it to...

- Tell the user to bring an umbrella if it is going to be rainy
- Print "Goodbye!" when a user inputs "goodbye" with a Scanner
- Say "Good morning" if it is the morning or "Good night" if it is nighttime

To do this, we use "if statements". If statements follow the formula

```java
if (condition) {
    // If condition is true, run this code
    System.out.println("Hello from if!");
} else if (other condition) {
    // If the first condition was false but
    // this condition is true, run this code
    System.out.println("Hello from else if!");
} else {
    // If no conditions were true, run this
    System.out.println("Hello from else!");
}
```

There can be as many `else if` as we want, plus `else if` and `else` are both optional.

We can create conditions using a couple of operators

| Operator | Name                     |
| -------- | ------------------------ |
| `<`      | Less than                |
| `<=`     | Less than or equal to    |
| `>`      | Greater than             |
| `>=`     | Greater than or equal to |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `&&`     | and                      |
| `||`     | or                       |

For Strings, use `.equals()` instead of `==` and `!=`

## Example Code

```java
package com.company;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);

        // Get the user's favorite number
        System.out.print("Enter your favorite number: ");
        int favoriteNumber = myScanner.nextInt();

        // Print whether it is positive, zero, or negative
        if (favoriteNumber > 0) {
            System.out.println("That's a positive number");
        } else if (favoriteNumber == 0) {
            System.out.println("That's zero");
        } else {
            System.out.println("That's a negative number");
        }
    }
}
```
