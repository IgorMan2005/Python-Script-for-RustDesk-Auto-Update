from setuptools import setup

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='rustdesk-auto-update',
  version='1.0.0',
  author='IgorMan',
  author_email='igorman2005@gmail.com',
  description='Python Script for RustDesk Auto-Update',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/IgorMan2005/Python-Script-for-RustDesk-Auto-Update/',
  packages=['rustdesk_auto_update'],
  install_requires=['requests'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='openai image api open ai python',
  project_urls={
    'Documentation': 'https://best-itpro.ru/news/rustdesk-auto-update/',
  },
  python_requires='>=3.6'
)
