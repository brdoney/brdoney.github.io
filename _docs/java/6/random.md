---
title: Random Numbers
order: 6
type: lesson
---

Random numbers are super useful when making games, writing security systems, and when doing calculations. In Java, they can be generated using **Random**.

Below, `varName` should be replaced with the name of your Random variable.

| Function                    | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| varName.nextInt(upperBound) | Generates random numbers between 0 and the (upperBound - 1) |

## Random Numbers Example Code

```java
package com.company;

import java.util.Random;

public class Main {
    public static void main(String[] args) {
        // Instantiate Random object
        Random rand = new Random();

        // Generate random integer in range 0 to 999
        int randInt = rand.nextInt(1000);

        // Print random integer
        System.out.println("Random Integer: " + randInt);
    }
}
```
