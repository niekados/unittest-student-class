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

Luckily for us, `Unittest` gives us two methods that will be run at the beginning and end of each test method. They are called `setUp` and `tearDown` respectively, are optional and are used to set up and teardown or destroy a testing environment for each test method. It’s important to note that these methods are defined using camel case instead of the conventional snake case which is used in Python. This is most likely due to it having been carried over from older legacy code. It’s important to declare them using camel case or they won’t run at all.

Since the `setUp` method runs before each test method, it would save us code repetition if we could define our student instance there so it can be available in each test method when it’s run.

Let’s go ahead and create the `setUp` method at the beginning of our `TestStudent` class and add a reference to `self`. Next, I’ll create a student instance as an instance variable, so it needs to be prepended with the `self` keyword. Just so we can see when the `setUp` method is run, I’ll add a print statement that’ll print “setUp” to the terminal.

Since `student` is now an instance variable, we’ll need to go and change every reference to `self.student`. Now that the `student` instance will be created in the `setUp` method at the start of each test method, we can remove the student instantiations in each of them. I’ll also add a print statement to each test method which will print the method’s name to the terminal. This will allow us to see when our test methods are run relative to the `setUp` and `tearDown` methods.

We won’t be using any functionality that requires the use of the `tearDown` method, but you may be wondering what it’s for. Whereas the `setUp` method can be used to create temporary files and folders or set up a database connection during tests, the `tearDown` method would be used to remove temporary files or folders or close a connection to a database. As we don’t need any of that functionality, adding a simple statement to print “tearDown” will allow us to see when it is called behind the scenes.

Everything is now in place to test whether our setup works. Let's see what happens when we run our tests. Just as expected. For each test, we can see in order the following printed in the terminal: `setUp`, followed by the name of the test and finally, `tearDown`. This shows that the `setUp` method is run before each test, while the `tearDown` method is run after. The fact that all our tests still pass indicates that our `student` instance was indeed created successfully and that it was accessible within each test. It is interesting to note that the tests don’t run in the order we defined them. What is important, however, is that they do all get run.

Now consider we want to run code once at the beginning of our tests. We may want to do this to populate a test database with data, for example. We can’t use the `setUp` method as that gets called at the beginning of each test method. Fortunately, `Unittest` provides another method we can use for this particular use case called `setUpClass`. We can also use the `tearDownClass` method to destroy a test database, for instance, and this method will be run once at the end of our tests.

As we don’t have a particular use for it in our test, I’ll simply show you how to set up these methods and add print statements so we can see when they are run. At the top of our `test_student` file, I’ll go ahead and add `setUpClass` with a parameter of `cls` instead of `self`. I do this as `setUpClass` is a class method that affects the class itself instead of only an instance of the class as the `self` parameter would. Let’s add a print statement inside our method that will print `setUpClass` to the terminal when run. There is one more thing we need to add to make this a class method, and that is the `@classmethod` decorator. Just to reiterate, adding the `@classmethod` decorator to a method and passing `cls` as a method parameter will make it a class method which acts on the class instead of an instance of the class.

I’ll do the same thing for the `tearDownClass` method, but print `tearDownClass` inside the method instead. Let’s not forget to add the `@classmethod` decorator. We expect the `setUpClass` and `tearDownClass` methods to run once at the beginning and end of our tests instead of before and after each test method. With our print statements added, we should be able to verify that in the terminal, so let’s go ahead and run our tests again.

And we can see `setUpClass` printed once at the beginning of our tests and `tearDownClass` at the end as expected. These `Unittest` methods are very powerful and will be of great use in your future projects. Knowing what you want to set up and when to do so will allow you to utilize the lifecycle of a test to your advantage.

In this lesson, you learned about the lifecycle of a test, including the `setUpClass` and `tearDownClass` methods that are run once at the beginning and end of our tests, as well as the `setUp` and `tearDown` methods that are run before and after each test method.


