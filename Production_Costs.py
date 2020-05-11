import numpy as np
import re
import math

Isogen = 7.1
Megacyte = 331
Mexallon = 60
Nocxium = 281
Pyerite = 2.9
Tritanium = 7.3
Zydrine = 490

Minerals_Prices = np.asarray(
    [Tritanium, Pyerite, Mexallon, Isogen, Nocxium,  Zydrine, Megacyte])
Minerals_Names_us_en = ['Tritanium', 'Pyerite',
                        'Mexallon', 'Isogen', 'Nocxium',  'Zydrine', 'Megacyte']

Minerals_Names_zh_cn = ['三钛合金', '类晶体胶矿',
                        '类银超金属', '同位聚合体', '超新星诺克石', '晶状石英核岩', '超噬矿']
Capital_Propulsion_Engine = [457050, 110416, 41994, 6938, 2110, 604, 302]
Capital_Sensor_Cluster = [443591, 101026, 40877, 6659, 1804, 666, 298]
Capital_Armor_Plates = [473141, 111118, 43324, 7109, 2141, 682, 304]
Capital_Capacitor_Battery = [326973, 107842, 39547, 6440, 1841, 660, 280]
Capital_Power_Generator = [510149, 110413, 45621, 7491, 2191, 728, 334]
Capital_Shield_Emitter = [498880, 104957, 43194, 7269, 2033, 696, 332]
Capital_Jump_Drive = [749916, 142710, 49913, 8617, 2249, 908, 444]
Capital_Drone_Bay = [347163, 83248, 33332, 4499, 1258, 486, 172]
Capital_Computer_System = [427708, 111110, 44110, 6581, 1858, 648, 296]
Capital_Construction_Parts = [388208, 93777, 37729, 5104, 1530, 538, 212]
Capital_Ship_Maintenance_Bay = [576759, 189942, 53312, 9010, 2461, 914, 416]
Capital_Corporate_Hangar_Bay = [583442, 145664, 51297, 9321, 2678, 938, 436]

Components_Minerals_Needs = np.asarray([Capital_Propulsion_Engine, Capital_Sensor_Cluster, Capital_Armor_Plates, Capital_Capacitor_Battery, Capital_Power_Generator, Capital_Shield_Emitter,
                                        Capital_Jump_Drive, Capital_Drone_Bay, Capital_Computer_System, Capital_Construction_Parts, Capital_Ship_Maintenance_Bay, Capital_Corporate_Hangar_Bay])

Building_Role_Bonus = 1


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(math.ceil(n * multiplier) / multiplier)


def calculate_Actual_Components_Mineral_Needs(Component_Blueprint_Material_Efficiency=0):
    index_row = 0
    for component_mineral_needs in Components_Minerals_Needs:
        index_column = 0
        for mineral_needs in component_mineral_needs:
            Components_Minerals_Needs[index_row][index_column] = round_up(
                mineral_needs*((100 - Component_Blueprint_Material_Efficiency)/100) * ((100 - Building_Role_Bonus)/100))
            index_column += 1
        index_row += 1


calculate_Actual_Components_Mineral_Needs(
    Component_Blueprint_Material_Efficiency=20)


def add_thousand_separator(n):
    pattern = r'(\d+)(\d{3})((,\d{3})*)'
    n = str(n)
    while True:
        n, number = re.subn(
            pattern, r'\1,\2\3', n)
        if number == 0:
            break
    return n


class Nyx():
    Components_Amounts = [139, 139, 167, 139,
                          111, 83, 222, 694, 139, 222, 222, 222]

    def __init__(self, Nyx_Blueprint_Material_Efficiency=0):
        self.Blueprint_Material_Efficiency = Nyx_Blueprint_Material_Efficiency
        self.Building_Role_Bonus = Building_Role_Bonus

    def calculate_minerals_needs(self):
        sum = np.zeros(7)
        index = 0
        for component_amount in Nyx.Components_Amounts:
            sum = sum + component_amount * Components_Minerals_Needs[index]
            index += 1
        sum = sum * ((100 - self.Blueprint_Material_Efficiency) /
                     100) * ((100 - Building_Role_Bonus)/100)
        print('------------------------    Nyx    ------------------------')
        print('While Blueprint Material Efficiency is ' + str(self.Blueprint_Material_Efficiency) +
              ' and Building Role Bonus is ' + str(Building_Role_Bonus) + ', the Minerals Needs: ')
        index = 0
        for mineral_amount in sum:
            mineral_amount = add_thousand_separator(round_up(mineral_amount))

            print(Minerals_Names_us_en[index] + " (" +
                  Minerals_Names_zh_cn[index] + ") : " + mineral_amount)
            index += 1
        return sum

    def calculate_manufacturing_costs(self, Minerals_Amounts):
        sum = 0
        index = 0
        for mineral_amount in Minerals_Amounts:
            sum = sum + mineral_amount * Minerals_Prices[index]
            index += 1
        print('Will cost ' + add_thousand_separator(round_up(sum)) + ' isk in total.')


job = Nyx(Nyx_Blueprint_Material_Efficiency=8)
job.calculate_manufacturing_costs(job.calculate_minerals_needs())
