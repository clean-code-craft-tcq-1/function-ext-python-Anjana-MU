
from report_vitals import report_battery_vitals
from filter_values import filterOut_safe_vitals             

def is_battery_ok(bms_attributes):
    value = dict(filter(filterOut_safe_vitals,bms_attributes.items()))
    report_battery_state(bms_attributes)
    return len(value) == 0

def report_battery_state(bms_attributes):    
    report_battery_vitals(bms_attributes)
    
if __name__ == '__main__':
  assert(is_battery_ok({'temperature': 25,'Soc': 70, 'Charge_rate': 0.7}) is True)  #all values in limit
  assert(is_battery_ok({'Temperature': 43,'soc': 24, 'Charge_rate': 0.5}) is False)  #high temp warning,low soc warning
  assert(is_battery_ok({'Temperature': 25,'Soc': 60, 'charge_rate': 0.03}) is False) #low charge warning  
