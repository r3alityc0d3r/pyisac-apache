"""
pyisac-apache2 class

Class to manage Apache2 on servers
"""
from Pyisac.core import Core, Database, Package

class Apache2(object):
    
    def __init__(self,node):
        os_type = "Ubuntu"
        if os_type == "Ubuntu":
            self.package_name = "apache2"
        apache_package = Package(self.package_name, node, "install")                                                                                
