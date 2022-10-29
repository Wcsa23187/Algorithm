[TOC]

# Black-Red-Tree

## 1.experiment content

Achieve the insert function of the  Black-Red-Tree , to this end , you need to complete the funtion 

- Insert a node in a Tree
- To fixed up the Tree to let it satisfy the attribute of Black-Red-Tree
- RotateRight and RotateLeft
- output : midTraverseTree , firstTraverseTree , levelTraverseTree (the same with the postoderTraverse)

## 2.The design of the Algrithm

I follow  the bible textbook - [**Introduction to Algorithms** *Third Edition*](https://mitpress.mit.edu/books/introduction-algorithms-third-edition), published by [Thomas H. Cormen](https://mitpress.mit.edu/contributors/thomas-h-cormen), [Charles E. Leiserson](https://mitpress.mit.edu/contributors/charles-e-leiserson), [Ronald L. Rivest](https://mitpress.mit.edu/contributors/ronald-l-rivest), and [Clifford Stein](https://mitpress.mit.edu/contributors/clifford-stein).

### a)  RotateLeft

![image-20221029154410041](C:\Users\王昌盛\AppData\Roaming\Typora\typora-user-images\image-20221029154410041.png)

### b)  RB-Insert

![image-20221029154430452](C:\Users\王昌盛\AppData\Roaming\Typora\typora-user-images\image-20221029154430452.png)

### c)  RB-INSERT-FIXUP

This part of content in the book has some intendation problems , so i will give a correct version of the pseudo code

```python
RB-INSERT-FIXUP(T, z)
1    while z.p.color == RED
2        if z.p == z.p.p.left
3            y = z.p.p.right
4            if y.color == RED
5                z.p.color = BLACK        // case 1
6                y.color = BLACK          // case 1
7                z.p.p.color = RED        // case 1
8                z = z.p.p                // case 1
9            else 
10               if z = z.p.right
11                   z = z.p              // case 2
12                   LEFT-ROTATE(T, z)    // case 2
13               z.p.color = BLACK        // case 3
14               z.p.p.color = RED        // case 3
15               RIGHT-ROTATE(T, z.p.p)   // case 3
16       else(same as then clause with "right" and "left" exchanged)
17   T.root.color = BLACK
```

## 3.Proof the Algorithm correctness test

we can get the result of  inTraverseTree and the midTraverseTree ,use these two results we can get a complete Tree

Through this way ,you can find that our Black-Red-Tree satisfies the attribution of Black-Red



