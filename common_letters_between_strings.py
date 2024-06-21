def common_letters():
    str1 = "amrit"
    str2 = "manash"
    s1=set(str1)
    s2=set(str2)
    common_letters_list = s1 & s2;
    print("Common letter or letters in both strings are ",common_letters_list)
    
   

common_letters()
