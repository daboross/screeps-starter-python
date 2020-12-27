# in Opperator

In regular python, `in` opreators on lists, objects, and generally any container object. It also supports overloading via the `__contains__` method.

Transcrypt's `in` operator supports neither of these things. In order to achieve better performance when used with dicts \(javascript "object"s\), it behaves very similarly to JavaScript's `in` operator.

It will work the same on dictionaries, but does not support lists, and does not support custom containers.

To find whether a list contains an item or a string contains a sub-string, one can use the [`includes`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes) method:

```python
# in regular python:
if ('x' in 'asdf'
        and 'the_key' in the_dict 
        and 'the_item' in the_list):
    pass
 # in Screeps via Transcrypt:
 if ('asdf'.includes('x')
         and 'the_key' in the_dict
         and the_list.includes('the_item')):
     pass
```

