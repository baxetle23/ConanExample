from conans import ConanFile, CMake

class Example(ConanFile):
    name = "Example"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package"
    requires = [
        ("fmt/9.1.0")
    ]