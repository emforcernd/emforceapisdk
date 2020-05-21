from setuptools import setup, find_packages

setup(
    name             = 'emforceapisdk',
    version          = '0.1.4.10',
    description      = 'Emforce Python sdk for media api',
    author           = 'Jimin Park',
    author_email     = 'parkjiminy@gmail.com',
    url              = 'https://github.com/emforcernd/emforceapisdk',
    # download_url     = 'https://github.com/emforcernd/emforceapisdk/archive/0.1.1.1.tar.gz',
    install_requires    =  [
        'google-api-python-client == 1.8.3',
        'facebook_sdk == 4.0.0rc0',
    ],
    dependency_links =[
        'https://github.com/mobolic/facebook-sdk.git@ffd9980700be48964d6a6a61144edb1c3ea29cff#egg=facebook_sdk-4.0.0rc0'
    ],
    packages            = find_packages(exclude = []),
    keywords            = ['emforce','emforceapisdk'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)