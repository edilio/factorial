# factorial
Loving factorial implementations

### definition (recursive)

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



