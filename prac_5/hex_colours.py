
colour_codes = {"blue1": "#0000ff", "BlueViolet": "#8a2be2",
                "brown3": "cd3333", "burlywood": "#deb887",
                "CadetBlue": "#5f9ea0", "coral": "#ff7f50",
                "cyan1": "#00ffff", "DarkGoldenrod": "#b8860b",
                "DarkGreen": "#006400", "DarkKhaki": "#bdb76b",
                "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc", "DarkSeaGreen": "#8fbc8f",
                "DeepPink1": "#ff1493", "firebrick": "#b22222"}

colour_name = input("Please enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             colour_codes.get(colour_name)))
    colour_name = input("Please enter a colour name: ")