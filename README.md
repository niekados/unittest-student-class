# Unittest

In this video, I’ll introduce the `Student` class which we’ll be using for the remainder of this module.

- Let’s start by creating a file called `student.py`.  
Once created, I’ll go ahead and define a class called `Student` and add a docstring stating what it’s for.  
To allow us to define start and end dates, we’ll use two methods from the `datetime` module called `date` and `timedelta` which I’ll import at the top of the file.
- Next, we can define our `__init__` method. It will have three parameters: `self`, `first_name` and `last_name`.  
  Inside the `__init__` method, we can set `self._first_name` to be equal to `first_name` and `self._last_name` equal to `last_name`.

---
***NOTE***

As we want these to be read-only fields, we can prepend the `first_name` and `last_name` properties with an underscore so other developers know how it should be used.
`_first_name` 
---

We’ll also go ahead and define a `start_date` which will be set using the `date.today()` method.  
When an instance of our `Student` class is created, the `start_date` value is set using the time at the moment of the instance’s creation. In our fictional school, students will enroll for a year, so we can define `end_date` and set it equal to `date.today()` plus a `timedelta` of 365 days.  
This doesn’t allow for leap years, so if you want to improve this class at the end of the module, this might be something worth looking into.

Finally, we’ll add a field called `naughty_list` which is set to `False` initially. This is of course so we can let Santa know if a student misbehaves and redirect their presents to ourselves.

With the `__init__` method defined, we can go ahead and create a read-only method to get more detailed information about a student, such as the student’s full name.  
Let’s add a method called `full_name`, add `self` as a parameter and return an f-string consisting of `self._first_name` and `self._last_name` separated by a space.  
Since this is a method to get data only, I’ll add the `@property` decorator to our `full_name` method.

We will add more methods to our `Student` class in later videos, but we can see that our `Student` class can be extended to add a lot more functionality and I encourage you to try that at the end of the module to cement your knowledge of testing in Python while creating truly practical and usable code.

In this video, we created a `student.py` file with a `Student` class which will form the base of our tests. It has properties, sets values automatically on creating an instance of the class and has a method to return a student’s full name.

## Testing Methods and Properties

We’ll look at testing the `full_name` method of our `Student` class. Now that our `Student` class is in place, how would we go about testing it?  
If you thought that we would need to create an instance of the class first...  
Well done! Before we can do that, however, we need to do our basic setup of our test file.  
Using the knowledge you’ve gained so far, pause the video and create a file using the naming convention mentioned in an earlier video while also setting up an empty class for our tests.  
At this point, you should have a file called `test_student.py`, and our required imports including `unittest` and our `Student` class. A class named `TestStudent` that inherits from `unittest.TestCase` is also required. Though it isn’t required, I’ll add the same `if __name__ == "__main__": unittest.main()` statement we used before so we can run the file without having to specify the `unittest` module.

With that now in place, we can start creating our first test and we’ll do so for the `full_name` method. I’ll name the method `test_full_name` and pass in a reference to `self`.  
As mentioned earlier, we need to create an instance of the `Student` class in order to test it. I’ll name the instance `student` and make sure to pass in the `first_name` and `last_name` arguments of ‘John’ and ‘Doe’ respectively.

We can now use an `assertEqual` on the `student` instance to see whether calling the `full_name` method on it returns the expected value.   
In our case, the `first_name` and `last_name` properties separated by a space.  
If we now run our test, we can see that it passes. Great! That’s our first test done, so we’re well on our way towards extending the scope of our tests and `Student` class.  
In this video, we wrote the first test for our `Student` class. We created an instance of the class and asserted that the `full_name` method returns the correctly formatted student name. 

## Building a method using TDD - creating the first test

