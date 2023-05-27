class Ticket:
    def __init__(self, station, arrival, price, time, date):
        self.departure = station.loc
        self.arrival = arrival
        self.price = price
        self.time = time
        self.date = date


class Passenger:
    def __init__(self, name, station, money, today):
        self.name = name
        self.station = station
        self.money = money
        self.today = today


class Station:
    def __init__(self, location):
        self.loc = location

    def sell(self, passenger, ticket):
        if passenger.money >= ticket.price:
            if passenger.today == ticket.date:
                print(f"{passenger.name} will go on a train today")
                print(f"{passenger.name} has bought a ticket from {self.loc} to {ticket.arrival} for {ticket.price} at {ticket.time}.")
                passenger.money -= ticket.price
                print(f"{passenger.name} now has {passenger.money} left.")
                passenger.station = ticket.arrival
                print(f"{passenger.name} is at {passenger.station}")
            else:
                print(f"{passenger.name} doesn't want to wait for tomorrow")
        else:
            print(f"{passenger.name} doesn't have enough money to buy this ticket :(")
            print("\n_______________\n")

Moscow = Station("Москва")
msk_nsk = Ticket(Moscow, "Новосибирск", 4549, "02:46", 'today')
msk_spb = Ticket(Moscow, "Санкт-Петербург", 1786, "14:23", 'tomorrow')
msk_kzn = Ticket(Moscow, "Казань", 2345, "12:58", 'today')

novosibirsk = Station("Новосибирск")
nsk_omsk = Ticket(novosibirsk, "Омск", 2217, "12:45", 'today')
nsk_irk = Ticket(novosibirsk, "Иркутск", 4926, "13:34", 'today')
nsk_krsn = Ticket(novosibirsk, "Красноярск", 3239, "18:06", 'tomorrow')

person_1 = Passenger("Masha", "Москва", 10000, 'today')

Moscow.sell(person_1, msk_nsk)
novosibirsk.sell(person_1, nsk_krsn)