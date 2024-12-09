from setuptools import setup, find_packages
import os

# 获取当前目录路径
here = os.path.abspath(os.path.dirname(__file__))

# 读取 README 文件内容作为 long_description
with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

# 使用 setuptools.setup 来定义安装过程
setup(
    name='cpu_rec',
    version='0.1',
    author='newton',
    author_email='littlenewton6@gmail.com',
    description='A CPU recognition project form from airbus-seclab/cpu_rec.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LittleNewton/cpu_rec',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['cpu_rec.c', 'cpu_rec.py', 'cpu_rec_corpus/*'],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
