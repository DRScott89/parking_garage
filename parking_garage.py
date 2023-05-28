
class Parking_Garage():
    
    def __init__(self):
        self.tickets = list(range(1,31))
        self.parkingSpaces = list(range(1,31))
        self.currentTicket = {'paid': False}
    
    def takeTicket(self):
            print(f'Ticket Number: {self.tickets.pop()}\nParking Space: {self.parkingSpaces.pop()}')
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Parking: {len(self.parkingSpaces)}')

    def payForParking(self):
        pay_parking = int(input('Please input payment amount...\nParking Fee: 10 USD '))
        if pay_parking == 10:
            self.currentTicket = {'paid': True}
            print(f'\nPayment Complete! You have 15 minutes to exit.')
            increase_tickets = self.tickets[-1] + 1
            self.tickets.append(increase_tickets)
            increase_spaces = self.parkingSpaces[-1] + 1
            self.parkingSpaces.append(increase_spaces)
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Parking: {len(self.parkingSpaces)}')
        if pay_parking > 10:
            self.currentTicket = {'paid': True}
            dispense_amount = pay_parking - 10
            print(f'\nDispensing change...{dispense_amount} USD')
            print(f'Payment Complete! You have 15 minutes to exit.')
            increase_tickets = self.tickets[-1] + 1
            self.tickets.append(increase_tickets)
            increase_spaces = self.parkingSpaces[-1] + 1
            self.parkingSpaces.append(increase_spaces)
            print(f'\nAvailable Tickets: {len(self.tickets)}')
            print(f'Available Parking: {len(self.parkingSpaces)}')
        if pay_parking < 10:
            self.currentTicket = {'paid': False}
            balance = 10 - pay_parking
            print(f'\nPlease input {balance} USD to complete payment.')
            remaining_balance = int(input('Please insert remaining balance...'))
            if remaining_balance == balance:
                self.currentTicket = {'paid': True}
                print(f'\nPayment Complete! You have 15 minutes to exit.')
                increase_tickets = self.tickets[-1] + 1
                self.tickets.append(increase_tickets)
                increase_spaces = self.parkingSpaces[-1] + 1
                self.parkingSpaces.append(increase_spaces)
                print(f'\nAvailable Tickets: {len(self.tickets)}')
                print(f'Available Parking: {len(self.parkingSpaces)}')
                
            else:
                self.currentTicket = {'paid': False}
                print('\nReturning money. Please try again.')
                
    def leaveGarage(self):
        if self.currentTicket == {'paid': True}:
            print('\nThank you have a nice day!')
        else:
            print("This ticket has not been paid. Input 'Pay' to insert ticket amount.\nTicket Amount: 10 USD")

usedTicket = Parking_Garage()


def run():
    while True:
        question = input("All Parking 10 USD!!!\nPlease input the following: \n'Ticket': Print Ticket\n'Pay': Insert Payment\n'Exit': Leave Garage\n'Quit': Quit: ")
        
        if question.lower() == 'ticket':
            usedTicket.takeTicket()
        if question.lower() == 'pay':
            usedTicket.payForParking()
        if question.lower() == 'exit':
            usedTicket.leaveGarage() 
        if question.lower() == 'quit':
            break
run()

        
    