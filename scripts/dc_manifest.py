#!dc_manifest
"""
list deluge_card contents of folder specified
"""
import argparse
from deluge_card import DelugeCardFS
from deluge_card.deluge_card import InvalidDelugeCard, list_deluge_fs

def list_songs(card):
	cs = card.songs()
	print(f'Deluge filesystem has {len(cs)} songs')
	for s in cs:
		print(f'  song {s} key {s.scale()}')

def list_samples(card):
	cs = card.samples()
	print(f'Deluge filesystem has {len(cs)} samples')
	for s in cs:
		print(f'  sample: {s}')



if __name__ == '__main__':
	print('dc_manifest')
	parser = argparse.ArgumentParser(description='list deluge_card contents')
	parser.add_argument('folder', type=str, nargs='+',
	                    help='one or more folder to check')
	parser.add_argument('-l', '--list', nargs='+',
	                    help='include listing of s=songs, S=samples, K=Kit, I=instrument')

	args = parser.parse_args()
	print(args.folder)
	
	for fname in args.folder:
		card_imgs = list_deluge_fs(fname)
		if len(card_imgs):
			for c in card_imgs:
				print(f'Deluge filesystem at {c.card_root()} mounted: {c.is_mounted()}')
				opts = [x for x in ''.join(args.list)]
				print(opts)
				if 's' in opts:
					print('Songs')
					list_songs(c)

				if 'S' in opts:
					print('Samples')
					list_samples(c)