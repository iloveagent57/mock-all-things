# mock-all-things
Examples of using mock for python unit tests

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
* Something for side effect
* Test something that returns a generator
* Put return_value, side_effect inside Mock() init
* call_args_list
