def are_you_playing_banjo(name):
    # Implement me!
    first_string = name[0]
    if(first_string == "R" or first_string == "r"):
        is_playing_banjo = name + " plays banjo" 
    else:
        is_playing_banjo = name + " does not play banjo"
    return is_playing_banjo