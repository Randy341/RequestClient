from distutils.core import setup
setup(
    name="RequestClient",
    package=["RequestClient"],
    version="0.1.0",
    license="MIT",
    description="Easy-to-use request wrapper that saves coding time",
    author="Randy Chang",
    author_email="randy@randy-chang.com",
    url="https://github.com/Randy341/RequestClient",
    download_url="",
    keywords=["requests","HTTP","wrapper", "client"],
    install_requires=["requests","pydash"],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)