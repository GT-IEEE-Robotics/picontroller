from setuptools import setup

setup(name='gatech-ieee-picontroller',
      version='0.1',
      description='High-level python interface to control robot for IEEE competition',
      url='http://github.com/grokkingStuff/picontroller',
      author='Vi Kumar',
      author_email='grokkingStuff@gmail.com',
      license='',
      packages=find_packages(),
      install_requires=['numpy',
                        'logging',
                        'warning'],
      python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
      zip_safe=False)
