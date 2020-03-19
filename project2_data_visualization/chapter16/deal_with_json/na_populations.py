# coding: utf-8

import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of countries in North America'
wm.add('Notrh America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

filename = r'project2_data_visualization\chapter16'
filename += r'\deal_with_json\na_population.svg'
wm.render_to_file(filename)