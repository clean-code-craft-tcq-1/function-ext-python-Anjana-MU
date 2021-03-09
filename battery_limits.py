lang = 'EN'

warning_range_percent = 5

bms_attribute_limits = {'TEMPERATURE': {'min': 0, 'max': 45},
                        'SOC': {'min': 20, 'max': 80},
                        'CHARGE_RATE': {'min': 0,'max': 0.8}} 

en_list = ("low_replace_breach","low_replace_warning","normal","high_replace_warning","high_replace_breach")
de_list =("niedrig_replace_bruch","niedrig_replace_warnung","normal","hoch_replace_warnung","hoch_replace_bruch")
lang_range_dict = {"EN":en_list,"DE":de_list}

en_attr_list = ("TEMPERATURE","SOC","CHARGE_RATE")
de_attr_list = ("TEMPERATUR","SOC","lADESTROM")
lang_attr_dict = {"EN":en_attr_list,"DE":de_attr_list}

en_message_list = ("Battery is ok".upper(),"Abnormal Vitals".upper(),"Value".upper())
de_message_list = ("Batterie ist in Ordnung","Abnorme Vitalwerte","Wert")
lang_message_list ={"EN":en_message_list,"DE":de_message_list}

def Get_Lang_Based_Word(attribute,lang,lang_attr_dict):
    en_attributes = lang_attr_dict['EN']
    index = en_attributes.index(attribute.upper())
    user_lang_attributes = lang_attr_dict[lang]  
    return user_lang_attributes[index].upper()  
        
def Get_Lang_Based_Range_String(index,attributeByLang,lang,lang_range_dict):
    lang_range_list = lang_range_dict[lang]   
    range_string = lang_range_list[index]
    range_string = range_string.replace("replace",attributeByLang)
    return range_string.upper()
    
def Create_Range_List():
    rangeDict = {}
    percent = warning_range_percent/100
    for i in bms_attribute_limits.items():
        rangeList =[]
        val = i[1]['max']*percent
        attrByLang = Get_Lang_Based_Word(i[0].upper(),lang,lang_attr_dict)        
        rangeList.append(( i[1]['min'],Get_Lang_Based_Range_String(0,attrByLang,lang,lang_range_dict)))
        rangeList.append(( i[1]['min']+val,Get_Lang_Based_Range_String(1,attrByLang,lang,lang_range_dict)))
        rangeList.append(( i[1]['max']-val,Get_Lang_Based_Range_String(2,attrByLang,lang,lang_range_dict)))
        rangeList.append(( i[1]['max'],Get_Lang_Based_Range_String(3,attrByLang,lang,lang_range_dict)))
        rangeList.append(Get_Lang_Based_Range_String(4,attrByLang,lang,lang_range_dict))
        rangeDict[i[0]]=rangeList
    return rangeDict 
  
bms_range_limits = Create_Range_List()

