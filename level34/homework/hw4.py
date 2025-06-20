def number(bus_stops):
    total_people = 0  
    for stop in bus_stops:
        on = stop[0]   
        off = stop[1]  
        total_people += on - off 

    return total_people
