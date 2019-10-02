import random

class Student():
    def __init__(self, name, age=0,precourse_scores=0,passing_score=3.5,applied='yes'):
        self.name=name
        self.age= random.randint(18,56)
        self.precourse_scores= random.sample(range(1,6),5)
        self.passing_score=passing_score
        self.applied=applied
