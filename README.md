# mock-all-things
Examples of using mock for python unit tests

Mock for python 2.7: http://www.voidspace.org.uk/python/mock/ (Lots of great examples in here, too)

From the library's homepage:

"mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

mock is now part of the Python standard library, available as unittest.mock in Python 3.3 onwards.

mock provides a core Mock class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel for creating unique objects. See the quick guide for some examples of how to use Mock, MagicMock and patch().

Mock is very easy to use and is designed for use with unittest. Mock is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by many mocking frameworks."

# Why Write Unit Tests?
Unit tests are 
Let's ask Google: https://www.google.com/search?q=what's+the+value+of+unit+tests

When in doubt, ask StackOverflow: http://stackoverflow.com/questions/67299/is-unit-testing-worth-the-effort

Some paraphrased highlights from that answer:
* Unit tests allow us to make changes to the code quickly (even big changes) and be confident that our changed code works.  All we need to do is refactor, re-run tests, update tests, and check that our coverage is 100%.  
* Even if you're not writing tests first (because you're not cool enough to practice pure TDD), tests let you know when to stop coding.  Passing tests give you confidence that your code is good enough for now.
* Unit tests help you thoroughly understand the design of the code you're working on.
* It's actually faster than doing manual tests (with no unit tests) once you get into a groove with it.
* Good unit tests help document the intended behavior of a function.  If the intent of a test is murky or complex, chances are the function is too complex.  If you're new to a codebase, good unit tests help explain the intended use/"flow" of a module.
* "Find a bug, write a test".  Once you have a bug fix with a unit test that specifically covers the case where the bug occurred, that specific bug is unlikely to ever appear again (and the test proves it).

Another good point about the business value of unit tests: http://www.daedtech.com/intro-to-unit-testing-10-the-business-value-of-unit-tests

One of the key points therein: In the modern software development world, it's generally accepted (probably) that you should write unit tests for most of your code.  Unit tests make us look legitimate, and having a robust suite of unit tests probably helps recruit people to work with you.

# How to Run this Code Example
This requires python virtualenv to be installed on your machine
```
cd mock-all-things/
mkdir env
virtualenv --python=/usr/bin/python2.7 --no-site-packages env/
pip install -r requirements.txt
```

# TODO
* Patch decorators
* Raising an exception with mock
* patch.object and patch.dict
* apply patch to TestCase class to mock the same thing in every test method (or start and stop)
* Autospec: "If you pass autospec=True to patch then it does the patching with a real function object. This function object has the same signature as the one it is replacing, but delegates to a mock under the hood. You still get your mock auto-created in exactly the same way as before. What it means though, is that if you use it to patch out an unbound method on a class the mocked function will be turned into a bound method if it is fetched from an instance. It will have self passed in as the first argument, which is exactly what I wanted:"
