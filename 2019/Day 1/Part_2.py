#Advent of Code Day 1 Part 2
import math

def main():

    fuel_weights = [] #Creates a list that will contain each individual fuel weight

    with open('input.txt', 'r') as reader:
        module_weights = reader.readlines() #Turns the input into a list

    for i in module_weights: #Calculates each individual weight and adds it to the end of the fuel_weights list
        i = int(i)
        j = i
        fuel_weight = i
        while ( fuel_weight - ( fuel_weight % 3 ) ) / 3 - 2 > 0:
            fuel_weight = ( fuel_weight - ( fuel_weight % 3 ) ) / 3 - 2
            i = fuel_weight + i
        i = i - j
        print(fuel_weight)
        fuel_weights.append(i)
    
    total_weight = 0 #Creates the variable total_weight, which will eventually hold the total weight

    for i in fuel_weights:
        total_weight = i + total_weight

    
    print(total_weight)

main()