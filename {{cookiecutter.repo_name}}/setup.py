from setuptools import setup, find_packages

version = "{{ cookiecutter.version }}"

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name="{{ cookiecutter.repo_name }}",
    version=version,
    description="{{ cookiecutter.description }}",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="",
    author="{{ cookiecutter.author }}",
    author_email="",
    url="{{ cookiecutter.url }}",
    license="GPL",
    packages=find_packages(),
    namespace_packages=['{{ cookiecutter.namespace_package }}'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
{% if cookiecutter.add_robot_tests|int() > 0 %}
    extras_require={'test': ['plone.app.testing[robot]>=4.2.2']},
{% else %}
    extras_require={'test': ['plone.app.testing']},
{% endif %}
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
