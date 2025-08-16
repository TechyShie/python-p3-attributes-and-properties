#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unkown", job="Marketing"):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, title):
        if not isinstance(title, str) or not 1 <= len(title) <= 25:
            print("Name must be string between 1 and 25 characters.")

        else:
           self._name = title.title()

        

    @property
    def  job(self):
            return self._job
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")

        else:
            self._job = value
    
