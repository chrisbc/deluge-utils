#!dc_manifest
"""
list deluge_card contents of folder specified
"""
import argparse
from deluge_card import DelugeCardFS
from deluge_card.deluge_card import InvalidDelugeCard, list_deluge_fs


if __name__ == '__main__':
	print('dc_manifest')
	parser = argparse.ArgumentParser(description='list deluge_card contents')
	parser.add_argument('folder', type=str, nargs='+',
	                    help='one or more folder to check')
	args = parser.parse_args()
	print(args.folder)
	
	for fname in args.folder:
		card_imgs = list_deluge_fs(fname)
		if len(card_imgs):
			for c in card_imgs:
				print(f'Deluge filesystem at {c.card_root()} mounted: {c.is_mounted()}')
