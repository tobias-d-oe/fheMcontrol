#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.install import install
from subprocess import check_call


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        check_call("systemctl daemon-reload".split())
        check_call("systemctl enable fheMcontrol".split())
        install.run(self)

setup(name='fheMcontrol',
      version='1.0',
      description='mcontrol Gateway server for fhem',
      author='Tobias D. Oestreicher',
      author_email='lists@oestreicher.com.de',
      url='https://github.com/tobias-d-oe/fheMcontrol/',
      data_files=[('/etc/fheMcontrol', ['conf/fheMcontrol.cfg', 'conf/fheMcontrolServer.xml']),
                  ('/usr/bin/', ['src/fheMcontrolServer']),
                  ('/lib/systemd/system/', ['conf/fheMcontrol.service'])],
      cmdclass={'install': PostInstallCommand,},
     )



