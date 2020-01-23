# Splay-Tree-
Data Structures &amp; Algorithms Project

self-adjusted binary tree which are roughly balanced having a time complexity of O(log n)

## Splaying Property - Splay()
Splaying a node of a tree is basically the process of bringing it to the root position by performing suitable rotations 
In Splay Trees after applying splay() operation , the tree rearranges itself in such a manner that the chosen node becomes the root.

## Function 1 - Insert()
In Insert operation new node is inserted in the tree like a Normal Binary Search Tree then after it Splaying operation is applied

-->> As you keep on inserting the new node it will become the root node . The last inserted will always be on root position due to continous splaying

## Function 2 - Search()
In Search operation the node is found like a normal Binary Ssearch Tree and then splayed to the root else if the node to be searched is not in the tree then the last node accessed prior to reaching the NULL is splayed and becomes the new root.

-->> Every time you will search a node it will be splayed and printed as root of tree . This will improve the time Complexity of the tree as the frequently accessed node will always be near or at the root position

## Function 3 - Delete()
In Delete operation , first the node will be found and then splayed and then deleted , after deletion the trees will be splitted into two by Split() then Join() would be applied.

## Advantages Of Splay Tree :
1 . It has "Caching Effect" as frequently accessed elements are always easily accessible due to contionus Splaying , it is used to implement Caches , Memory allocators etc.

2 . Easy implementation , unlike AVL & RB Tree it doesnt stores extra information

## Disadvantages Of Splay Tree :
1 . As they are not strictly balanced so height can become linear or skewed which makes O(n) but it happens in very rare cases

## References : 
1 . https://en.wikipedia.org/wiki/Splay_tree

2 . https://www.cs.usfca.edu/~galles/visualization/SplayTree.html

3 . https://www.youtube.com/watch?v=qMmqOHr75b8

4 . https://crab.rutgers.edu/~guyk/splay.ppt
