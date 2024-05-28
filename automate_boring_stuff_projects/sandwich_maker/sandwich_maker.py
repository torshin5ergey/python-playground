'''
sandwich_maker.py - 

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''

import pyinputplus as pyip


class Sandwich:
    def __init__(self) -> None:
        self.bread = None
        self.protein = None
        self.cheese = None
        self.extra = []
        self.total_cost = 0

    bread_prices = {
            "wheat": 1.5,
            "white": 1,
            "sourdough": 1.75
        }
    protein_prices = {
            "chicken": 2.5,
            "turkey": 2.75,
            "ham": 2.5,
            "tofu": 2.25
        }
    cheese_prices = {
            "cheddar": 1,
            "Swiss": 1.25, 
            "mozarella": 1.5
        }
    extra_prices = {
            "mayo": 0.25,
            "mustard": 0.25,
            "lettuce": 0.5,
            "tomato": 0.5
        }
        
        
    def choose_bread(self, ask=True):
        if self.bread:
            self.alert_already_exists('bread')
        else:
            self.bread = pyip.inputMenu(list(self.bread_prices.keys()), 
                                        prompt = "What bread type would you prefer?\n",
                                        strip=True)
        

    def choose_protein(self, ask=True):
        if self.protein:
            self.alert_already_exists('protein')
        else:
            self.protein = pyip.inputMenu(list(self.protein_prices.keys()), 
                                        prompt = "What protein type would you prefer?\n",
                                        strip=True)


    def choose_cheese(self, ask=True):
        if self.cheese:
            self.alert_already_exists('cheese')
        else:
            if ask:
                with_cheese = pyip.inputYesNo("Would you like to add cheese (y/n)? \n",
                                              strip=True)
            else:
                with_cheese = 'yes'

            if with_cheese == 'yes':
                self.cheese = pyip.inputMenu(list(self.cheese_prices.keys()), 
                                             prompt = "What cheese would you prefer?\n",
                                             strip=True)


    def choose_extra(self, ask=True):
        # TODO: extra loop bug
        if self.extra:
            self.alert_already_exists('extra')
        if ask:
            with_extra = pyip.inputYesNo("Would you like to add extras (y/n)?\n",
                                        strip=True)
        else:
            with_extra = 'yes'
        
        if with_extra == 'yes':
            extra_available = list(self.extra_prices.keys())
            more = 'yes'
            while more == 'yes':
                extra = pyip.inputMenu(extra_available, 
                                       prompt = "What extra would you prefer?\n",
                                       strip=True)
                self.extra.append(extra_available.pop(extra))
                more = pyip.inputYesNo("Would you like to add more extras (y/n)?\n",
                                       strip=True)


    def alert_already_exists(self, param):
        prompt = f"{param.capitalize()} already chosen: {getattr(self, param)}. Would you like to modify it (y/n)?\n"
        do_modify = pyip.inputYesNo(prompt, strip=True)
        if do_modify == 'yes':
            self.rechoose(param)


    def rechoose(self, param):
        if param == 'extra':
            setattr(self, param, [])
        else:
            setattr(self, param, None)
        # Call method with name
        method_to_call = 'choose_' + param
        getattr(self, method_to_call)(ask=False)

    
    def calculate_total(self):
        
        try:
            # + bread
            self.total_cost += self.bread_prices[self.bread]
            # + protein
            self.total_cost += self.protein_prices[self.protein]
            # + cheese
            if self.cheese:
                self.total_cost += self.cheese_prices[self.cheese]
            # + extras
            if self.extra:
                for i in self.extra:
                    self.total_cost += self.extra_prices[i]
        except KeyError as e:
            print(f"Some sandwich parameter is empty. {e}")


def main():
    # Sandwich maker
    sandwich = Sandwich()
    #sandwich.choose_bread()
    #sandwich.choose_protein()
    #sandwich.choose_cheese()
    sandwich.choose_extra()
    sandwich.choose_extra()
    sandwich.calculate_total()
    print(sandwich.total_cost)
    print(vars(sandwich))


if __name__ == "__main__":
    main()