We’ll start using Test-Driven Development and create a test for a function called `alert_santa` that will change the `naughty_list` property to `True`.  
We don’t have the method we want to test yet, but we do know what we want it to do.  
If a student misbehaves for some inexplicable reason, we want to alert Santa by adding the student to his naughty list.  
When the class is instantiated, the `naughty_list` property is set to `False`.  
So, we know that the method we want to test will set the value of the `naughty_list` property to `True` and this makes it easily testable.  
Since we want to alert Santa, we’ll make a decision now to call that method `alert_santa` so we can use it in our tests before it’s been created.  
Following the naming convention for test methods, I’ll go ahead and create a method called `test_alert_santa` and pass in a reference to `self`.  
As before, we need to create an instance of our `Student` class and call it `student`.  
We’ve been using `assertEqual` methods up till now, but we’ll use a different assert for this test called `assertTrue`.  
The reason being that we know that we want the `alert_santa` method to set the value of the `naughty_list` property to `True` when called.  
With our `student` instance created, let’s call the `alert_santa` method on it.  
Now, we can use `self.assertTrue` to test whether `student.naughty_list` is `True`.  
Note that we don’t pass a second argument to `assertTrue` as it’s not comparing two values but simply checking whether an expression or value is `True`.  
What do you expect will happen if we run our tests now? Since our `alert_santa` method doesn’t exist in the `Student` class yet, we expect it to fail with an error. Let’s run the tests now and check that.  
And, as expected, it fails with an `AttributeError`. This completes the “red” stage of our red-green-refactor methodology.  
In this video, we started following the TDD principle and created a test called `test_alert_santa` that will test the behavior of a method called `alert_santa` that we still need to create in the `Student` class. 

## Building a method using TDD - creating the code

We’ll create the `alert_santa` method, rerun our tests and confirm that they’re passing.  
As seen in the previous video, we had a pretty good idea of what our `alert_santa` method needs to look like.  
It isn’t a read-only method and will modify the `naughty_list` property instead of returning a value. With this in mind we can create our method.  
Let’s create it below the `full_name` method.  
We’ll call it `alert_santa` to mirror the name used in our `test_alert_santa` method and pass in a reference to `self`. I’ll add `self.naughty_list` equals `True` to update the property value.  
With this in place, let’s run our tests again and see if they pass.  
And we can see that both of them do. Fantastic! We’ve now completed the “green” part of our red-green-refactor process for the `alert_santa` function.  
While we’re at it, let’s add another test and function. I’ll let you take the reins for this one and we can look at my implementation afterwards.  
What we want is a read-only method that will return a student’s email address. It will take the form `_first_name`.`_last_name@email.com`.  
For simplicity’s sake, all email addresses will end in `email.com`.  
You can create the test for this first, followed by the actual method itself in the `Student` class.  
If you’re uncertain how to proceed, use the `test_full_name` and `full_name` methods as reference.  
Pause the video now and work away on that and unpause to compare your code to mine.  
Welcome back. I’ll implement it quickly so you can reference my code.  
First, I’ll create a new test method called `test_email` with a reference to `self`.  
Inside it, I’ll create an instance of the `Student` class using the `first` and `last`
 name properties as before.  
Next, I’ll code our `assertEqual` and compare the output of `student.email` to the expected output.  
Email addresses use lowercase letters, so I’ll make sure to add a second argument to the assert with the first and last names values adjusted appropriately.  
To achieve this output, our `email` method will need to convert the first and last name properties to lowercase, so we’ll make sure to do that when the test is done.

Our test is looking good, so I’ll go ahead and add our `email` method to the `Student` class. As it’s a read-only method, I’ll add the `@property` decorator and call the method `email` with a reference to `self`.  
We just need to return a string that includes the `_first_name` and `_last_name` properties separated by a dot, followed by `email.com`. As mentioned earlier, the `_first_name` and `_last_name` values need to be converted to lowercase, so I’ll make sure to do that using the `lower()` string method.  
With that in place, I’ll run our tests again to confirm that they pass, which they do!

## Lifecycle of a Test

In this lesson, we’ll look at the lifecycle of a test—more specifically, how and when the tests are run and how instances are created and destroyed when running our tests.

