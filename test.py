import carla
client = carla.Client('localhost', 2000)
client.set_timeout(2.0)

world = client.get_world()
blueprint_library = world.get_blueprint_library()