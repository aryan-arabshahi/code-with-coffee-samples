import setuptools


PROJECT_NAME = 'trex_runner'
PROJECT_VERSION = '1.0.0'
PROJECT_ENTRY_POINTS = """
[console_scripts]
trex-runner = trex_runner.cli.main:main
"""


def read_file(filename, return_as_array=True):
    empty_resp = [] if return_as_array else ''
    try:
        with open(filename) as f:
            if return_as_array:
                arr = f.readlines()
                arr = [x.strip() for x in arr]
                return arr
            else:
                return f.read()
    except:
        return empty_resp


def read_requirements():
    reqs = read_file('requirements.txt')
    return reqs


setuptools.setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    entry_points=PROJECT_ENTRY_POINTS,
    author="Aryan Arabshahi",
    author_email="aryan.arabshahi.programmer@gmail.com",
    description="The T-Rex runner player.",
    packages=setuptools.find_packages(),
    install_requires=read_requirements(),
    python_requires='>=3.6',
)