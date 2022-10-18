afc_east_west_wins = {'Bills': 4,
                      'Jets': 3,
                      'Dolphins': 3,
                      'Patriots': 2,
                      'Chiefs': 3,
                      'fantasy team': 8,
                      'Chargers': 3,
                      'Broncos': 2,
                      'Raiders': 1}

largest_so_far = 'Raiders'
for team_name in afc_east_west_wins.keys():
    # The "keys" function knows to look at the 'names' based on how dictionaries are laid out.
    if afc_east_west_wins[largest_so_far] < afc_east_west_wins[team_name]:
        largest_so_far = team_name
print(f"The team with the most wins is {largest_so_far} with {afc_east_west_wins[largest_so_far]} wins.")
