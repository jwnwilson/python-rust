import rust_factorial

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    

# Benchmark it
# generate 1M of random letters to test it
val = 15

def test_pure_python(benchmark):
    benchmark(factorial, val)

def test_rust(benchmark):
    benchmark(rust_factorial.factorial, val)

