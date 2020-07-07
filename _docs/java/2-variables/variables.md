---
title: Variables
order: 4
type: lesson
---

Just like we remember things about the past, computers can remember things using variables.

To create a variable, we need to tell the computer three things:

- The variable's type
- The variable's name
- The variable's value

### Types

As people, we don't think about this often, but there are a bunch of different types of things we can remember. There are words, letters, numbers, and more!

Because computers are dumber than people, they need to keep closer track of the different types of things we tell them to remember.

That's why "_Types_" exist!

Look at the handy table and picture below to get to know the different data types.

| Type      | Real World | Example                          |
| --------- | ---------- | -------------------------------- |
| `String`  | Words      | "Hello World", "Goodbye!", "123" |
| `char`    | letters    | 'a', 'b', 'c', '?', '6'          |
| `int`     | Integers   | 1, -750, 120000                  |
| `double`  | Decimals   | 1.0, -14.61, 151253.131764       |
| `boolean` | Yes or No  | true, false                      |

### Variable Name

Think about when you remember something important, like your age:

Your age isn't just a number floating around in your head, because then it would be useless. Instead, without even having to think about it, you remember the number as your age.

Just like when you remember your age, a computer needs to connect a name to whatever you tell it to remember in order to make what it remembers meaningful.

This is what is called a variable's name. It can be anything, as long as it is a single word.

### Value

Last up is simply the thing you want to computer to remember. The only special thing to remember is that the value has to agree with the type of your variable. Look back at the table at the end of the ["Types" section](#types).

### Putting It All Together

Now that we know about types, a variable's name, and values, check out how we actually write and use variables:

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
