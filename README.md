# Interview-Practice
I can do it :)

## Self-Tips:
* Think out loudly
* Minimum pseudocode 
* Try to improve solutions (simplicity and efficiency)
* Do not make assumptions
* Consider time and space complexities
* Be careful to base and edge cases

## Index:
* [Data Structures](#data-structure)
* [Algorithms](#algorithms)
* [Runtime](#runtime)

## Data Structures:

### Array
### Linked List
### Heap
### Tree
#### Binary Search Tree
#### Binary Tree
### Graph
### Matrix
     
## Algorithms

### Array
#### Sorting
##### Insertion Sort
For each item in the unsorted array, swap the item backwards until it is in the correct position
* Best case: N (array is already ordered so only checking each item)
* Worst case: N^2 (array is reversed-sorted so swap for each item)
##### Selection Sort
For each item in the unsorted array, find and remove the smallest item and add it to the sorted array
* Best case: N^2 (compare each tiem with every other item)
* Worst case: N^2
##### Merge Sort
Base case: when an empty or one-item array is reached
Recurse body: split the array to be sorted in half, recursively call merge sort on each half, merge the sorted half arrays
* Best case: NlogN (
* Worst case: NlogN 
##### Quick Sort
Base case: when an empty or one-item array is reached
Recursive body: split the array into less-than-items and greater-tahn-items based on a pivot, recursively call quicksort on each array, merge the sorted arrays
* Base case runtime: NlogN (good pivot close to median)
* Worst case runtime: N^2 (bad pivot close to min or max)
#### Searching 

## Runtime
| Algorithm | Best Case | Worst Case | Average Case |
|-----------|-----------|------------|--------------|
Insertion Sort | N | N^2 | N^2 |
Selection Sort | N^2 | N^2 | N^2 |
Merge Sort | NlogN | NlogN | NlogN |
Quick Sort | NlogN | N^2 | NlogN |

