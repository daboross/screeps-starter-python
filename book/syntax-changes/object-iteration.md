# dict Iteration

## Transcrypt vs. Python: iterating dicts

In Python, dictionaries are a special case - they have a different class than Object which allows for `[]` access to values, and iteration methods like `.keys()`, `.values()` and `.items()`.

In JavaScript, all objects are "dictionaries". Screeps-transcrypt has made the choice to by default keep all dictionaries created in Python regular JS objects for consistency between JS-created dicts and Python-created dicts.

While this is good for performance, it's not great for pythonic code. `.keys()`, `.values()` and `.items()` are not available in Transcrypt-python.

Instead, there are two possibilities:

## 1\) manually force things to be dictionaries

`dict()` method does exist, and will turn a regular object into a dictionary with right methods.

```python
my_stuff = dict({
    "a": b,
})
```

## 2\) use JS-style or lodash access

In JavaScript, lodash methods are often used for object iteration.

Instead of:

```python
for key, value in obj.items():
    print(key, value)
for key in obj.keys():
    print(key)
for value in obj.values():
    print(value)
```

You can use:

```python
for key, value in _.pairs(obj):
    print(key, value)
for key in Object.keys(obj): # or _.keys(obj)
    print(key)
for value in Object.values(obj): # or _.values(obj)
    print(value)
```

