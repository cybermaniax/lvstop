from pybuilder.core import use_plugin,Author,init

use_plugin("python.core")
use_plugin("python.distutils")

default_task = "publish"
description = """Linux Virtual Server (LVS) Top. Tool for LVS admins"""
authors = [Author("Grzegorz Halajko", "ghalajko+lvstop@gmail.com")]

@init
def initialize(project):
    project.version = "0.1.0"