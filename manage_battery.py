from report_vitals import report_battery_vitals
from filter_values import filterOut_safe_vitals   
from process_battery_data import process_data 
from controller_actions import get_actions  

def is_battery_ok(bms_attributes):
    data = process_data(bms_attributes)
    report_battery_vitals(data)
    get_actions(data)
    value = list(filter(filterOut_safe_vitals,data))
    return len(value) == 0 


if __name__ == '__main__':
  assert(is_battery_ok({'temperature': 25,'Soc': 70, 'Charge_rate': 0.7}) is True)  #all values in limit
  assert(is_battery_ok({'Temperature': 46,'soc': 23, 'Charge_rate': 0.77}) is False)  #high temp warning,low soc warning,charge_rate high warnings
