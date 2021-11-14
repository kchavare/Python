try:
    Score =float(input("Enter the Score between (0.0 to 1.0):"))
    if Score > 1.0:
        print("Please enter the number between specified range.")
        exit()
    elif Score == 0.9 or Score == 1.0:
        print("Grade - A")
    elif Score == 0.8:
        print("Grade - B")
    elif Score == 0.7:
        print("Grade - C")
    elif Score == 0.6:
        print("Grade - D")
    elif Score <= 0.5:
        print("Grade - F")
except Exception as e:
    print("Plese enter Score in number.")