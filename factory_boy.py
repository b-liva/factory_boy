import datetime
import factory


class Account:
    def __init__(self, username, email, date_joined):
        self.username = username
        self.email = email
        self.date_joined = date_joined

    def __str__(self):
        return '%s (%s)' % (self.username, self.email)


class Profile:

    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_UNKNOWN = 'u'  # If the user refused to give it

    def __init__(self, account, gender, firstname, lastname, planet='Earth'):
        self.account = account
        self.gender = gender
        self.firstname = firstname
        self.lastname = lastname
        self.planet = planet

    def __str__(self):
        return '%s %s (%s)' % (
            self.firstname,
            self.lastname,
            self.account.username,
        )


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)


class ProfileFactory(factory.Factory):
    class Meta:
        model = Profile

    account = factory.SubFactory(AccountFactory)
    gender = factory.Iterator([Profile.GENDER_MALE, Profile.GENDER_FEMALE])
    firstname = 'John'
    lastname = 'Doe'


class FemaleProfileFactory(ProfileFactory):
    gender = Profile.GENDER_FEMALE
    firstname = 'Jane'
    account__username = factory.Sequence(lambda n: 'jane%s' % n)
