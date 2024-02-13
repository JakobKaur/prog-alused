from typing import Optional


class Client:

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):

        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        return self.name

    def earnings_per_day(self):
        pass

def read_from_file_into_list(filename: str) -> list:
    clients = []
    with open(filename, 'r') as file:
        for line in file:          
            name, bank, account_age, starting_amount, current_amount = line.strip().split(',') 
            clients.append(Client(name, bank, int(account_age), int(starting_amount), int(current_amount)))
    return clients

def filter_by_bank(filename: str, bank: str) -> list:
    clients = read_from_file_into_list(filename)
    return [client for client in clients if client.bank == bank]

def largest_earnings_per_day(filename: str) -> Optional[Client]:
    clients = read_from_file_into_list(filename)
    max_earnings_per_day = 0
    best_client = None

    for client in clients:
        earnings_per_day = (client.current_amount - client.starting_amount) / client.account_age
        if earnings_per_day > 0: 
            if earnings_per_day > max_earnings_per_day or (earnings_per_day == max_earnings_per_day and client.account_age < best_client.account_age):
                max_earnings_per_day = earnings_per_day
                best_client = client
    return best_client


def largest_loss_per_day(filename: str) -> Optional[Client]:
    clients = read_from_file_into_list(filename)
    max_loss_per_day = 0
    worst_client = None

    for client in clients:
        loss_per_day = (client.starting_amount - client.current_amount) / client.account_age
        if loss_per_day > 0:  
            if loss_per_day > max_loss_per_day or (loss_per_day == max_loss_per_day and client.account_age < worst_client.account_age):
                max_loss_per_day = loss_per_day
                worst_client = client
    return worst_client

    for client in clients:
        loss_per_day = (client.starting_amount - client.current_amount) / client.account_age
        if loss_per_day > max_loss_per_day:
            max_loss_per_day = loss_per_day
            worst_client = client
        elif loss_per_day == max_loss_per_day:            
            if client.account_age < worst_client.account_age:
                worst_client = client
    return worst_client

if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]
    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]
    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh
    print(largest_loss_per_day("clients_info.txt"))  # -> Franz