from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='medialog.maxtheme',
      version=version,
      description="Medialog Maxtheme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='Plone Theme Maxtheme',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.maxtheme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
    	  'collective.portlet.itemview',
          'collective.ptg.nivoslider',
          'collective.ptg.tile',
    	  'collective.vaporisation',
          'medialog.hidetitle',
    	  'medialog.imageexport',
          'medialog.issuu',
          'medialog.newsitemview',
          'medialog.portlet.placeholder',
          'medialog.qrcode',
          'plone.app.dexterity',
          'plone.app.contenttypes',
          'plonetheme.classic',
          'Products.Maps',
          'redturtle.smartlink',
          'sc.social.like',
          'wildcard.foldercontents',
          'ftw.mobilenavigation',
          
          
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
