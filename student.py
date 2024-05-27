from datetime import date, timedelta

class Student:
    """ A Student class as a basis for method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False


    @property   
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


    def alert_santa(self):
        self.naughty_list = True
    

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@mail.com"

    def apply_extension(self, extra_time):
        self.end_date = self.end_date + timedelta(days=extra_time)




mike = Student("Mike", "Test")
print(mike.end_date)
mike.apply_extension(20)
print(mike.end_date)