# Sync specified sidebearings to other layers for selected glyphs in Edit View
# PKM 2022-03-23
#

# User-configurable values
source_layer  = 'Regular'
#side_bearings = ['Left','Right'] # Values: 'Left', 'Right'
side_bearings = ['Left']
#side_bearings = ['Right']
dest_layers   = ['Black']
label_colour   = 5  # 0 = no change

print()
print('Copying "{}" sidebearings from {} to {}'.format(side_bearings, source_layer, dest_layers))
print()

for selection_layer in Glyphs.font.selectedLayers:
	g = selection_layer.parent
	print(g.name)
	changed = False
	for dest_layer in dest_layers:

		if 'Left' in side_bearings:
			source_LSB = g.layers[source_layer].LSB
			dest_LSB_orig   = g.layers[dest_layer].LSB
			g.layers[dest_layer].LSB = source_LSB
			dest_LSB_new   = g.layers[dest_layer].LSB
			if dest_LSB_orig != dest_LSB_new:
				changed = True
				print('LSB changed from {} to {}'.format(dest_LSB_orig, dest_LSB_new))
			else:
				print('LSB unchanged at {}'.format(dest_LSB_orig))

		if 'Right' in side_bearings:
			source_RSB = g.layers[source_layer].RSB
			dest_RSB_orig   = g.layers[dest_layer].RSB
			g.layers[dest_layer].RSB = source_RSB
			dest_RSB_new   = g.layers[dest_layer].RSB
			if dest_RSB_orig != dest_RSB_new:
				changed = True
				print('RSB changed from {} to {}'.format(dest_RSB_orig, dest_RSB_new))
			else:
				print('RSB unchanged at {}'.format(dest_RSB_orig))

	if changed & label_colour != 0:
		g.color = label_colour
	print()

print('-----------------------------------------------------------------')
