cmake_minimum_required(VERSION 3.16)

project(CONAN_Example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_MODULE_PATH "${CMAKE_BINARY_DIR};${CMAKE_MODULE_PATH}")
set(PROJECT_NAME "example")

add_executable(${PROJECT_NAME} main.cpp)

find_package(fmt REQUIRED)
if(fmt_FOUND)
    message("fmt FOUND")
    target_include_directories(${PROJECT_NAME} PRIVATE ${fmt_INCLUDE_DIRS})
    target_link_libraries(${PROJECT_NAME} PRIVATE ${fmt_LIBRARIES})
endif()