import setuptools

setuptools.setup(
    name="distro_constraints",
    version="0.1.0",
    url="https://github.com/yazug/distro_constraints",

    author="Jon Schlueter",
    author_email="jschluet@redhat.com",

    description="Python tool to complete the circle of constraints to distro binary packages back to a constraints based file given currently available packages.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['pymod2pkg', 'pip>=7.1'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
