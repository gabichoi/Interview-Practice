# Self-Practice
:smile:

## Tips:
* Think out loudly
* The less pseudocode, the better
* Try to improve solutions (simplicity and efficiency)
* Do not make assumptions
* Consider time and space complexities
* Be careful to invalid inputs, base cases and edge cases
---

## Index:
* [Data Structures](#data-structure)
    * [Array](#array)
    * [Linked List](#linked-list)
    * [Stack](#stack)
    * [Queue](#queue)
    * [Hashing](#hashing)
    * [Heap](#heap)
    * [Tree](#tree)
* [Algorithms](#algorithms)
    * [Array Sorting](#array-sorting)
        * [Insertion Sort](#insertion-sort)
        * [Selection Sort](#selection-sort)
        * [Merge Sort](#merge-sort)
        * [Quick Sort](#quick-sort)
    * [Graph Search](#graph-search)
        * [Breadth First Search](#breadth-first-search)
        * [Depth First Search](#depth-first-search)
        * [Dijkstra's Short Path Algorithm](#dijkstra's-short-path-algorithm)
* [Time Complexity](#time-complexity)
    * [Data Structure Runtime](#data-structure-runtime)
    * [Algorithm Runtime](#algorithm-runtime)
---

## Data Structures
### Array
|Topic |File |
|------|-----|
|Reverse an array without affecting items |[reverse_string.py](Array/reverse_string.py)|
|Merge two sorted lists |[merge_sorted_lists.py](Array/merge_sorted_lists.py)|
|Sum of non identical elements | [sum_of_elements.py](Array/sum_of_elements.py)|

### Linked List
|Topic |File |
|------|-----|
|Linked list class |[linked_list.py](LinkedList/linked_list.py)|

### Stack
* A new item is placed at the back 
* Only the item at the back can be acceessed at any item

### Queue
* A new item is placed at the last place
* Only the item at the front can be acceessed at any item

### Hashing

### Heap

### Tree
|Topic |File |
|------|-----|
|Tree class |[tree.py](Tree/tree.py)|
|Balanced Tree |[balanced_tree.py](Tree/balanced_tree.py)|
|Binary Tree class|[binary_tree.py](Tree/binary_tree.py)|
|Sum of all entries in the tree|[sum_of_entries.py](Tree/sum_of_entries.py)|
---

## Algorithms

### Array Sorting
#### Insertion Sort
For each item in the unsorted array, swap the item forward until it is in the correct position
* [insertion_sort.py](Array/insertion_sort.py)
* Best case: N (array is already ordered so only checking each item)
* Worst case: N^2 (array is reversed-sorted so swap for each item)

#### Selection Sort
For each item in the unsorted array, find and remove the smallest item and add it to the sorted array
* [selection_sort.py](Array/selection_sort.py)
* Best case: N^2 (compare each tiem with every other item)
* Worst case: N^2

#### Merge Sort
Base case: when an empty or one-item array is reached

Recurse body: 

1. Split the array to be sorted in half
2. Recursively call merge sort on each half
3. Merge the sorted half arrays
* [merge_sort.py](Array/merge_sort.py)
* Best case: NlogN 
* Worst case: NlogN 

#### Quick Sort
Base case: when an empty or one-item array is reached

Recursive body: 

1. Split the array into less-than-items and greater-tahn-items based on a pivot
2. Recursively call quicksort on each array
3. Merge the sorted arrays
* [quick_sort.py](Array/quick_sort.py)
* Base case runtime: NlogN (good pivot close to median)
* Worst case runtime: N^2 (bad pivot close to min or max)

### Graph Search
#### Breadth First Search
* [BFS.py](Graph/BFS.py)
* Queue used
* Visit nodes by level, top to bottom, left to right
#### Depth First Search
* [DFS.py](Graph/DFS.py)
* Stack used
* Visit deep nodes before shallow nodes
** Pre-order: node -> node.left -> node.right
** In-order: node.left -> node -> node.right
** Post-order: node.left -> node.right -> node
#### Dijkstra's Short Path Algorithm
* [Dijkstra.py](Graph/Dijkstra.py)
* With the association of weights (distance) and edges for each node, finds the shorest path from a starting vertex to all other nodes until the first visited item is visited again
---

## Time Complexity
### Data Structure Runtime
| Data Structure | Average Case | | | | Worst Case | | | |
|----------------|--------------|-|-|-|------------|-|-|-|
|  | Access | Search | Insert | Remove | Access | Search | Insert | Remove |
|Array|1|N|N|N|1|N|N|N|
|Stack|N|N|1|1|N|N|1|1|
|Queue|N|N|1|1|N|N|1|1|
|Linked List|N|N|1|1|N|N|1|1|
Binary Search Tree|logN|logN|logN|logN|N|N|N|N|

### Algorithm Runtime
| Algorithm | Best Case | Worst Case | Average Case |
|-----------|-----------|------------|--------------|
| Insertion Sort | N | N^2 | N^2 |
| Selection Sort | N^2 | N^2 | N^2 |
| Merge Sort | NlogN | NlogN | NlogN |
| Quick Sort | NlogN | N^2 | NlogN |


