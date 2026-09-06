import os
import re

from conan import ConanFile
from conan.errors import ConanException
from conan.tools.files import load
from conan.tools.cmake import cmake_layout, CMakeDeps, CMakeToolchain

class BurdRecipe(ConanFile):
    name = "burd-lib"
    settings = "os", "compiler", "build_type", "arch"
    _default_generator = "Ninja"

    def set_version(self):
        version = (load(self, os.path.join(self.recipe_folder, "VERSION")).splitlines() or [""])[0].strip()
        if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
            raise ConanException("Version must be in x.y.z format")
        self.version = version

    def build_requirements(self):
        self.test_requires("doctest/2.4.12")

    def layout(self):
        cmake_layout(self, generator=self._default_generator)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self, generator=self._default_generator)
        tc.user_presets_path = None
        tc.generate()
