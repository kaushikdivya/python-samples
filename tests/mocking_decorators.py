# Mock the class implementing the decorator before importing the class using it.

# Example:

# decorator.py


class Decorator(object):

    def func(self):
        def wrap(f):
            print "I am in decorator"
            return f
        return wrap

# implement.py

from decorator import Decorator


class Implement(object):

    @Decorator.func
    def f(self):
        print "I am in f"


# test_Implement.py

# First approach
import unittest
from mock import Mock, patch
import decorator
# patch decorator before you import Implement
patch('decorator.Decorator.func', lambda y: y).start()
import Implement


# In case you have test suits and other tests are importing a module which
# imports the module implementing or using the decorator can overwrite the patch

# so either use the same patching as above or use the below code

# Below code reloads the tests and the class to be tests before running the
# tests


from unittest import TestCase
import implement  # Module with our thing to test
from decorator import Decorator  # Module with the decorator we need to replace
import imp  # Library to help us reload our UUT module
from mock import patch


class TestUUT(TestCase):
    def setUp(self):
        # Do cleanup first so it is ready if an exception is raised
        def kill_patches():  # Create a cleanup callback that undoes our patches
            patch.stopall()  # Stops all patches started with start()
            imp.reload(implement)  # Reload our UUT module which restores the original decorator
        self.addCleanup(kill_patches)  # We want to make sure this is run so we do this in addCleanup instead of tearDown

        # Now patch the decorator where the decorator is being imported from
        patch('decorators.Decorator.func', lambda x: x).start()  # The lambda makes our decorator into a pass-thru. Also, don't forget to call start()
        # HINT: if you're patching a decor with params use something like:
        # lambda *x, **y: lambda f: f
        imp.reload(implement)  # Reloads the uut.py module which applies our patched decorator

# The cleanup callback, kill_patches, restores the original decorator and
# re-applies it to the unit we were testing. This way, our patch only persists
# through a single test rather than the entire session -- which is exactly how
# any other patch should behave. Also, since the clean up calls patch.stopall(),
# we can start any other patches in the setUp() we need and they will get
# cleaned up all in one place.

