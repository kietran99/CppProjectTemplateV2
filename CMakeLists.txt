cmake_minimum_required(VERSION 3.28.2)

file(STRINGS VERSION LIB_VERSION LIMIT_COUNT 1)

if(NOT LIB_VERSION MATCHES [[^[0-9]+\.[0-9]+\.[0-9]+$]])
  message(FATAL_ERROR "Version must be in x.y.z format")
endif()

project(burd-lib VERSION ${LIB_VERSION} LANGUAGES CXX)

option(LIB_HEADER_ONLY "Does this library contain only header files" OFF)

if(LIB_HEADER_ONLY)
  set(lib_type INTERFACE)
  set(scope_keyword INTERFACE)
  set(lib_sources "")
  set(lib_definitions BURD_LIB_HEADER_ONLY)
else()
  set(lib_type STATIC)
  set(scope_keyword PUBLIC)
  set(lib_sources src/stub.cpp)
  set(lib_definitions "")
endif()

add_library(burd-lib ${lib_type} ${lib_sources})

target_compile_features(burd-lib
  ${scope_keyword}
    cxx_std_20
)

target_compile_definitions(burd-lib
  ${scope_keyword}
    ${lib_definitions}
)

target_include_directories(burd-lib
  ${scope_keyword}
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

add_library(burd::burd-lib ALIAS burd-lib)
