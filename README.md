# factorial
Loving several factorial implementations

### The problem
https://en.wikipedia.org/wiki/Factorial

#### Some of the code is coming from comments at
####  https://stackoverflow.com/questions/5136447/function-for-factorial-in-python

## definition (recursive)

```python
def fact(n):
    """
    recursive
    """
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)
```

## for loop implementation
```python        
def factorial(n):
    """0, 1 ==> 1"""
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret
```

## while loop similar to what we found at stackoverflow
```python  
def fact_while1(n):
    """
    using while loop based on
    :param n:
    :return:
    """
    ret = 1
    if n == 0:
        return 1
    while True:
        if n == 1:
            return ret
        n, ret = n - 1, ret * n

```

## another while loop a little bit cleaner from my point of view
```python  
def fact_while2(n):
    ret = 1
    while n > 1:
        n, ret = n - 1, ret * n
    return ret
```

## recursive plus memoization implementation
```python  
def fact_memoization_gen():
    cache = {0: 1, 1: 1}

    def fact_memoization(n):
        ret = cache.get(n)
        if ret is None:
            ret = n * fact_memoization(n-1)
            cache[n] = ret
        return ret
    return fact_memoization
    
fact_memo = fact_memoization_gen()
```

### Using lambda and reduce(functional programming)

```python
import functools, operator
 
factorial_lambda = lambda n: functools.reduce(operator.mul, range(1, n+1), 1)
```

# reduce but without lambda
```python
import functools, operator

def factorial_reduce(n):
    return functools.reduce(operator.mul, range(1, n+1), 1)
```





## Eval implementation

```python  
def factorial_eval(n):
    """
    # Factorials are really just a range of numbers
    # multiplied by each other.
    #
    # So this one liners:
    # 1) converts a range (1,2,3...) to a string,
    # 2) removes the leading & closing brackets, and
    # 3) then multiplies the results together using eval.
    It fails when n = 126000
    :param n:
    :return:
    """
    lst = list(range(1, n+1))
    return eval(str(lst).replace(', ', '*')[1:-1:])

```

## Iterator so one can do infinite iterations over factorial numbers
```python  
def factorial_generator():
    i, ret = 0, 1
    yield ret
    while True:
        i += 1
        ret *= i
        yield ret

```

### Sample using generator
```python
for i, f in zip(range(25), factorial_generator()):
    print(i, f)
```

I don't know why you would do that but it is interesting

## Finite generator

```python
def factorial_finite_generator(n):
    i, ret = 0, 1
    while i <= n:
        yield ret
        i += 1
        ret *= i
        
for f in factorial_finite_generator(25):
    print(f)
```

# Results using cProfile
### factorial (for loop)
         4 function calls in 4.657 seconds

### fact_while2
         4 function calls in 5.062 seconds


### fact_while1(while True)
         4 function calls in 5.117 seconds

### factorial_lambda
         5 function calls in 4.589 seconds


### factorial_reduce
         5 function calls in 4.606 seconds


# Conclusions

* Recursive, Momeoization and eval don't work with a big n(126000) 
* Reduce implementation without lambda was a little bit faster than using lambda
* For loop and reduce implementations were the fastest in my MacPro



