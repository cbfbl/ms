
def calculate_damage_based_on_formula():
    skill = 0
    w_attack = 0
    main_stats = 0
    multiplier = 0
    secondary = 0
    attack_power = 0
    physical_max = skill * w_attack * (1 + (main_stats * multiplier + secondary + 2 * attack_power) / 100)
