import argparse

def parse_args():
    
	parser = argparse.ArgumentParser(description='Model Params')
	parser.add_argument('--lr', default=1e-3, type=float, help='learning rate')
	parser.add_argument('--batch', default=1, type=int, help='batch size')
	parser.add_argument('--reg', default=0, type=float, help='weight decay regularizer')
	parser.add_argument('--spreg', default=0, type=float, help='weight decay regularizer')
	parser.add_argument('--epoch', default=10, type=int, help='number of epochs')
	parser.add_argument('--decay', default=0.96, type=float, help='weight decay rate')
	parser.add_argument('--save_path', default='tem', help='file name to save model and training record')
	parser.add_argument('--load_model', default=None, help='model name to load')
	parser.add_argument('--latdim', default=16, type=int, help='embedding size')
	parser.add_argument('--spacialRange', default=2, type=int, help='number of hops for spacial message propagation')
	parser.add_argument('--temporalRange', default=30, type=int, help='number of hops for temporal features')
	parser.add_argument('--temporalGnnRange', default=7, type=int, help='number of gnn iterations for temporal message propagation')
	parser.add_argument('--data', default='crime_reports', type=str, help='name of dataset')
	parser.add_argument('--tstEpoch', default=1, type=int, help='number of epoch to test while training')
	parser.add_argument('--head', default=4, type=int, help='number of attention head')
	parser.add_argument('--negRate', default=4, type=int, help='rate of neg v.s. pos samples while training')
	parser.add_argument('--border', default=0.5, type=float, help='border line for pos and neg predictions')
	parser.add_argument('--hyperNum', default=128, type=int, help='number of hyper edges')
	parser.add_argument('--dropRate', default=0.0, type=float, help='drop rate for dropout')
	parser.add_argument('--task', default='r', type=str, help='classification or regression')
	return parser.parse_args()

args = parse_args()