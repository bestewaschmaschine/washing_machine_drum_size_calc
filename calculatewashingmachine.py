import numpy as np


## Inputs
fieldname1 = 12 # TShirt
fieldname2 = 8 # Pants
fieldname3 = 12 # Socks and undergarmets
fieldname4 = 1 # Towels
fieldname5 = 1 # Bedsheets

# Weights of each cloth (gram)
F1_weight_gr = 200  
F2_weight_gr = 700 
F3_weight_gr = 150 
F4_weight_gr = 600 
F5_weight_gr = 750

IntendedMonthlyWashes = 4 # How many you want to wash per month

# Washing machine sizes in the kg
WashingMachineSizes = [6,7,8,9,10,11,12]


# Calculated Output
def main():
    WashPerMonth =[] # Array for washes per month with each machine weight

    WeeklyWashWeight = (( fieldname1 * F1_weight_gr) + 
                    ( fieldname2 * F2_weight_gr) +
                    ( fieldname3 * F3_weight_gr) +
                    ( fieldname4 * F4_weight_gr) +
                    ( fieldname5 * F5_weight_gr))/1000  # total weight of clothes per week

    MonthlyWashWeight = WeeklyWashWeight * 4 # total weight of clothes per month

    for i in range(len(WashingMachineSizes)):
        WashPerMonth.append(MonthlyWashWeight/WashingMachineSizes[i])

    # find the nearest value to the intended washing per month
    Value, ind = find_nearest(WashPerMonth, IntendedMonthlyWashes) 

    print('Total weight of laundry per month (kg): ' + str(MonthlyWashWeight))
    print('The suitable machine size for your home: ' +  str(WashingMachineSizes[ind]) + 'kg washing machine' ) 


# find the nearest value in an arry
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx


if __name__ == "__main__":
    main()