At the moment, we’ve got quite a bit of repetition in our test functions. In every test, we’re manually creating the same student instance on which to perform our tests. This violates the DRY, or Don’t Repeat Yourself, principle. Our `TestStudent` class contains only a few test methods, but can you imagine how much code repetition we’d have if we had many more tests to run?

---
**NOTE**

Luckily for us, `Unittest` gives us two methods that will be run at the beginning and end of each test method. They are called `setUp` and `tearDown` respectively, are optional and are used to set up and teardown or destroy a testing environment for each test method. It’s important to note that these methods are defined using camel case instead of the conventional snake case which is used in Python. This is most likely due to it having been carried over from older legacy code. It’s important to declare them using camel case or they won’t run at all.

---

Since the `setUp` method runs before each test method, it would save us code repetition if we could define our student instance there so it can be available in each test method when it’s run.

Let’s go ahead and create the `setUp` method at the beginning of our `TestStudent` class and add a reference to `self`. Next, I’ll create a student instance as an instance variable, so it needs to be prepended with the `self` keyword. Just so we can see when the `setUp` method is run, I’ll add a print statement that’ll print “setUp” to the terminal.

```python
class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')
```

Since `student` is now an instance variable, we’ll need to go and change every reference to `self.student`. Now that the `student` instance will be created in the `setUp` method at the start of each test method, we can remove the student instantiations in each of them. I’ll also add a print statement to each test method which will print the method’s name to the terminal. This will allow us to see when our test methods are run relative to the `setUp` and `tearDown` methods.

```python
# code before
self.assertEqual(student.full_name, 'John Doe')

# code now 
self.assertEqual(self.student.full_name, 'John Doe')
```


We won’t be using any functionality that requires the use of the `tearDown` method, but you may be wondering what it’s for. Whereas the `setUp` method can be used to create temporary files and folders or set up a database connection during tests, the `tearDown` method would be used to remove temporary files or folders or close a connection to a database. As we don’t need any of that functionality, adding a simple statement to print “tearDown” will allow us to see when it is called behind the scenes.

Everything is now in place to test whether our setup works. Let's see what happens when we run our tests. Just as expected. For each test, we can see in order the following printed in the terminal: `setUp`, followed by the name of the test and finally, `tearDown`. This shows that the `setUp` method is run before each test, while the `tearDown` method is run after. The fact that all our tests still pass indicates that our `student` instance was indeed created successfully and that it was accessible within each test. It is interesting to note that the tests don’t run in the order we defined them. What is important, however, is that they do all get run.

Now consider we want to run code once at the beginning of our tests. We may want to do this to populate a test database with data, for example. We can’t use the `setUp` method as that gets called at the beginning of each test method. Fortunately, `Unittest` provides another method we can use for this particular use case called `setUpClass`. We can also use the `tearDownClass` method to destroy a test database, for instance, and this method will be run once at the end of our tests.

As we don’t have a particular use for it in our test, I’ll simply show you how to set up these methods and add print statements so we can see when they are run. At the top of our `test_student` file, I’ll go ahead and add `setUpClass` with a parameter of `cls` instead of `self`. I do this as `setUpClass` is a class method that affects the class itself instead of only an instance of the class as the `self` parameter would. Let’s add a print statement inside our method that will print `setUpClass` to the terminal when run. There is one more thing we need to add to make this a class method, and that is the `@classmethod` decorator. Just to reiterate, adding the `@classmethod` decorator to a method and passing `cls` as a method parameter will make it a class method which acts on the class instead of an instance of the class.

I’ll do the same thing for the `tearDownClass` method, but print `tearDownClass` inside the method instead. Let’s not forget to add the `@classmethod` decorator. We expect the `setUpClass` and `tearDownClass` methods to run once at the beginning and end of our tests instead of before and after each test method. With our print statements added, we should be able to verify that in the terminal, so let’s go ahead and run our tests again.

```python
@classmethod
def setUpClass(cls):
    print('setUpClass')

@classmethod
def tearDownClass(cls):
    print('tearDownClass')

```

