# Step 1: Packaging the GUI as a standalone app using setuptools
# Create setup.py

from setuptools import setup, find_packages

setup(
    name='datasaver-gui',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'notify2',
        'pyudev'
    ],
    entry_points={
        'gui_scripts': [
            'datasaver-gui = datasaver_gui:main'
        ]
    },
    include_package_data=True,
    author='ostronics',
    description='Datasaver GUI utility with lid event monitoring',
    license='Apache2.0',
)

# Step 2: Create a desktop entry file for system launchers
# Save this as datasaver.desktop under /usr/share/applications/

[Desktop Entry]
Name=Datasaver GUI
Comment=Toggle MTU settings to save data
Exec=datasaver-gui
Icon=/datasaver/assets/datasaver.ico
Terminal=false
Type=Application
Categories=Network;Utility;
StartupNotify=true
