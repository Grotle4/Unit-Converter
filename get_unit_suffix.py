def get_suffix(converted, unit_to, page_type):
    print(page_type)
    if page_type != "temperature":
        if converted > 1:
            if unit_to == "foot":
                return "Feet"
            elif unit_to == "inch":
                return "Inches"
            else:
                unit_plural = unit_to + "s"
                return unit_plural.capitalize()
        else:
            return unit_to.capitalize()
    else:
        return unit_to.capitalize()
