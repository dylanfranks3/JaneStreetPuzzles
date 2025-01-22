import random
import os
import json
import time
from multiprocessing import Pool, cpu_count
import string
import datetime
# Path to store progress files
PROGRESS_DIR = "progress"

def existsAPoint(blueX, blueY, redX, redY) -> bool:
    yIntercept = (
        -((redX - blueX) / (redY - blueY))
        + ((redX - blueX) / (redY - blueY)) * ((blueX + redX) / 2)
        + (blueY + redY) / 2
    )
    return 0 <= yIntercept <= 1

def pointOnTriangle():
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * 0.5 + t * 1 + u * 1,
        s * 0.5 + t * 1 + u * 0,
    )

def simulate_chunk(iterations, process_id):
    """
    Simulates a chunk of iterations, saves results to a file, and returns the results.
    """
    count = 0
    existsCount = 0
    for _ in range(iterations):
        redX, redY = random.uniform(0, 1), random.uniform(0, 1)
        blueX, blueY = pointOnTriangle()
        count += 1
        if existsAPoint(blueX, blueY, redX, redY):
            existsCount += 1

    # Save results to a file
    
    return existsCount, count

def save_progress(existsCount, count):
    """
    Save progress of a process to a file.
    """
    idValue = "-".join(
            [
                "".join(
                    random.choices(
                        string.ascii_letters + string.digits, k=random.randint(4, 12)
                    )
                )
                for i in range(5)
            ]
        )
    if not os.path.exists(PROGRESS_DIR):
        os.makedirs(PROGRESS_DIR)

    filepath = os.path.join(PROGRESS_DIR, f"process_{idValue}.json")
    with open(filepath, "w") as f:
        json.dump({"existsCount": existsCount, "count": count}, f)

def load_progress():
    """
    Load progress from all saved files.
    """
    total_existsCount = 0
    total_count = 0

    if not os.path.exists(PROGRESS_DIR):
        return total_existsCount, total_count

    for filename in os.listdir(PROGRESS_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(PROGRESS_DIR, filename)
            with open(filepath, "r") as f:
                data = json.load(f)
                total_existsCount += data["existsCount"]
                total_count += data["count"]

    return total_existsCount, total_count

def main():
    # Number of iterations per process
    iterations_per_process = 5000000
    # Number of processes to run (equal to the number of CPU cores)
    num_processes = cpu_count()

    
    
    # Start the simulation
    start_time = time.time()  # Track total elapsed time
    while True:  # Continuous loop
        
        iteration_start_time = time.time()  # Track time for this bulk iteration
        
        # Create a multiprocessing pool
        with Pool(num_processes) as pool:
            # Run simulations in parallel
            results = pool.starmap(
                simulate_chunk, [(iterations_per_process, i) for i in range(num_processes)]
            )

        currentRunExists = currentCount = 0

        # Combine results from this bulk process
        for existsCount, count in results:
            currentCount += existsCount
            currentRunExists += count
        
        save_progress(currentCount, currentRunExists )

        # Load existing progress
        total_existsCount, total_count = load_progress()
        print("Resuming from saved progress...")
        # Calculate the updated probability
        probability = total_existsCount / total_count

        # Calculate elapsed time
        iteration_elapsed = time.time() - iteration_start_time
        total_elapsed = time.time() - start_time

        # Print progress
        print("--- Bulk Process Completed ---")
        print(f"Total iterations: {total_count}")
        print(f"Probability so far: {probability}")
        print(f"Time for this process: {iteration_elapsed:.2f} seconds")
        print(f"Time this process finished: {datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
        print(f"Total elapsed time: {total_elapsed:.2f} seconds\n")

    

if __name__ == "__main__":
    main()
