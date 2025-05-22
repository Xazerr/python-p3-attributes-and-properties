class Person:
    approved_jobs = ["Sales", "Engineer", "Artist", "Chef", "Teacher"]

    def __init__(self, name="John Doe", job="Sales"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
            # Don’t print
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
            # Don’t print
        else:
            print("Job must be in list of approved jobs.")


