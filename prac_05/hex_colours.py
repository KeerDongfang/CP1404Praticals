HEX_COLOR_CODE = {"ZAFFRE": "#0014a8", "ZOMP": "#39a78e", "WINE": "#722f37", "WINTERGREEN": "#56887d",
                  "WISTERIA": "#c9a0dc", "TURQUOISE": "#00ffef", "TEAL BLUE": "#367588", "SHAMROCK GREEN": "#009e60",
                  "ROYALBLUE": "#4169e1", "PALETURQUOISE": "#afeeee"}
print(HEX_COLOR_CODE)

color_name = input("Please enter a name of color: ").upper()
while color_name != "":
    if color_name in HEX_COLOR_CODE:
        print(f"The hexadecimal code of {color_name} is {HEX_COLOR_CODE[color_name]}")
    else:
        print("Invalid input.")
    color_name = input("Please enter a name of color: ").upper()


