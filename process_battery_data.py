from battery_limits import bms_range_limits
     
def process_data(bms_attributes):
    info = []
    for param in bms_attributes.items():
        param_value = param[1]
        param_name = param[0]        
        limitRanges = bms_range_limits[param_name.upper()]
        info.append(check_vitals(limitRanges[1],param_value,param_name,limitRanges[0]))
    return info         
            
def check_vitals(limitRanges,param_value,param_name_english, param_name_by_lang):
    paramdata = get_data(limitRanges)
    for item in limitRanges:       
        if param_value < item[0]:
            return param_name_english,param_name_by_lang, param_value,item[1],paramdata
    return param_name_english,param_name_by_lang, param_value,limitRanges[4][1],paramdata

def get_data(limitRanges):
    #lambda x: (param[0] for param in limitRanges) 
    x = []
    for param in limitRanges:
        x.append(param[0])
    return x 
