def filterOut_safe_vitals(item):   
    return ( "_" in item[3]) # except normal all other string will contain '_'
