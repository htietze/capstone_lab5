from peewee import *

db = SqliteDatabase('chainsaw_db.sqlite')

class Juggler(Model):
    name = CharField()
    country = CharField()
    num_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} has a record of {self.num_catches} catches'

def main():
    db.connect()
    db.drop_tables([Juggler])
    db.create_tables([Juggler])

    mustonen = Juggler(name="Janne Mustonen", country='Finland', num_catches=98)
    mustonen.save()

    stewart = Juggler(name="Ian Stewart", country='Canada', num_catches=94)
    stewart.save()

    gregg = Juggler(name="Aaron Gregg", country='Canada', num_catches=88)
    gregg.save()

    taylor = Juggler(name="Chad Taylor", country='USA', num_catches=78)
    taylor.save()

    display_records()
    add_record()
    search_record()
    update_record()
    delete_record()
    display_records()


def display_records():
    print('Displaying records')
    jugglers = Juggler.select()
    for juggler in jugglers:
        print(juggler)

def add_record():
    print('Adding record')
    test = Juggler(name=input('Please enter a name: '), 
        country=input('Please enter their country: '), 
        num_catches=input('Please enter their record (as integer): '))
    print(test)
    test.save()

def search_record():
    print('Searching for record')
    record = Juggler.get_or_none(Juggler.name == input('Please enter a name to search: '))    
    print(record)

def update_record():
    print('Updating record')
    try:
        Juggler.update(num_catches=(int(input('Enter new record: ')))).where(Juggler.name == input('Name: ')).execute()
    except ValueError:
        print('Non-integer record entered or no record under that name found.')

def delete_record():
    print('Deleting record')
    Juggler.delete().where(Juggler.name == input('Name: ')).execute()

main()

""" So realizing my way of doing this isn't ideal because all the user inputs need more validation! so separating them
and then after validation, adding them to the peewee functions, is the better way to do it.
"""