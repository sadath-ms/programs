def sadath(aurgment):
    dict_name={32:'sadath',1:'aditya',52:'roni'}
    for key,values in dict_name.items():
        if key == aurgment:
            print(key,'-',values)
    return dict_name.get(aurgment)

if __name__ == '__main__':
    aurg=int(input('enter the key'))
    print(sadath(aurg))
