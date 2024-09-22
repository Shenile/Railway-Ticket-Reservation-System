from utils import get_current_time
class Train:
    def __init__(self, name, number, startingPoint,
                 endingPoint, superfast, RoutesAndDistanceChart, time_schedule):
        self.name = name
        self.number = number
        self.startingPoint = startingPoint
        self.endingPoint = endingPoint
        self.superfast = superfast
        self.routeAndDistanceChart = RoutesAndDistanceChart
        self.stops = sorted(list(RoutesAndDistanceChart.keys()))
        self.time_schedule = time_schedule
        self.status = self.check_status()



    def check_status(self):
        # Assuming departure time is a key in time_schedule
        departure_time = self.time_schedule['departure']
        # Compare departure time with current time
        return "Departed" if departure_time < get_current_time() else "At Station"


    def __str__(self):
        print(f'train name :', self.name)
        print(f'train number :', self.number)
        print(f'StartPoint :', self.startingPoint)
        print(f'Endpoint :', self.endingPoint)
        print(f'SuperFast: {"yes" if self.superfast else "no"}')
        return "details"



