
In this video, I’ll introduce the Student class which we’ll be using for the remainder of this module.

- Let’s  start by creating a file called student.py.   
Once created, I’ll go ahead and define a class called  Student and add a docstring stating what it’s for.
To allow us to define start and end  dates, we’ll use two methods from the  
datetime module called date and timedelta  which I’ll import at the top of the file.
- Next, we can define our init method. It will have  three parameters: self, first_name and last_name.  
Inside the init method, we can set  self._first_name to be equal to first_name  
and self._last_name equal to last_name.

---
***NOTE***

As we want these to be read-only  fields, we can prepend the first_name  
and last_name properties with an underscore so  other developers know how it should be used.
`_first_name` 
---


We’ll also go ahead and define a start_date  which will be set using the date.today() method.  
When an instance of our Student class is created,  the start_date value is set using the time at  
the moment of the instance’s creation. In our  fictional school, students will enroll for a year,  
so we can define end_date and set it equal  to date.today() plus a timedelta of 365 days.  
This doesn’t allow for leap years, so if you want  to improve this class at the end of the module,  
this might be something worth looking into.
Finally, we’ll add a field called naughty_list  which is set to False initially. This is of course  
so we can let Santa know if a student misbehaves  and redirect their presents to ourselves.
With the init method defined, we can  go ahead and create a read-only method  
to get more detailed information about a  student, such as the student’s full name.  
Let’s add a method called full_name,  add self as a parameter and return an  
f-string consisting of self._first_name  and self._last_name separated by a space.  
Since this is a method to get data only, I’ll add  the @property decorator to our full_name method.
We will add more methods to our  Student class in later videos,  
but we can see that our Student class can  be extended to add a lot more functionality  
and I encourage you to try that at the end  of the module to cement your knowledge of  
testing in Python while creating  truly practical and usable code.
In this video, we created a student.py file  with a Student class which will form the  
base of our tests. It has properties, sets values  automatically on creating an instance of the class  
and has a method to return a student’s full name.