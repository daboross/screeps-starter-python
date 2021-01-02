# Lodash Overview
[Lodash](https://lodash.com/) is a JavaScript library that provides utility methods for accomplishing tasks via functional programming.  Screeps supports Lodash in its entirety; while using it isn't a requirement, it can make accomplishing some tasks in game substantially easier.  


#### Syntax Basics
In respect to screeps, Lodash is useful when work needs to be performed on an object with numerous properties, or an array populated by objects (that also may have numerous properties).  A typical Lodash method takes the form of `_.lodashMethod(collection, function)` where `collection` is your object or array, and `function` is an anonymous function that will be invoked for each iteration on the provided `collection`.  

This syntax is similar to the `key` arguments supported by some of Python's built in functions like `sorted()`, `min()`, `max()`, and so on.  

##### Lambda Functions
The [Lodash Documentation](https://lodash.com/docs/4.17.5) provides a good overview of how to use each method, and what those can be used to accomplish.  While helpful examples are provided with each entry, Python's anonymous function syntax via [lambdas](http://www.secnetix.de/olli/Python/lambda_functions.hawk) must be used in place of JavaScript anonymous function syntax.  



