---
title: User Input
order: 7
type: lesson
---

Let's add some interactivity! Scanners can be used to get input from the user, so we can do things like...

- Typing in word documents
- Controlling games
- Writing code

and many others! In order to get keyboard input from users, we use **Scanners**.

In the following table, `varName` should be replaced with the name of your Scanner variable.

| Type    | Scanner Function      |
| ------- | --------------------- |
| boolean | varName.nextBoolean() |
| char    | varName.nextChar()    |
| int     | varName.nextInt()     |
| double  | varName.nextDouble()  |
| String  | varName.nextLine()    |

## Example Code

```java
package com.company;

import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        // Instantiate Scanner
        Scanner sc = new Scanner(System.in);

        // String input
        System.out.print("Input your name: ");
        String name = sc.nextLine();

        // Numerical data input
        System.out.print("Input your age: ");
        int age = sc.nextInt();

        System.out.print("Input the amount of money you have: ");
        double money = sc.nextDouble();

        System.out.println("Hello" + name + "!");
        System.out.println("I heard you are " + age);
        System.out.println("And have $" + money + "in the bank");
    }
}
```
