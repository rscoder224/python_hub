
# Problem 2
# 0 * 1.8 + 32 = farenhieght





def fconverter():
    temp = int(input("Enter The Tempreture: "))
    print(f"Celcius: {temp} converted to fahrenhiet {temp*1.8+32}")
    if temp < 0 :
        print("too cold")
    elif temp < 20 :
        print("Cold Outside")
    elif temp > 20 and temp <= 30:
        print("Moderate Climate")
        
     

fconverter()


     
     
