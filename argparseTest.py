import argparse

# def required_length(nmin,nmax):
#     class RequiredLength(argparse.Action):
#         def __call__(self, parser, args, values, option_string=None):
#             if not nmin<=len(values)<=nmax:
#                 msg='argument "{f}" requires between {nmin} and {nmax} arguments'.format(
#                     f=self.dest,nmin=nmin,nmax=nmax)
#                 raise argparse.ArgumentTypeError(msg)
#             setattr(args, self.dest, values)
#     return RequiredLength

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
# parser.add_argument('-f', nargs='+', action=required_length(2,3))

args = parser.parse_args()
print args
print args.accumulate(args.integers)