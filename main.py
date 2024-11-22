import time
import statistics

from array_generator import SimpleInputGenerator
from operation_counter import OperationCounter
from helpers import *
from msd_radix_sort import *

def run_experiment_diff_sizes(min_size, max_size, step, num_runs):
    simple_input_generator = SimpleInputGenerator()
    sizes = range(min_size, max_size + 1, step)
    results = []

    for cur_size in sizes:
        times = []
        operations = []
        for _ in range(num_runs):
            data = simple_input_generator.generate_data(cur_size)
            counter = OperationCounter()
            
            start_time = time.time()
            sorted_data = msd_radix_sort(data, counter)
            end_time = time.time()
            time_spent = end_time - start_time
            
            times.append(time_spent)
            operations.append(counter.count)
            assert is_sorted(sorted_data), "sorting failed"
        
        result = {
            'size': cur_size,
            'worst_time': max(times),
            'avg_time': statistics.mean(times),
            'best_time': min(times),
            'worst_ops': max(operations),
            'avg_ops': statistics.mean(operations),
            'best_ops': min(operations)
        }
        results.append(result)
        print(f"size: {cur_size:,}, avg Time: {result['avg_time']:.6f} s, avg Ops: {result['avg_ops']:.0f}")

    return results
def run_experiment_same_size(size, num_runs):
    simple_input_generator = SimpleInputGenerator()
    times = []
    operations = []
    for i in range(num_runs):
        data = simple_input_generator.generate_data(size)
        counter = OperationCounter()

        start_time = time.time()
        sorted_data = msd_radix_sort(data, counter)
        end_time = time.time()
        time_spent = end_time - start_time
        
        times.append(time_spent)
        operations.append(counter.count)
        assert is_sorted(sorted_data), "Sorting failed"

    results = [{'time': times[i], 'ops': operations[i]} for i in range(num_runs)]
    return results

if __name__ == "__main__":
    min_size = int(1e4)
    max_size = int(1e6)
    step = int(1e4)
    num_runs_for_each_size = 10
    results_diff_sizes = run_experiment_diff_sizes(min_size, max_size, step, num_runs_for_each_size)
    output_filename = "msd_results_diff_sizes.csv"
    save_results_to_csv_diff_sizes("msd_results_diff_sizes.csv", results_diff_sizes)
    print(f"results of MSD sorting random arrays with sizes from {min_size} to {max_size} with step {step} have been saved to '{output_filename}'")

    constant_size = 10000
    num_runs_for_constant_size = 10000
    results_same_size = run_experiment_same_size(constant_size, num_runs_for_constant_size)
    output_filename = f"msd_results_constant_size_of{constant_size}.csv"
    save_results_to_csv_same_size(output_filename, results_same_size)
    print(f"results of MSD sorting array with same size of {constant_size} have been saved to '{output_filename}'")