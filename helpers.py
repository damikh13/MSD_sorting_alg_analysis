import csv

def save_results_to_csv_diff_sizes(filename, results):
    # .csv header
    header = ['size', 'worst Time', 'avg time', 'best time', 'worst ops', 'avg ops', 'best ops']
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) # write the header
        for result in results:  # and the results
            writer.writerow([
                result['size'],
                result['worst_time'],
                result['avg_time'],
                result['best_time'],
                result['worst_ops'],
                result['avg_ops'],
                result['best_ops']
            ])
def save_results_to_csv_same_size(filename, results):
    header = ['time', 'ops']
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) # write the header
        for result in results:  # and the results
            writer.writerow([
                result['time'],
                result['ops'],
            ])
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

