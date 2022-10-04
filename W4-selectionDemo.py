us_recession_start_years = [1920, 1923, 1926, 1929, 1937, 1945, 1949, 1953, 1958, 1960, 1969, 1973, 1980, 1981, 1990,
                            2001, 2008, 2020]
total_election_years = 0
# Assigning it to an integer
for years in us_recession_start_years:
    if years % 4 == 0:
        # total_election_years = total_election_years+1
        total_election_years += 1
        # shortcut way of saying the previous comment
# Remember, "=" is NOT "equal to", it is ASSIGNING a value to a variable. "==" is equal to. "!=" is DNE (does not equal)
        print(f"there was a recession in {years}")
print(f"there were {total_election_years} recessions in election years 1920-2020")
