# del Operator

In python, `del list[0]` will delete the first item in the list, and truncate it.

The same is not true in Transcrypt. Transcrypt translates `del` directly to JavaScript's `delete`, so you'll end up with an incoheret list if you use this operator.

Instead, using the `pop` operator can work.

```python
# in regular python:
del list[0]
# in Screeps via Transcrypt:
list.pop(0)
```

If you need to delete a range, the JavaScript [`splice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice) method can help:

```python
# in regular python:
del list[1:3] # delete items 1 through 3, exclusive
# in Screeps via Transcrypt:
list.splice(1, 2) # delete 2 items, starting with index 1
```

