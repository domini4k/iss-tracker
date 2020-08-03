import requests
import matplotlib.pyplot as plt
import time
from mpl_toolkits.basemap import Basemap

plt.ion()
fig = plt.figure(figsize=(8, 6), edgecolor='w')
fig.add_subplot(2, 1, 1)
m1 = Basemap(projection='cyl', resolution=None,
             llcrnrlat=-90, urcrnrlat=90,
             llcrnrlon=-180, urcrnrlon=180)
m1.etopo(scale=0.5, alpha=0.5)


while True:
    # Request data from api
    data = requests.get('http://api.open-notify.org/iss-now.json')
    position = data.json()['iss_position']
    latitude = float(position['latitude'])
    longitude = float(position['longitude'])

    # draw first map
    x1, y1 = m1(longitude, latitude)
    dot_m1 = plt.plot(x1, y1, 'ro', markersize=1)
    text_m1 = plt.text(x1, y1, ' ISS', fontsize=12)
    # draw second map
    plt.subplot(2, 1, 2)
    m2 = Basemap(width=6000000, height=4500000,
                 resolution=None, area_thresh=1000, projection='lcc',
                 lat_1=latitude-5, lat_2=latitude+5,
                 lat_0=latitude, lon_0=longitude)
    m2.bluemarble(scale=0.5, alpha=0.7)

    x2, y2 = m2(longitude, latitude)
    dot_m2 = plt.plot(x2, y2, 'ro', markersize=2)
    text_m2 = plt.text(x2, y2, ' ISS', fontsize=12)

    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(5)

    # delete unnecessary data from chart
    plt.subplot(2, 1, 1)
    text_m1.remove()
    plt.plot(x1, y1, 'ok', markersize=1)


