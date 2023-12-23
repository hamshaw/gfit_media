class Profile:
    def __init__(self):
        self.user_name = user_name
        self.birthday = {'month': None, 'day': None, 'year': None}
        self.sizes = {'shirt': None, 'pants':'Mshoes': None, 'Wshoes': None, }
        self.allergies = ['1']
        self.color = ()##tuple with RGB value
        self.hobbies = []

    def set_birthday(self, month, day, year):
        ##make it check that its a legit date
        if self.legit_date(month, day, year):
            self.birthday[month] = month
            self.birthday[day] = day
            self.birthday[year] = year
        else:
            raise("birthday must be valid date")

    def set_sizes(self, item, size):
        ##add checks
        self.sizes[item] = size

    def change_allergies(self, action, allergy):
        if action = 'add':
            if allergy not in self.allergies:
                self.allergies.append(allergy)
            else:
                raise("allergy already known")
        elif action = 'drop':
            if allergy in self.allergies:
                self.allergies.remove(allergy)
            else:
                raise('allergy does not need to be dropped')
        else:
            raise('action must be "add" or "drop"')

    def set_color(self, color):
        if color.is_tuple():
            self.color = color
        else:
            raise('color should be an RGB tuple')

    def change_hobbies(self, action, hobby):
        if action = 'add':
            if hobby not in self.hobbies:
                self.hobbies.append(hobby)
            else:
                raise("hobby already shown")
        elif action = 'drop':
            if hobby in self.hobbies:
                self.hobbies.remove(hobby)
            else:
                raise('hobby does not need to be dropped')
        else:
            raise('action must be "add" or "drop"')




