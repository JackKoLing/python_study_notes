# coding: utf-8
import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
        'gy', 'pe', 'py', 'sr', 'uy', 've'])

filename = r'project2_data_visualization\chapter16\deal_with_json\americas.svg'
wm.render_to_file(filename)