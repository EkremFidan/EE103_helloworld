import numpy as np

from operations import add, subtract, multiply, divide


def say_hello():
    
    print("Hello World from EE103!")
    


if __name__ == "__main__":
    
    say_hello()

    print(f"Using NumPy version: {np.__version__}")

    arr = np.array([1, 2, 3])
    print("NumPy works. Sum =", arr.sum())

    print("düzenleme1")

    # ---- Yeni: operations.py fonksiyonlarını kullan ----
    a, b = 10, 3
    print(f"add({a}, {b}) =", add(a, b))
    print(f"subtract({a}, {b}) =", subtract(a, b))
    print(f"multiply({a}, {b}) =", multiply(a, b))

    # Bölme: 0'a bölmeyi örnekleyelim (hata yakalama ile)
    try:
        print(f"divide({a}, {b}) =", divide(a, b))
        print(f"divide({a}, 0) =", divide(a, 0))  # bu satır hata fırlatır
    except ValueError as e:
        print("divide hatası:", e)