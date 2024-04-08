from setuptools import setup, find_packages
setup(
    name = "dtreg",
    version = "0.1",
    description = "Clean package",
    packages = find_packages() + ['templates'],
    include_package_data = True
)
if __name__ == '__main__':
    setup()