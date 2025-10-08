# operations.py
"""
Dört işlem fonksiyonlari: toplama, cikarma, carpma, bolme.
Bolme için 0'a bolme durumunda ValueError verir.
"""

def add(a, b):
    """Toplama"""
    return a + b

def subtract(a, b):
    """Cikarma"""
    return a - b

def multiply(a, b):
    """Carpma"""
    return a * b

def divide(a, b):
    """Bolme (b = 0 ise ValueError)"""
    if b == 0:
        raise ValueError("Sifira bolme hatasi: b = 0 olamaz.")
    return a / b
