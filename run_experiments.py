import time
import random
import numpy as np
import matplotlib.pyplot as plt
import argparse

# --- Part A: Algorithm Implementation ---

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left + middle + right

# --- Utilities ---

def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def generate_nearly_sorted_array(size, noise_level):
    arr = list(range(size))
    num_swaps = int(size * noise_level)
    for _ in range(num_swaps):
        idx1 = random.randint(0, size - 1)
        idx2 = random.randint(0, size - 1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def measure_time(sort_function, arr, repetitions):
    times = []
    for _ in range(repetitions):
        temp_arr = arr.copy()
        start_time = time.time()
        sort_function(temp_arr)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times), np.std(times)

def plot_results(sizes, results, errors, title, filename, xlabel):
    plt.figure(figsize=(10, 6))
    for name in results:
        plt.errorbar(sizes, results[name], yerr=errors[name], label=name, capsize=5, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel('Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
    print(f"Graph saved as: {filename}")

# --- Main Interface ---

def main():
    parser = argparse.ArgumentParser(description="Sorting Algorithm Experiments")
    parser.add_argument("-a", "--algorithms", nargs="+", type=int)
    parser.add_argument("-s", "--sizes", nargs="+", type=int)
    parser.add_argument("-e", "--exp_type", type=int, choices=[1, 2])
    parser.add_argument("-r", "--repetitions", type=int, default=5)

    args = parser.parse_args()

    algo_map = {
        3: ("Insertion Sort", insertion_sort),
        4: ("Merge Sort", merge_sort),
        5: ("Quick Sort", quick_sort)
    }

    selected_algos = [algo_map[i] for i in args.algorithms if i in algo_map]

    if args.exp_type == 1:
        results = {name: [] for name, _ in selected_algos}
        errors = {name: [] for name, _ in selected_algos}
        for size in args.sizes:
            print(f"Running Experiment 1 (Random), Size: {size}")
            arr = generate_random_array(size)
            for name, func in selected_algos:
                avg, std = measure_time(func, arr, args.repetitions)
                results[name].append(avg)
                errors[name].append(std)
        plot_results(args.sizes, results, errors, "Exp 1: Random Arrays", "result1.png", "Array Size (n)")

    elif args.exp_type == 2:
        noise_levels = [0.05, 0.20]
        results = {name: [] for name, _ in selected_algos}
        errors = {name: [] for name, _ in selected_algos}
        size = args.sizes[0]
        for noise in noise_levels:
            print(f"Running Experiment 2 (Noise {int(noise*100)}%), Size: {size}")
            arr = generate_nearly_sorted_array(size, noise)
            for name, func in selected_algos:
                avg, std = measure_time(func, arr, args.repetitions)
                results[name].append(avg)
                errors[name].append(std)
        plot_results(["5%", "20%"], results, errors, "Exp 2: Nearly Sorted", "result2.png", "Noise Level")

if __name__ == "__main__":
    main()