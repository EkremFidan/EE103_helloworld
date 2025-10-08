import numpy as np

def say_hello():
    
    print("Hello World from EE103!")
    


if __name__ == "__main__":
    
    say_hello()

    print(f"Using NumPy version: {np.__version__}")

    arr = np.array([1, 2, 3])
    print("NumPy works. Sum =", arr.sum())

    print("düzenleme1")