# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line

### Part 1 ###

# Namen doelpunten makers
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

# Minuut waarin gescoord is
goal_0 = 32
goal_1 = 54

# Doetpunten maker(s) + minuut waarin gescoord is
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

# Doelpunten makers + minuut op elk een eigen line
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"

### Part 2 ###

# Naam voetballer
player = "Jan Wouters"

# Get first name
name_space = player.find(" ")

first_name = player[:name_space]

# Get last name
total_lenght = len(player)
last_name = player[name_space:total_lenght]
last_name_no_space = last_name[1:]
last_name_len = len(last_name_no_space)

# Verkort naam naar J. Wouters
name_short = f"{first_name[0]}.{last_name}"

# Maak een chant met 3x voornaam + !

# Variabele met ! + space
first_name_addon = first_name + "! "
chant_with_space = first_name_addon * 3

# Zorg dat laatste character geen spatie is
chant = chant_with_space[:-1]

# Controleer of laatste character van Chant een spatie is
check_last_chant = chant[:]

# Controleer of dit een spatie is met een NOT EQUAL (!=) Uitkomst moet TRUE zijn (is niet gelijk aan)
good_chant = check_last_chant != " "
