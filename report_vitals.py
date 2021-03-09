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
   print(Get_Lang_Based_Word("Abnormal Vitals",lang,lang_message_list))
    
   for i in abnormal_vitals.items():
       limitRanges = range_limits[i[0].upper()]
       print(abnormal_attribute_and_limt(limitRanges,i[1]))
   print("\n")

def abnormal_attribute_and_limt(ranges,attributeValue):
    count = 0
    message = ""
    attrValAsString = str(attributeValue)
    valueStringByLang = Get_Lang_Based_Word("Value",lang,lang_message_list)
    for rangeVal in ranges:
        if count == 4: #If the last range is reached, then it means the attribute has exceeded all limits
           message = rangeVal + " | "+valueStringByLang+" : "+attrValAsString #the last item in limitranges is a single item, hence index is not neede for rangeVal
           break
        elif attributeValue<=rangeVal[0]:
            if count == 2: #If the range is in safe region, then the battery data doesn't need to be published
               break
            message = rangeVal[1] +" | "+valueStringByLang+" : "+attrValAsString
            break
        count+=1
    return message
    
