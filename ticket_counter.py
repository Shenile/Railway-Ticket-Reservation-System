import os
from utils import get_current_time
class TicketCounter:

    def __init__(self):
        self.trains = {}

    def add_train(self, *args):
        for train in args:
            if train not in self.trains:
                self.trains[train.number] = train
            else:
                print(f"{train.name} is already in the list")

    def __binary_search(self, cont, target):

        low, high = 0, len(cont) - 1

        while (low <= high):
            mid = (low + high) // 2

            if (cont[mid] == target):

                return True
            elif(cont[mid] < target):
                low = mid + 1
            else:
                high = mid - 1

        return False

    def __isTrain_Available(self, train, start, end):
        stops = train.stops
        return (all([self.__binary_search(stops, start), self.__binary_search(stops, end)])
                and train.time_schedule["departure"] > get_current_time())

    def __search_trains(self, start, end):
        available_trains = []
        for train in self.trains.values():
            if(self.__isTrain_Available(train, start, end)):
                available_trains.append(train)
        return available_trains

    def __display_trains_list(self, start , end):
        trains = self.__search_trains(start, end)
        choicesMap = {}
        idx = 1
        print(f'Choose the train : ')
        for train in trains:
            choicesMap[idx] = train
            print(f'{idx} . {train.name} departure time : {train.time_schedule["departure"]}')
            idx += 1
        choice = self.__getChoice(choicesMap, idx)
        return choicesMap[choice]

    def __getChoice(self, choicesMap, numberOfChoices):
        if not choicesMap:
            return "there are no choices"
        while(True):
            choice = int(input("Enter your choice :"))
            if(choice > 0 and choice <= numberOfChoices):
                return choice
            else:
                print("Enter a valid Choice".center(21,'!'))

    def display_stops_list(self):
        idx = 1
        choicesMap = {}
        vals = self.trains.values()
        for train in vals:
            for stop in train.stops:
                if stop not in choicesMap.values():
                    choicesMap[idx] = stop
                    print(f'{idx} . {stop}')
                    idx += 1
        choice = self.__getChoice(choicesMap, idx)
        return choicesMap[choice]

    def __display_ticket(self, train, startingPoint, endingPoint, totalfare, totalDistance):
        print("-".center(20, '-'))
        print('IRCTC Ticket Booking System')
        print("-".center(20, '-'))
        print(f'Train name : {train.name}')
        print(f'Train number : {train.number}')
        print(f'Departure time : {train.time_schedule["departure"]} Arrival time : {train.time_schedule["arrival"]}')
        print(f'Boarding at : {startingPoint}')
        print(f'Destination : {endingPoint}')
        print(f'TotalDistance : {totalDistance} km')
        print(f'TotalFare : {totalfare} Rs')
        print("-".center(20, '-'))
        print("Happy Journey")
        print("-".center(20, '-'))

    def __compute_fare_and_distance(self, train, start, end, fare):
        totalDistance = abs(train.routeAndDistanceChart[start] - train.routeAndDistanceChart[end])
        totalFare = totalDistance * fare
        return totalFare, totalDistance

    def generate_Ticket(self, startingPoint, endingPoint):
        os.system("cls")
        train = self.__display_trains_list(startingPoint, endingPoint)
        totalFare, totalDistance = self.__compute_fare_and_distance(train, startingPoint, endingPoint, fare = 0.5)
        os.system("cls")
        if(train.time_schedule["departure"] > get_current_time()):
            self.__display_ticket(train, startingPoint, endingPoint, totalFare, totalDistance)
