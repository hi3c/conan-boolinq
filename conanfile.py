from conans import ConanFile, CMake, tools
import os

SHA1="1468eff8df78f322d69a5c7b7e47dff38bd8d2e1"

class BoolinqConan(ConanFile):
    name = "boolinq"
    version = "1468eff"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.download("https://github.com/k06a/boolinq/archive/{}.zip".format(SHA1), "boolinq.zip")
        tools.unzip("boolinq.zip")
        os.remove("boolinq.zip")

    def package(self):
        self.copy("*.h", dst="include", src="boolinq-{}/include".format(SHA1))

    def package_info(self):
        self.cpp_info.libs = []
        self.cpp_info.libdirs = []
