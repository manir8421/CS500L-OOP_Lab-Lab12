from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)

@acts_as_state_machine
class VendingProcess:
    # define 4 states
    idle = State(initial=True)
    coin_insert = State()
    product_select = State()
    product_dispense = State()

    # define transitions
    coininserting = Event(from_states = idle, to_state = coin_insert)
    productselecting = Event(from_states = coin_insert, to_state = product_select)
    productdispensing = Event(from_states = product_select, to_state = product_dispense)
    returnchange = Event(from_states= (coin_insert, product_select, product_dispense), to_state = idle)
    returncoin = Event(from_states= coin_insert, to_state=idle)

    # before
    @before('coininserting')
    def before_coininserting(self):
        confirm = input("Do you want to insert coins? (y/n): ")
        return True if confirm.lower() == 'y' else False

    @before('productselecting')
    def before_productselecting(self):
        confirm = input("Do you want to select products? (y/n): ")
        return True if confirm.lower() == 'y' else False

    @before('productdispensing')
    def before_productdispensing(self):
        confirm = input("Do you want to dispense products? (y/n): ")
        return True if confirm.lower() == 'y' else False

    # after
    @after('coininserting')
    def after_coininserting(self):
        print("Coin has been inserted.")

    @after('productselecting')
    def after_productselecting(self):
        print("Product has been selected.")

    @after('productdispensing')
    def after_productdispensing(self):
        print("Product has been dispensed.")

    @after('returnchange')
    def after_returnchange(self):
        print("Return the changes.")

    @after('returncoin')
    def after_returncoin(self):
        print("Return the coins.")


    
class VendingMachine:
    def __init__(self) -> None:
        self.state = VendingProcess()

    def insertcoin(self):
        self.state.coininserting()

    def selectproduct(self):
        self.state.productselecting()

    def dispenseproduct(self):
        self.state.productdispensing()

    def returnchange(self):
        self.state.returnchange()

    def returncoin(self):
        self.state.returncoin()

    def get_current_state(self):
        return self.state.current_state
    

def show_menu():
    print("\n====== Vending Machine Menu ======")
    print("1. Insert Coins")
    print("2. Select Product")
    print("3. Dispense Product")
    print("4. Return changes")
    print("5. Return Coins")
    print("6. Exit")


def main():
    vending_machine = VendingMachine()
    while True:
        show_menu()
        choice = input("\nEnter your selection: ")
        try:
            if choice == '1':
                vending_machine.insertcoin()
            elif choice == '2':
                vending_machine.selectproduct()
            elif choice == '3':
                vending_machine.dispenseproduct()
            elif choice == '4':
                vending_machine.returnchange()
            elif choice == '5':
                vending_machine.returncoin()
            elif choice == '6':
                break
            else:
                print("Invalid selection! Please select a valid option.")
            print(f"Machine is now in '{vending_machine.get_current_state()}' state.")
        except InvalidStateTransition as ex:
            print(f"Cannot perform the operation in {vending_machine.get_current_state()} state.")

if __name__ == "__main__":
    main()