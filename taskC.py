import random
import time
import os
import csv
import matplotlib.pyplot as plt
from taskA import gale_shapley, write_output

def generate_preference_list(n):
    pref = list(range(1, n + 1))
    random.shuffle(pref)
    return pref

def save_input_file(filename, hospitals, applicants, n):
    with open(filename, 'w') as f:
        f.write(f"{n}\n")
        
        for i in range(1, n + 1):
            line = ' '.join(map(str, hospitals[i]))
            f.write(line + "\n")
            
        for i in range(1, n + 1):
            line = ' '.join(map(str, applicants[i]))
            f.write(line + "\n")

def generate_data_for_n(n):
    hospitals = {}
    applicants = {}
    
    for i in range(1, n + 1):
        hospitals[i] = generate_preference_list(n)
        applicants[i] = generate_preference_list(n)
        
    return hospitals, applicants

def main():
    if not os.path.exists("data"):
        os.makedirs("data")
        
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    results = []
    
    print(f"{'N':<10} | {'Time (Seconds)':<15}")
    print("-" * 30)

    for n in sizes:
        filename_in = f"data/input_{n}.in"
        filename_out = f"data/output_{n}.out"
        
        hospitals, applicants = generate_data_for_n(n)
        
        save_input_file(filename_in, hospitals, applicants, n)
        
        start_time = time.time()
        result = gale_shapley(hospitals, applicants, n)
        end_time = time.time()
        
        duration = end_time - start_time
        results.append((n, duration))
        
        write_output(filename_out, result)
        
        print(f"{n:<10} | {duration:.5f}")
    
    with open("data/timing_results.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'time'])
        writer.writerows(results)
    
    print("\nTiming results saved to data/timing_results.csv")
    
    ns = [r[0] for r in results]
    times = [r[1] for r in results]
    
    plt.plot(ns, times, marker='o')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Gale-Shapley Algorithm Scalability')
    plt.grid(True)
    plt.savefig('data/scalability_graph.png')
    print("Graph saved to data/scalability_graph.png")
    plt.show()

if __name__ == "__main__":
    main()