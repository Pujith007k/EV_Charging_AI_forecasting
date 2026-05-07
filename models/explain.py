def explain(d,g):
    if d>80 and g>120:
        return "High demand & grid load → shift to off-peak"
    elif d>80:
        return "High demand → avoid peak hours"
    return "Normal"
