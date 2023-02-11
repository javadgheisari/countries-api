from mongoengine import *

class Country(Document):
    code = IntField(required=True)
    name = StringField(max_length=50)
    population = IntField()
    region = StringField(max_length=50)

    # def _init__(self, id, name, people, continent):
    #     self.studentid=id
    #     self.name=name
    #     self.people=people
    #     self.continent=continent