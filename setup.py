from distutils.core import setup
import os


setup(
    name='tfora_social_auth',
    packages=['tfora_social_auth'], 
    version='0.3',     
    license='MIT',
    description='Easy django rest auth integration for social applications (currently supports google and facebook)',
    author='Ummer Farooq',                   
    author_email='farooq.tfora@gmail.com',      
    url='https://github.com/pvfarooq/tfora_social_auth',
    download_url='https://github.com/pvfarooq/tfora_social_auth/archive/refs/tags/0.3.tar.gz',
    keywords=['django', 'social login', 'allauth', 'rest_auth','google login','facebook login'],
    install_requires=[            
        'facebook-sdk',
        'google-auth',
        'requests',
        'djangorestframework'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

