import argparse
import pymod2pkg
import subprocess


def main(args):
    with open(args.input_constraints, 'r') as input_file:
        for row in input_file:
            module = row.split(':')[0].split('===')[0]
            # split and guard on foo==1.2.3;python_version='2.7'
            python_version = None
            if ';python_version' in row:
                python_version = row.strip().split(';')[1]
                if args.python_version not in python_version:
                    print module + ';' + python_version
                    continue
            package = pymod2pkg.module2package(module, args.dist)
            cmd = None
            if args.dist in ('CentOS', 'RDO', 'RHEL'):
                # centos
                cmd = [
                    'repoquery', '--quiet', '--whatprovides', package,
                    '--qf', '%{ver} %{epoch}:%{name}-%{ver}-%{rel}.%{arch}'
                ]
            if args.dist == 'fedora':
                cmd = [
                    'dnf', 'repoquery', '--quiet', '--whatprovides', package,
                    '--qf',
                    '%{version} %{epoch}:%{name}-%{version}-%{release}.%{arch}'
                ]
            if cmd is None:
                print "dist not recognized [{0}]".format(args.dist)
                break

            output = None
            try:
                output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            except Exception as e:
                print e
                print output

            if output is not None:

                max_ver = None
                max_nvr = None
                for line in output.split('\n'):
                    if len(line) > 0:
                        ver, nvr = line.split(' ')
                        if ver > max_ver or max_ver is None:
                            max_ver = ver
                            max_nvr = nvr

                if max_ver is not None:
                    if python_version is not None:
                        max_ver = max_ver + ';' + python_version
                    print "{0}==={1} # {2}".format(module, max_ver, max_nvr)
                else:
                    if python_version is not None:
                        print module + ';' + python_version
                    else:
                        print module


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Distro constraints')
    parser.add_argument('input_constraints', default='upper-constraints.txt',
                        help='Input constraints file to read in and process')
    args = parser.parse_args()

    args.dist = 'CentOS'
    args.python_version = '2.7'
    main(args)
