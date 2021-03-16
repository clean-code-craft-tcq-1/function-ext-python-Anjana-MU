temperature_actions = { 0 : 'Warm the battery',
                 1 : 'Warm the battery',
                 2 : 'Maintain the state',
                 3 : 'Cool the battery',
                 4 : 'Cool the battery'}

soc_actions = {  0 : 'Show no charge warning',
                 1 : 'Show low charge warning',
                 2 : 'Turn on green light',
                 3 : 'Show almost full info',
                 4 : 'Show stop charge info'}

chargeRate_actions = { 0 : 'Start charging',
                 1 : 'Increase the charging rate',
                 2 : 'Maintain the state',
                 3 : 'Slow down the charging',
                 4 : 'Stop charging'}

action_dict = { 'TEMPERATURE' : temperature_actions,
                'SOC' : soc_actions,
                'CHARGE_RATE' : chargeRate_actions}

def get_actions(data):
    print("Controller actions \n")    
    for item in data:
        if (item[0].upper() in action_dict):
            instructions = action_dict[item[0].upper()]
            val = item[2]
            rangelist = item[4]
            index = get_index_for_range(val,rangelist)
            print('{:>20}'.format(item[0].upper()) + "   " +instructions[index])

        
def get_index_for_range(val,rangelist):
    index = 0
    for param in rangelist:        
        if val < param:            
            return index
        index += 1
    return (index - 1)
