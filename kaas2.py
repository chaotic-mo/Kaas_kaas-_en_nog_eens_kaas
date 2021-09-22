#dit wats om te vergelijken en goed nachecken ook al is het nu het zelfde.

print("beantwoordt de volgende vragen met 'yes' en 'no'. ")
geel = input('is de kaas geel? ')
if geel == ("yes"):
    gaten = input('Zitten er gaten in? ')
    if gaten == ("yes"):
        duur = input('Is de kaas belachelijk duur? ')    
        if duur == ("yes"):
            print('Dan is het Emmenthaler')
        else:
            print('Dan is het Leerdammer')
    elif gaten == ("no"):
        hard = input('Is het hard als steen? ')
        if hard == ("yes"):
            print('dan is het Parmigiano Reggiano')
        else:
            print('dan is het goudsekaas')
elif geel == ("no"):
    schimmel = input('Heeft de kaas schimmels? ')
    if schimmel == ("yes"):
        korst_blauw = input('Heeft de kaas een korst? ')
        if korst_blauw == ("yes"):
            print('dan is het Blue de rochbaron')
        else:
            print("dan is het foume D'Ambert")
    elif schimmel == ("no"):
        korst_geel = input('Heeft de kaas een korst? ')
        if korst_geel == ("yes"):
            print('Dan is het Camembert')
        else:
            print('dan is het mozzarella')