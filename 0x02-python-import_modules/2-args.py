#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if (num_args == 0):
    print("0 arguments.")

elif (num_args == 1):
    print("1 argument:")

else:
    print(f"{num_args} {'arguments:'}")

index = 1

while index <= num_args:
          print(f"{index}:{sys.argv[index]}")
          index+=1
