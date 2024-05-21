import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="calculate_savings",
    version="0.0.1",
    author="YukiTakenaka",
    author_email="s2222024@stu.musashino-u.ac.jp",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takenakayuuki0901/calculate_savings.git",
    project_urls={
        "Bug Tracker": "https://github.com/takenakayuuki0901/calculate_savings.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=["calculate_savings"],
    packages=setuptools.find_packages(where="sre"),
    python_requires=">=3.7",
    entry_points={"console _scripts": ["calculate_savings = calculate_savings:main"]},
)
