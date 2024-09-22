from train import Train
from ticket_counter import TicketCounter
from utils import get_current_time
from Inputs import train_list
import os


tc = TicketCounter()
for t in train_list:
    tc.add_train(t)
os.system("cls")
start = tc.display_stops_list()
os.system("cls")
end = tc.display_stops_list()
os.system("cls")

tc.generate_Ticket(start, end)