And we can see `setUpClass` printed once at the beginning of our tests and `tearDownClass` at the end as expected. These `Unittest` methods are very powerful and will be of great use in your future projects. Knowing what you want to set up and when to do so will allow you to utilize the lifecycle of a test to your advantage.

In this lesson, you learned about the lifecycle of a test, including the `setUpClass` and `tearDownClass` methods that are run once at the beginning and end of our tests, as well as the `setUp` and `tearDown` methods that are run before and after each test method.


## Updating End Date with Extension

There are still properties in our `Student` class that aren’t really doing anything at the moment, and these are `start_date` and `end_date`. Until time travel is invented, there shouldn’t be a reason to change a student’s start date. It’s set automatically when we create an instance of the `Student` class, and as long as our time is set correctly, we won’t have to modify this value again.

The end date is another matter though. Due to unforeseen circumstances, none of which of course relate to time mismanagement by a student (cough cough), a short extension could be offered to help them finish the course. This is what you’re going to implement.

### Requirements

- Create a test called `test_apply_extension` that will assert whether a method called `apply_extension` updates a student’s `end_date` by adding a number of days to it. The number of days needs to be passed into `apply_extension` as an argument.
- Then create a method in the `Student` class called `apply_extension` that will have a parameter called `days` and will update a student’s `end_date` by adding the argument given as `days` to their original `end_date`.

Having a look at the `timedelta` documentation is also recommended. Pause the video now and try to implement that before coming back to see how I go about doing it.

### Implementation

In our test file (`test_student.py`), I’ll go ahead and create a new test method called `test_apply_extension` and pass in a reference to `self`. Before adjusting the `end_date`, I’ll store the current value for the student instance in a variable called `old_end_date`. Next, I’ll call the `apply_extension` method on `student` and pass in an argument of five for the number of days required. With that in place, I’ll call `assertEqual` and test whether `student`’s `end_date` is equal to the `old_date` plus a `timedelta` of five days.

If we run our tests now, we get an attribute error as expected. We haven’t created our `apply_extension` method yet, but we'll do that next.

In our `Student` class, I’ll go ahead and create a method called `apply_extension` and pass in a reference to `self` as well as a parameter called `days`. Inside the method, I’ll simply set `self.end_date` equal to `self.end_date` plus a `timedelta` where the `days` parameter equals the `days` argument we pass into the method. This will update the property value for us.

This is definitely simpler than the test method we had to create for it! If I go ahead and run our tests now, we can see that they all pass.


## Introduction to Mocking in Testing

In this class, we'll explore the concept of mocking and how it enhances our ability to test functionality that could fail due to factors beyond our control.

### Current Testing Scenario

So far, we've written comprehensive tests for our `Student` class. These tests are comprehensive because they shouldn’t fail due to external factors. However, what if our class relies on an external API call? What if the external server is down? How can we test for scenarios that we as developers can’t control?

Our methods may contain complex logic with `try-except` blocks or conditional statements that are difficult to satisfy. It can be challenging for developers to test the complete flow of logic through methods, especially when external dependencies cannot be intentionally caused to fail.

### The Role of Mocking

This is where mocking comes into play. The primary purpose of mocking is to focus on the behavior of the code being tested rather than the state or behavior of external dependencies.

In essence, mocking allows us to imitate the behavior of external factors, enabling us to confirm that our methods function as intended.

# Lesson: Testing a Student's Course Schedule with Mocking

We'll create a new method which will make a request to a fictional external API to retrieve a student’s course schedule. We’ll then write a test to mock this request to make sure our method behaves as expected when the request is successful and when it fails.

## Step 1: Create the Method to Retrieve Course Schedule

Before we start creating our method to retrieve a student’s course schedule, we need to import the `requests` module in our `student.py` file so we can use it to make a request to our fictional API service.

1. **Import the requests module**:
    ```python
    import requests
    ```

Now we can create our method, call it `course_schedule` and pass in a reference to `self`.

