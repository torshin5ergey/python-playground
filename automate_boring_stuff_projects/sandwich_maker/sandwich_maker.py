'''
sandwich_maker.py - 

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
'''

import pyinputplus as pyip


class Sandwich:
    """Sandwich and its properties."""
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
        
        
    def choose_bread(self, ask=True) -> None:
        """Choose the type of bread for the sandwich."""
        if self.bread:
            self.alert_already_exists('bread')
        else:
            self.bread = pyip.inputMenu(list(self.bread_prices.keys()), 
                                        prompt = "What bread type would you prefer?\n",
                                        strip=True)
        

    def choose_protein(self, ask=True) -> None:
        """Choose the type of protein for the sandwich."""
        if self.protein:
            self.alert_already_exists('protein')
        else:
            self.protein = pyip.inputMenu(list(self.protein_prices.keys()), 
                                          prompt = "What protein would you prefer?\n",
                                          strip=True)


    def choose_cheese(self, ask=True) -> None:
        """Choose the type of cheese for the sandwich."""
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


    def choose_extra(self, ask=True) -> None:
        """Choose extras for the sandwich."""
        if self.extra:
            self.alert_already_exists('extra')
            return
        if ask:
            with_extra = pyip.inputYesNo("Would you like to add extras (y/n)?\n",
                                         strip=True)
        else:
            with_extra = 'yes'
        
        if with_extra == 'yes':
            extra_available = list(self.extra_prices.keys())
            while True:
                # If extra has one element
                if len(extra_available) == 1:
                    extra = pyip.inputYesNo(f"Would you like to add {extra_available[0]} (y/n)?\n",
                                        strip=True)
                    if extra == 'yes':
                        self.extra.append(extra_available[0])
                    break

                # If extra has more than one element
                else:
                    extra = pyip.inputMenu(extra_available, 
                                       prompt = "What extra would you prefer?\n",
                                       strip=True)
                    self.extra.append(extra)
                    extra_available.remove(extra)
                    more = pyip.inputYesNo("Would you like to add more extras (y/n)?\n",
                                        strip=True)
                    if more == 'no':
                        break


    def alert_already_exists(self, param) -> None:
        """Alert if the parameter already exists."""
        current_param = getattr(self, param)
        if isinstance(current_param, list):
            existed = ', '.join(current_param)
        else:
            existed = current_param
        prompt = f"{param.capitalize()} already chosen: {existed}. Would you like to modify it (y/n)?\n"
        do_modify = pyip.inputYesNo(prompt, strip=True)
        if do_modify == 'yes':
            self.rechoose(param)


    def rechoose(self, param) -> None:
        """Rechoose a parameter."""
        if param == 'extra':
            setattr(self, param, [])
        else:
            setattr(self, param, None)
        # Call method with name
        method_to_call = 'choose_' + param
        getattr(self, method_to_call)(ask=False)

    
    def calculate_total(self) -> None:
        """Calculate total cost of the sandwich."""
        try:
            # + bread
            if not self.bread:
                print("Please, choose bread type.")
                self.choose_bread()
            self.total_cost += self.bread_prices[self.bread]

            # + protein
            if not self.protein:
                print("Please, choose protein.")
                self.choose_protein()
            self.total_cost += self.protein_prices[self.protein]

            # + cheese
            if self.cheese:
                self.total_cost += self.cheese_prices[self.cheese]
            
            # + extras
            if self.extra:
                for i in self.extra:
                    self.total_cost += self.extra_prices[i]
        except KeyError as e:
            print(f"Some required sandwich parameter is empty. {e}")


def main():
    # Make a sandwich
    sandwich = Sandwich()
    sandwich.choose_bread()
    sandwich.choose_protein()
    sandwich.choose_cheese()
    sandwich.choose_extra()
    sandwich.calculate_total()
    print(f"Total cost of your sandwich: {sandwich.total_cost}€")


if __name__ == "__main__":
    main()
