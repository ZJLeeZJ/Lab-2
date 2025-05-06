def calcBMI(height, weight):
    bmi = weight/height**2
    print("height is ", height)
    print("weight is ", weight)
    print("bmi is ", bmi)
    return bmi

def classifyBMI(bmi):
    if(bmi>=30.0):
        return 1
    elif(bmi<30.0 and bmi>25.0):
        return 0
    elif(bmi>=18.5 and bmi<=25.0):
        return -1
    
    return

def app():
    output = calcBMI(1.78,86)
    classifyBMI(output)
    return

if __name__ == "__main__":
    app()