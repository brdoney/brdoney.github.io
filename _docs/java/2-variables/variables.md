---
title: Variables
order: 3
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