2. **Create the `course_schedule` method**:
    ```python
    class Student:
        def course_schedule(self):
            response = requests.get(f"https://fictional-api.com/students/{self._last_name}/{self._first_name}")
            if response.ok:
                return response.text
            else:
                return "Something went wrong with the request!"
    ```

Inside our new method, we make a `get` request to our fictional API using a student’s `_last_name` and `_first_name` in the URL and store the response in a variable called `response`. We can now check if the request was successful using `response.ok` and return the response content itself using `response.text`. To check for a failed response, we can add an `else` statement and return the message “Something went wrong with the request!”

## Step 2: Testing the Method with Mocking

So far, we haven’t used mocking at all. Our `course_schedule` method will handle successful and unsuccessful requests, but as we can’t control whether an external API is available or not, it would be impossible for us to test both cases for our method. This is where mocking comes into play as it will allow us to mock the request being both successful and unsuccessful.

In order for us to mock our `get` request, we need to import a method from `unittest.mock` called `patch` in our `test_student.py` file.

1. **Import `patch` from `unittest.mock`**:
    ```python
    from unittest.mock import patch
    import unittest
    from student import Student
    ```

We’ll create two tests for the `course_schedule` method: one to mock a successful request and another for an unsuccessful request. 

Let’s create the test for a successful request first, call it `test_course_schedule_success` and pass in a reference to `self`.

The `patch` method we’ve imported can be used as a decorator or a context manager. We’ll use a context manager for our test method. We know that we want to mock a `get` request in the student module, so we can write `with patch('student.requests.get') as mocked_get:` to set our context manager. This creates an object called `mocked_get` which we can use to test the `get` request functionality. Note that we’re importing the student class at the top of the file and that’s why we use `student.requests.get` to access it.

Remember that we aren’t making an actual call to an API, but mocking it instead. As such, we need to set certain values explicitly to mock successful or unsuccessful requests.

Since we’re testing a successful request, which values are we interested in if we look at the `course_schedule` method? Pause and think about it before continuing.

Well, we are interested in whether the response is `ok` and the response text. We can set these values in our `mocked_get` object as if it were a successful request. In order to do so, I’ll use `mocked_get.return_value.ok = True` as well as setting the response text to mock something being returned from the API. Here, I’ll just set the response text to “Success” using `mocked_get.return_value.text = "Success"`.

2. **Create the test for a successful request**:
    ```python
    class TestStudent(unittest.TestCase):
        def test_course_schedule_success(self):
            with patch('student.requests.get') as mocked_get:
                mocked_get.return_value.ok = True
                mocked_get.return_value.text = "Success"
                
                student = Student()
                schedule = student.course_schedule()
                
                self.assertEqual(schedule, "Success")
    ```

With that in place, let’s get the student’s course schedule and store it in a variable called `schedule`. We can now use `assertEqual` to compare the variable `schedule`, which should hold the returned response text for a successful call, with the string “Success”.

Let’s run our tests to make sure they’re passing. And we can see that they are.

I’ll let you create the test for a failed response. If we look at the logic of the `course_schedule` method, a failed request would happen if the response is not okay. You can also get the expected string which you can use as the `return_value.text` from the `course_schedule` method.

Pause and try to implement that. Compare your code to mine when you’re done.

So, I created a test called `test_course_schedule_failed` and set the `return_value.ok` to `False`. I then used the string “Something went wrong with the request!” from the `course_schedule` method in the `assertEqual` when comparing it to the return value in the `schedule` variable.

3. **Create the test for a failed request**:
    ```python
    class TestStudent(unittest.TestCase):
        def test_course_schedule_failed(self):
            with patch('student.requests.get') as mocked_get:
                mocked_get.return_value.ok = False
                
                student = Student()
                schedule = student.course_schedule()
                
                self.assertEqual(schedule, "Something went wrong with the request!")
    ```

Running our tests shows them all passing, so we’ve successfully tested successful and unsuccessful requests for our `course_schedule` method. We all deserve a massive pat on the back for making it this far, so here is a virtual one from me.

In this lesson, we implemented mocking to test successful and unsuccessful requests for our `course_schedule` method.
