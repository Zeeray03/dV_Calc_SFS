def area_formula(width_a, width_b, height, coefficient) :

    area = ((float(width_a) + float(width_b)) / 2) * float(height)
    mass = area / float(coefficient)

    return mass

def width_formula(width, coefficient) :

    mass = float(width) / float(coefficient)

    return mass