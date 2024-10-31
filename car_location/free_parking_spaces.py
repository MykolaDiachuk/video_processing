from zones.enum_parking_area.enum_parking_spaces import ParkingSpaces


def find_free_zones(occupied_zones):
    """Повертає список вільних зон на основі зайнятих зон."""
    all_zones = set(ParkingSpaces)  # всі доступні зони на стоянці
    occupied_zones_set = set(occupied_zones)  # зайняті зони (результат попереднього коду)

    free_zones = all_zones - occupied_zones_set  # вільні зони - це ті, що не входять до зайнятих
    return list(free_zones)  # повертаємо вільні зони як список

