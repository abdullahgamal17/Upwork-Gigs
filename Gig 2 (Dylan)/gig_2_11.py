#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Solved according to the photo's logic
def solve_problem(p,number_of_processes_per_processor,single_processor_speed,time_per_message,message_per_processor):
    time_needed = 0
    time_needed_per_processor = number_of_processes_per_processor/single_processor_speed
    time_needed_to_handle_messages = time_per_message * message_per_processor 
    time_needed = time_needed_per_processor + time_needed_to_handle_messages
    return time_needed

p = 1000
#time_needed_for_serial = pow(10,6) #in seconds , Tserial
single_proccesor_speed = pow(10,6) #in instructions per second , S
instruction_per_processor = pow(10,12)/p
messages_per_processor = pow(10,9)*(p-1)
time_per_message_2_11a = pow(10,-9)
number_of_processes_per_processor = pow(10,12)/p
# 1000 processors (p = 1000) , Tserial = 10^6 , processor_speed = 10^6 , time_per_message = 10^-9 , message_per_processor = 10^9(p-1)
answer1 = solve_problem(p,
                        number_of_processes_per_processor
                        ,single_proccesor_speed
                        ,time_per_message_2_11a
                        ,messages_per_processor)
print(answer1)
time_per_message_2_11b = pow(10,-3)
answer2 = solve_problem(p,
                        number_of_processes_per_processor
                        ,single_proccesor_speed
                        ,time_per_message_2_11b
                        ,messages_per_processor)
print(answer2)
    