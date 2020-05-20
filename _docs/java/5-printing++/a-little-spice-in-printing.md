---
title: A Little Spice in Printing
order: 8
type: lesson
---

There are some things that we haven't talked about so far, but that can make your programs much nicer.

## Printing without adding a new line

- `System.out.println` puts a blank line after it prints out your message
- `System.out.print` doesn't put a blank line after your message

This can be super useful when getting user input. For example,

```java
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter a word: ");
    String text = input.nextLine();
    System.out.println(text);
  }
}
```

Would print out the message "Enter a word: " and then ask for input, all on the same line!

## Putting variables in the middle of messages

Adding when working with Strings is special and super useful, because it lets us put variables in the middle of messages.

```java
public class Main {
  public static void main(String[] args) {
    int myNumber = 6;
    System.out.println("My favorite number is " + myNumber);
    System.out.println("Is your favorite number " + myNumber + "?");
    String favoriteNumString = "I can say that my favourite number is " + myNumber + "in variables too!";
  }
}
```
