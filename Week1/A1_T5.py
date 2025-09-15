# Print “Calculate the area of a wall.”
print("Calculate the area of a wall.")

#Prompt user
#“Enter the width in meters: ”
#Store the input value into Feed variable.
#Convert the Feed variable into an integer and store it in Width variable
Feed = input("Enter the width in meters: ")
Width = int(Feed)

#Prompt user
#“Enter the height in meters: ”
#store the input value into Feed variable.
#Convert the Feed variable into an integer and store it in Height variable
Feed = input("Enter the height in meters: ")
Height = int(Feed)

#Print “Width is {Width} m and height is {Height} m.”
# f-string
print(f"Width is {Width} m and height is {Height} m.")

#Multiply Width and Height, then store the result in Area variable
Area = Width * Height

#Display results to the user: “The wall will be {Area} square meters.”
print(f"The wall will be {Area} square meters.")

