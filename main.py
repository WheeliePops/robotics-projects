import time
import numpy as np

def main():
    print("Starting simulation...")
    start_time = time.time()

    for step in range(10):
        distance = np.random.uniform(0.1, 1.0)
        control_signal = 0.5 * (0.5 - distance)
        print(f"Step {step}: Distance={distance:.2f}, Control={control_signal:.3f}")
        time.sleep(0.1)

    print(f"Simulation completed in {time.time() - start_time:.1f}s")

if __name__ == "__main__":
    main()
