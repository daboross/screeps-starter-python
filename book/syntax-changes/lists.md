## Transcrypt vs. Python: list methods

Ideally, we'd have support for lists equivalent to Python itself. Unfortunately, this is not the case.

Three are three differences between Python and Screeps/Transcrypt lists.

## 1) In non-IVM Screeps, there are two types of lists.

If you're using the [IVM architecture], you can skip this section! The new architecture, when enabled on an account-level, fixes this problem.

Lists created within our code, in general, support python methods. Lists created outside of our code do not.

This means that if you are working with lists from `Memory`, lists from `room.fiynd()`, or any other non-user-javascript source, you won't be able to use Python prototype methods.

Instead, it's possible to use JavaScript methods. As painful as this is, it's a temporary workaround that does work:

```py
x = Memory.some_list

# won't work :(
x.append(3)
# does work, but isn't great
x.push(3)
```

The reason this is necessary is that the Screeps environment itself has two separate environments: the outside, where the game code exists, and our sandbox, where our code lives. We're allowed to add methods to types existing in our sandbox, but that doesn't translate to types outside the sandbox.

Memory, lodash, and all game methods are created outside our sandbox and thus don't have any of the prototype methods Transcrypt adds to lists.

[IVM architecture](http://blog.screeps.com/2018/03/changelog-2018-03-05/)

## 2) Negative indices don't work

For performance, Transcrypt translates indexing into lists directly into JavaScript indexing. This works most of the time, but fails for negative list indices.

```py
the_list = [1, 2, 3, 4]
# in Python:
assert the_list[-1] == 4
# in Transcrypt:
assert the_list[-1] == undefined # :(
# instead, you can use:
assert the_list[len(the_list) - 1] == 4
```

## 3) Slicing outside of an array bounds gives extra items

In regular Python, slicing outside of an array bounds will just give you till the end of the array. In Transcrypt, the same will pad the array with `undefined`.

```py
the_list = [1, 2]
# in Python:
assert the_list[:5] == [1, 2]
# in Transcrypt:
assert the_list[:5] == [1, 2, undefined, undefined, undefined]
```

There isn't a good fix for this besides just expecting this behavior.
