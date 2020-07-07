---
title: First Program
order: 2
type: lesson
---

Write your first program with Java!

When you run the code below, the computer will automatically run the code inside of `main`, line-by-line.

```java
public class Main {
    public static void main(String args[]) {
        System.out.println("Hello World!");
        System.out.println("Goodbye!");
    }
}
```

Let's pick the two most important parts of this apart:

### The "Main Method"

```java
public class Main {
    public static void main(String args[]) {
        // Anything inside here is run one line after the other
        // So all the code we want to run goes in here
        // It can be as many lines as we want!
    }
}
```

Anything inside both curly brackets is run, line-by-line, when we run our program. If you don't put any code in between the curly brackets, nothing will run!

For now, you'll have to simply memorize how this is written so that you can write it whenever you create a new Java program, but later on, you'll understand why this works perfectly.

### Printing Messages

This is our first real instruction in Java! When we run our program, our program will output whatever we put in between the quotation marks (quotation marks look like `"`).

The word we use to describe this is "*printing*," because our program will be outputting something just like a regular printer.

```java
System.out.println("Anything in here is output");
```

### Putting It Together

So, if we put everything we've learned together, we end up with:

```java
public class Main {
    public static void main(String args[]) {
        System.out.println("Anything in here is output");
    }
}
```
