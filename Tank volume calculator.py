"""
Tank Volume Calculator

Author: Chibuikem Ndubuisi

Calculates the volume of:
- Cylinder
- Sphere
- Cone
- Rectangular Tank
"""

import math

pie = math.pi


def cylinder_volume(r_cyl, h_cyl):
    # Calculate the volume of a cylinder
    v_cyl = pie * (r_cyl ** 2) * h_cyl
    return v_cyl


def sphere_volume(r_sph):
    # Calculate the volume of a sphere
    v_sph = 4 / 3 * pie * (r_sph ** 3)
    return v_sph


def cone_volume(r_con, h_con):
    # Calculate the volume of a cone
    v_con = 1 / 3 * pie * (r_con ** 2) * h_con
    return v_con


def rectangular_volume(l_rec, w_rec, h_rec):
    # Calculate the volume of a rectangular tank
    v_rec = l_rec * w_rec * h_rec
    return v_rec


def main():

    print("==============================")
    print("Tank Volume Calculator")
    print("==============================")
    print("Shapes Available:")
    print("Cylinder")
    print("Sphere")
    print("Cone")
    print("Rectangle")
    print()

    again = "yes"

    while again == "yes":

        shape = input("What shape do you want the volume calculated for? ")
        shape = shape.lower()

        if shape == "cylinder":

            radius = float(input("What is the radius? "))
            height = float(input("What is the height? "))

            if radius <= 0 or height <= 0:
                print("Radius and height must be greater than zero.")

            else:
                volume = cylinder_volume(radius, height)
                volume_string = str(volume)
                print("The volume of the cylinder is " + volume_string + " m^3.")

        elif shape == "sphere":

            radius = float(input("What is the radius? "))

            if radius <= 0:
                print("Radius must be greater than zero.")

            else:
                volume = sphere_volume(radius)
                volume_string = str(volume)
                print("The volume of the sphere is " + volume_string + " m^3.")

        elif shape == "cone":

            radius = float(input("What is the radius? "))
            height = float(input("What is the height? "))

            if radius <= 0 or height <= 0:
                print("Radius and height must be greater than zero.")

            else:
                volume = cone_volume(radius, height)
                volume_string = str(volume)
                print("The volume of the cone is " + volume_string + " m^3.")

        elif shape == "rectangle":

            length = float(input("What is the length? "))
            width = float(input("What is the width? "))
            height = float(input("What is the height? "))

            if length <= 0 or width <= 0 or height <= 0:
                print("All dimensions must be greater than zero.")

            else:
                volume = rectangular_volume(length, width, height)
                volume_string = str(volume)
                print("The volume of the rectangular tank is " + volume_string + " m^3.")

        else:
            print("Invalid shape.")
            print("Please choose Cylinder, Sphere, Cone or Rectangle.")

        print()
        again = input("Would you like another calculation? (yes/no) ")
        again = again.lower()

    print("Thank you for using the Tank Volume Calculator.")


if __name__ == "__main__":
    main()