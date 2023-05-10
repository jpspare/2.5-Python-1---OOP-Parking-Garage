
class ParkingGarage():
    """
    Has three methods:
    1. take_ticket, which when instantiated, decreases the number of tickets and parking spaces by 1
    2. pay_for_parking, which allows the user to attempt to pay the requiste amount for a ticket
    3. leave_garage, which allows the user to leave once the ticket is paid

    Has three atrributes:
    - tickets, which is a list from 0 to 49
    - parking spaces, which is a list from 0 to 49
    - current ticket, which is a dictionary beginning with values for 'payment' of 0 and 'paid' as False
    """

    def __init__(self):
        self.tickets = list(range(50))
        self.parking_spaces = list(range(50))
        self.current_ticket = {'payment': 0, 'paid': False}
    
    # Method for user to 'take a ticket,' reducing available tickets and parking spaces by 1
    def take_ticket(self):
        del self.tickets[-1]
        del self.parking_spaces[-1]
        print(f'There are now {len(self.tickets)} tickets and {len(self.parking_spaces)} parking spaces remaining.')
    
    # Method for user to pay for parking
    def pay_for_parking(self):
        print(f"Your total due is ${5 - self.current_ticket['payment']}.")
        try:
            amount_paid = self.current_ticket['payment'] + int(input("How much would you like to pay? "))
            if amount_paid == 5:
                print('Thank you! Your ticket is paid, and you have 15 minutes to leave the garage.')
                self.current_ticket['paid'] = True
            elif amount_paid > 5:
                print(f'Thank you! Your ticket is paid, and your change is ${amount_paid - 5}. You have 15 minutes to leave the garage.')
                self.current_ticket['paid'] = True
            else:
                print("I'm sorry, that's not a enough. Please return with more money.")
                self.current_ticket['payment'] = amount_paid
        except(ValueError):
            print("Please enter your money as an integer.")
        
    # Method for user to leave the garage, assuming the ticket has been paid
    def leave_garage(self):
        if self.current_ticket['paid']:
            print('Thank You, have a nice day')
            self.parking_spaces.append(len(self.parking_spaces))
            self.tickets.append(len(self.tickets))
            self.current_ticket['payment'] = 0
            self.current_ticket['paid'] = False
        else:
            print("Please pay your ticket before leaving. Thank you!")
            self.pay_for_parking()
        



# Sample garage along with run function for the ParkingGarage class to ensure operability
sample_garage = ParkingGarage()
def run():
    while True:
        possible_actions = [
            {'name': 'take ticket', 'fn': sample_garage.take_ticket},
            {'name': 'pay for parking', 'fn': sample_garage.pay_for_parking},
            {'name': 'leave garage', 'fn': sample_garage.leave_garage},
        ]

        action_input = input("\nWhat would you like to do?\n1. Take a Ticket \n2. Pay for Parking \n3. Leave the Garage\n4. Quit\n")
        action = None

        try:
            i = int(action_input)
            if i >= 1 and i <= len(possible_actions):
                action = possible_actions[i-1]
                action['fn']()
        except(ValueError):
            pass
        if not action:
            for option in possible_actions:
                if option['name'].lower().startswith(action_input.lower()):
                    action = option
                    return action['fn']()
        if action_input.lower() in ['4', 'quit']:
            break
        if not action:
            print(f"I'm sorry, I'm not sure what '{action_input}' means. Please enter 1, 2, 3, or 4.")
            return run()

run()