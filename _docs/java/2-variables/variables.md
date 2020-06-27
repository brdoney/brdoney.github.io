---
title: Variables
order: 4
type: lesson
---

Just like we remember things about the past, computers can remember things using variables.

To create a variable, the computer needs us to tell it three things:

- The variable's type
- The variable's name
- The variable's value

Look at the handy table and picture below to get to know the different data types and what to write to create a variable.

| Type      | Real World | Example                          |
| --------- | ---------- | -------------------------------- |
| `String`  | Words      | "Hello World", "Goodbye!", "123" |
| `char`    | Characters | 'a', 'b', 'c', '?', '6'          |
| `int`     | Integers   | 1, -750, 120000                  |
| `double`  | Decimals   | 1.0, -14.61, 151253.131764       |
| `boolean` | Yes or No  | true, false                      |

![Variable formula](/assets/images/variable_formula.png)

Variables can also be printed out just like raw values:

```java
public class Main {
    public static void main(String[] args) {
        int a = 1;
        System.out.println(a);
    }
}
```

If we have two variables that store numbers of the same type (so there are either two `double` or two `int`), we can even add, subtract, multiply, and divide them as well!

```java
public class Main {
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        int c = a + b;
        System.out.println(c);
    }
}
```

To do something other than add, just switch out the `+` symbol with the correct symbol from the table below:

| Symbol | Operation |
| ------ | --------- |
| `+`    | Add       |
| `-`    | Subtract  |
| `*`    | Multiply  |
| `/`    | Divide    |
