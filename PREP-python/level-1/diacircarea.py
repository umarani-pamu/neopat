pi_value=3.14
def find_Diameter(r):
    return (2*r)
def find_Circumference(r):
    return (2*pi_value*r)
def find_Area(r):
    return (pi_value*r*r)
r=float(input())

diameter = find_Diameter(r)
circumference = find_Circumference(r)
area = find_Area(r)

print("Diameter of a circle = %.2f" %diameter)
print("Circumference of a circle = %.2f" %circumference)
print("Area of a circle = %.2f" %area)    