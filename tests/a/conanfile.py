
import os
import importlib
import sys
import re
import shutil
import glob
import os.path as path
from textwrap import dedent
from conans import ConanFile, tools
from conan.tools.cmake import CMakeDeps, CMakeToolchain, CMake
from conans.tools import Version
from conan.tools.layout import cmake_layout


class BaseLibrary(ConanFile):
  name = "base"

  description = """This is a test project with a library base::io
    and base::math and an executable cli."""
  version = "1.0.0"
  license = "MIT"
  url = "asd"
  homepage = "asd"
  default_options = {
      "fmt:shared": False
  }  #shared libraries not fully working under windows yet.
  build_policy = "missing"  # if this package is build by default if missing.
  settings = "os", "compiler", "build_type", "arch"

  def export(self):
    self.copy("link/b/Readme.md")
