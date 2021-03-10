from filter_values import filterOut_safe_vitals
from battery_limits import Get_Lang_Based_Word, bms_range_limits, lang,lang_message_list

def report_battery_vitals(bms_attributes):
    abnormal_vitals = dict(filter(filterOut_safe_vitals,bms_attributes.items()))
    if len(abnormal_vitals) > 0:
        report_abnormal_vitals(abnormal_vitals,bms_range_limits)
    else:
        report_normal_vitals()
        
def report_normal_vitals():
    print(Get_Lang_Based_Word("Battery is ok",lang,lang_message_list))
    print("\n")
    
def report_abnormal_vitals(abnormal_vitals,range_limits):   
   messages =[]   
   for i in abnormal_vitals.items():
      limitRanges = range_limits[i[0].upper()]
      message = abnormal_attribute_and_limt(limitRanges,i[1])
      if not(message is None):
          messages.append(message)           
   print_abnormal_vitals(messages)

def print_abnormal_vitals(messages):
    if len(messages)>0:
        print(Get_Lang_Based_Word("Abnormal Vitals",lang,lang_message_list))
        for message in messages:
            print(message)
        print("\n")
        
def abnormal_attribute_and_limt(ranges,attributeValue):
    count = 0
    message = ""
    valueStringByLang = Get_Lang_Based_Word("Value",lang,lang_message_list)
    for rangeVal in ranges:
        message = get_message_to_print(rangeVal,valueStringByLang,attributeValue,count)
        if (count != 2): #Normal range, so no need to inform user
            return message
        count+=1
    return None

def get_message_to_print(rangeAndVal, valueStrByLang,attributeValue,count):
    if count==4:
        return rangeAndVal+" | "+valueStrByLang+" : "+str(attributeValue)
    elif attributeValue<=rangeAndVal[0]:
        return rangeAndVal[1] +" | "+valueStrByLang+" : "+str(attributeValue)    
