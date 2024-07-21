# Simple Blockchain in Python
## Description

Small and simple blockchain project, written in Python. 
The project was created by following this [YT Tutorial](https://www.youtube.com/watch?v=pYasYyjByKI)


### How does it work

| Transaction | From   | To     | Amount    |
|-------------|--------|--------|-----------|
| t1          | Anna   | Andres | 2 SBCC    |
| t2          | Bob    | Joe    | 4.3 SBCC  |
| t3          | Mark   | Mark   | 3.2 SBCC  |
| t4          | Andres | Mark   | 0.15 SBCC |
| t5          | Mark   | Miguel | 1.25 SBCC |
| t6          | Joe    | Mark   | 0.77 SBCC |


```
BLOCK1 ("FirstBlock", t1, t2) --hash--> 76fd89
BLOCK2 ("76fd89", t3, t4) --hash--> 83jan3
BLOCK3 ("83jan3", t5, t6) --hash--> 6782ff
...

```