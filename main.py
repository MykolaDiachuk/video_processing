from car_location.car_centres.find_centres import get_car_centres
from car_location.free_parking_spaces import find_free_zones
from const import image_path
from zones.plot_zones import plot_parking_zones
from car_location.occupied_p_spaces import find_parking_zones
from PIL import Image

df = get_car_centres(image_path)

car_coordinates = list(zip(df['center_x'], df['center_y']))
image = Image.open(image_path)
image_width, image_height = image.size
image_size = (image_width, image_height)


occupied_zones = find_parking_zones(car_coordinates, image_size)
#plot_zones_with_centers(image_path, occupied_zones)

free_zones = find_free_zones(occupied_zones)
plot_parking_zones(image_path, occupied_zones, free_zones)

