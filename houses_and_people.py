"""
File:         houses_and_people.py
Author:       Vu Nguyen
Date:         11/5/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs runs on two classes that where user
              can create as many object (person/address) as they
              want. Plus, user can also tell the person to enter
              which ever address they way and it'll display who
              is in what address and who isn't.
"""


class Person:
    # Constructor
    def __init__(self, name):
        self.name = name
        self.the_house = []

    # house in the parameter is an object
    def go_in(self, house):

        # This condition checks if this person is not already in the house
        if self.name in house.the_people:
            print('{} is already in the house'.format(self.name))
        else:
            house.the_people.append(self.name)
            self.the_house.append(self.name)

    # house in the parameter is an object
    def leave(self, house):

        # This condition checks to see if the person is not inside the house
        if self.name not in house.the_people:
            print('{} is not in the house'.format(self.name))
        else:
            house.the_people.remove(self.name)
            self.the_house.remove(self.name)


class House:
    # Constructor
    def __init__(self, address):
        self.address = address
        self.the_people = []

    def display(self):
        print("The house is at: {}".format(self.address))

        # This condition checks to see if there are any person in the house
        if self.the_people:
            for person in self.the_people:
                print('\t\t', person)


if __name__ == '__main__':
    print('The options are:\n\tcreate <person name>\n\tperson-name enter '
          'house-address\n\tperson-name exit house-address\n\tdisplay')
    in_string = input('What do you want to do? ')
    people_list = []
    house_list = []

    while in_string.strip().lower() not in ['quit', 'q']:
        enter_string = in_string.split('enter')
        exit_string = in_string.split('exit')
        if in_string.split()[0:2] == ['create', 'person']:
            people_list.append(Person(' '.join(in_string.split()[2:])))
            print('Person {} created'.format(people_list[-1].name))

        elif in_string.split()[0:2] == ['create', 'house']:
            house_list.append(House(' '.join(in_string.split()[2:])))
            print('House {} created'.format(house_list[-1].address))

        # This condition checks for the enter list ['Name ', ' house#']
        elif len(enter_string) == 2:
            if not any(enter_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(enter_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None

                # This loops cycle through every house address (string) to find the match input house string
                for house in house_list:
                    if house.address == enter_string[1].strip():
                        the_house = house
                # This loop cycles through every person name (string) to find the match input name string
                for person in people_list:
                    if person.name == enter_string[0].strip():
                        the_person = person
                # This condition checks that the person's name and addressed enter correctly
                if the_person and the_house:
                    the_person.go_in(the_house)
                else:
                    print('Something went wrong.  ')

        elif len(exit_string) == 2:
            if not any(exit_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(exit_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == exit_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == exit_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.leave(the_house)
                else:
                    print('Something went wrong.  ')

        elif in_string.lower().strip() == 'display':
            for house in house_list:
                house.display()
            print('These people aren\'t in a house')
            for person in people_list:
                if not person.the_house:
                    print(person.name)

        in_string = input('What do you want to do? ')
