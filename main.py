def bmi_calculator(weight, height):


    bmi = int(weight) / (float(height) ** 2)

    if (bmi < 18.5):
        return("Underweight")

    elif (bmi >= 18.5 and bmi < 25):
        return("Normal")

    elif (bmi >= 25 and bmi < 30):
        return("Overweight")

    elif (bmi > 30):
        return("Obesity")

    