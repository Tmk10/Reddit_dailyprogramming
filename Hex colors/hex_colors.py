def hexcolor(r, g, b) -> str:
    return ("#{:02X}{:02X}{:02X}".format(r, g, b))


def blend(colors_to_blend) -> str:
    colors_list = [[int(color[index:index + 2], 16) for color in colors_to_blend] for index in
                   range(1, 7, 2)]
    return (hexcolor(*(round(sum(color) / len(color)) for color in colors_list)))
