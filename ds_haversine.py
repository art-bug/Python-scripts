import numpy as np

def haversine(latitude1, longitude1, latitude2, longitude2, to_radians=True):
    '''
        Computes a distance between two geographic points.
        If to_radians flag is enabled (and it's enabled by default),
        then input points are translate into their radian representation.
        Returns a distance in km.
    '''
    if to_radians:
        latitude1, longitude1, latitude2, longitude2 = np.radians([latitude1, longitude1, latitude2, longitude2])

    radian_dist = 2 * np.arcsin( np.sqrt( np.sin((latitude2-latitude1) / 2.0)**2 +
                                          np.cos(latitude1) * np.cos(latitude2) *
                                          np.sin((longitude2-longitude1) / 2.0)**2 ))

    return 6371 * radian_dist    # 6371 - Earth radius

def __demonstrate():
    '''
        Demonstrates haversine using.
        Examples:
            dists = Series(haversine(carsharing_data['car_lat'], carsharing_data['car_lon'], \
                                     carsharing_data['finished_car_lat'], carsharing_data['finished_car_lon']))
    '''
    pass

if __name__ == '__main__':
    __demonstrate()