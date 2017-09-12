import argparse
import pymod2pkg


def main(args):
    with open(args.input_constraints, 'r') as input_file:
        for row in input_file:
            module = row.split(':')[0].split('===')[0]
            package = pymod2pkg.module2package(module, args.dist)
            print 'repoquery --qf "' + module + '===%{ver}  #%{name}-%{ver}-%{rel}.%{arch}" --whatprovides ' + package
            print 'repoquery --qf "' + module + '===%{ver}  #%{name}-%{ver}-%{rel}.%{arch}" --whatprovides ' + module


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Distro constraints')
    parser.add_argument('input_constraints', default='upper-constraints.txt',
                        help='Input constraints file to read in and process')
    # parser.add_argument('--dist', default='CentOS', action='store_const')
    args = parser.parse_args()

    args.dist = 'CentOS'
    main(args)
