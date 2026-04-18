# Sorting Assignment - Data Structures
By Elchay Avraham

## Algorithms Implemented
1. **Insertion Sort (ID: 3)** - O(n^2) complexity.
2. **Merge Sort (ID: 4)** - O(n log n) complexity.
3. **Quick Sort (ID: 5)** - O(n log n) complexity.

## Results
### Part B: Random Arrays
In `result1.png`, we can see that as the array size increases, Insertion Sort's execution time grows quadratically, while Merge and Quick sort remain significantly more efficient.

### Part C: Nearly Sorted Arrays
In `result2.png`, we compared the algorithms on arrays with 5% and 20% noise. We observed that Insertion Sort performs much better on nearly sorted data compared to random data.

## How to Run
To run the random experiment:
python run_experiments.py -a 3 4 5 -s 100 500 1000 5000 -e 1 -r 5

To run the noise experiment:
python run_experiments.py -a 3 4 5 -s 2000 -e 2 -r 5