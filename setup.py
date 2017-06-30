from setuptools import setup, find_packages

setup(
    name='mordred-web',
    version='0.2.1',
    description='molecular descriptor calculator web UI',
    license='BSD3',
    author='Hirotomo Moriwaki',
    author_email='philopon.dependence@gmail.com',
    url='https://github.com/mordred-descriptor/mordred-web',
    platforms=['any'],
    keywords='QSAR chemoinformatics',
    packages=[
        'mordred.web',
        'mordred.web.handler',
    ],
    package_dir={
        'mordred.web': 'python/mordred_web',
        'mordred.web.handler': 'python/mordred_web/handler',
    },

    package_data={
        'mordred.web': [
            'static/*',
            'static/**/*',
        ],
    },

    install_requires=[
        'mordred>=0.3.1',
        'tornado>=4.5',
        'psutil>=5.0',
        'base58>=0.2.0',
        'numpy>=1.10',
        'six>=1.10',
        'loky>=1.0',
        'Pillow>=4.1'
    ],

)
