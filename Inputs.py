from train import Train
from utils import get_current_time

StationsAndDistanceChart1 = {
    "chennai": 0,
    "vilupuram": 100,
    "trichy": 200,
    "madurai": 300,
    "rameswaram": 450,
}

time_schedule = {
    "departure" : get_current_time(5),
    "arrival" : get_current_time(10)
}
train1 = Train("Rameswaram Express", 2453725,
               "chennai", "rameswaram",
               True, StationsAndDistanceChart1, time_schedule)

# Station and distance charts for Tamil Nadu trains
StationsAndDistanceChart2 = {
    "chennai": 0,
    "vilupuram": 120,
    "trichy": 220,
    "madurai": 340,
    "kanyakumari": 600,
}

StationsAndDistanceChart3 = {
    "chennai": 0,
    "katpadi": 140,
    "vellore": 150,
    "salem": 300,
    "coimbatore": 500,
}

StationsAndDistanceChart4 = {
    "chennai": 0,
    "cuddalore": 180,
    "nagapattinam": 320,
    "thanjavur": 380,
    "tiruvarur": 400,
}

StationsAndDistanceChart5 = {
    "chennai": 0,
    "egmore": 5,
    "tambaram": 30,
    "dindigul": 400,
    "tirunelveli": 500,
}

# Time schedules for Tamil Nadu trains
time_schedule2 = {
    "departure": get_current_time(4),
    "arrival": get_current_time(11)
}

time_schedule3 = {
    "departure": get_current_time(6),
    "arrival": get_current_time(13)
}

time_schedule4 = {
    "departure": get_current_time(5),
    "arrival": get_current_time(12)
}

time_schedule5 = {
    "departure": get_current_time(3),
    "arrival": get_current_time(9)
}

# Creating additional Tamil Nadu train instances
train2 = Train("Kanyakumari Express", 2453726,
               "chennai", "kanyakumari",
               True, StationsAndDistanceChart2, time_schedule2)

train3 = Train("Coimbatore Intercity", 2453727,
               "chennai", "coimbatore",
               True, StationsAndDistanceChart3, time_schedule3)

train4 = Train("Nagapattinam Express", 2453728,
               "chennai", "tiruvarur",
               True, StationsAndDistanceChart4, time_schedule4)

train5 = Train("Tirunelveli Superfast", 2453729,
               "chennai", "tirunelveli",
               True, StationsAndDistanceChart5, time_schedule5)



train_list = [train1, train2, train3, train4, train5]

