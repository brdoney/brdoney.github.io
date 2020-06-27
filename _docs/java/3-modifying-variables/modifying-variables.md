---
title: Manipulating Variables
order: 6
type: lesson
---

Remembering things is great, but there's one important thing missing: changing what value the computer remembers.

For example, what if we have a variable that tracks a friend's age but that friend gets a year older?!?

Well, in Java, there are a couple of ways we can change variables after we have created them. In the following table, the variable declared below is used:

```java
int myVar = 1;
```

| Action | Example      | English                                    |
| ------ | ------------ | ------------------------------------------ |
| `=`    | `myVar=3;`   | Make myVar 3                               |
| `+=`   | `myVar+=14;` | Add 14 to the current value of myVar       |
| `++`   | `myVar++;`   | Add 1 to the current value of myVar        |
| `-=`   | `myVar-=9;`  | Subtract 9 from the current value of myVar |
| `--`   | `myVar--;`   | Subtract 1 from the current value of myVar |
| `*=`   | `myVar*=4;`  | Multiply the current value of myVar by two |
| `/=`   | `myVar/= 7;` | Divide the current value of myVar by 7     |

So a full program where we modify a variable after creating it might look something like this:

```java
public class Main {
    public static void main(String[] args) {
        int a = 1;
        System.out.println(a);
        a = 2;
        System.out.println(a);
        a++;
        System.out.println(a);
    }
}
```

Which would first print out `1`, then `2`, then `3`.
