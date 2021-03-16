from filter_values import filterOut_safe_vitals
from battery_limits import Get_Lang_Based_Word, lang, lang_message_list

def report_battery_vitals(processed_data):
    abnormal_vitals = list(filter(filterOut_safe_vitals,processed_data))
    if len(abnormal_vitals) > 0:
        report_abnormal_vitals(abnormal_vitals)
    else:
        report_normal_vitals()
        
def report_normal_vitals():
    print(Get_Lang_Based_Word("Battery is ok",lang,lang_message_list))
    print("\n")
    
def report_abnormal_vitals(abnormal_vitals):   
    messages =[]
    messages.extend(get_abnormal_values_heading())
    for i in abnormal_vitals:
        message = '{:>20}'.format(str(i[1])+"   |   ")
        message+='{:>30}'.format(str(i[3])+"   |   ")
        message+='{:>12}'.format("{:.2f}".format(i[2])+"   |   ")
        message+='{:>12}'.format("{:.2f}".format(i[4][1])+" - "+"{:.2f}".format(i[4][2]))
        messages.append(message)
    print_abnormal_vitals(messages)

def get_abnormal_values_heading():
    valueStringByLang = Get_Lang_Based_Word("Value",lang,lang_message_list)
    normalRangeStringbyLang = Get_Lang_Based_Word("Normal range",lang,lang_message_list)
    attributeStringByLang = Get_Lang_Based_Word("Attribute",lang,lang_message_list)
    infoStringByLang = Get_Lang_Based_Word("Info",lang,lang_message_list)    
    line1 = '{:>20}'.format(attributeStringByLang+"   |   ")
    line1+='{:>30}'.format(infoStringByLang+"   |   ")
    line1+='{:>12}'.format(valueStringByLang+"   |   ")
    line1+='{:>12}'.format(normalRangeStringbyLang)    
    line2 ="-"*80
    return (line1, line2)
    
def print_abnormal_vitals(messages):
    print(Get_Lang_Based_Word("Abnormal Vitals",lang,lang_message_list))
    print("\n")
    for message in messages:
        print(message)
    print("\n")      
