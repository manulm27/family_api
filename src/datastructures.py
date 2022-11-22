
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {   
                'id': 5,
                'first_name':'John Jackson',
                'age': '3 Years old',
                'Lucky_Numbers': [7, 13, 22]
            },
            {   
                'id': 7,
                'first_name':'Jane Jackson',
                'age': '35 Years old',
                'Lucky_Numbers': [10, 14, 3]
            },
            {   
                'id': 2,
                'first_name':'Jimmy Jackson',
                'age': '5 Years old',
                'Lucky_Numbers': [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member['id'] == '' or member['id'] == None:
            member['id'] = self._generateId()
        self._members.append(member)
        for x in self._members:
            if member['id'] == x['id']:
                return True
        pass

    def delete_member(self, id):
        member = None
        for x in self._members:
            if id == x['id']:
                member = x
        if member != None:
            self._members.remove(member)
            return True
        else:
            return False
        pass

    def get_member(self, id):
        for x in self._members:
            if id == x['id']:
                return x
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
