from battery_limits import bms_range_limits

def filterOut_safe_vitals(item):
    low_warning_val = bms_range_limits[item[0].upper()][1][0] 
    high_warning_val = bms_range_limits[item[0].upper()][2][0]   
    return (item[1] <= low_warning_val) or (item[1] >= high_warning_val)
