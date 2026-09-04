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
else()
  set(lib_type STATIC)
  set(scope_keyword PUBLIC)
endif()

add_library(burd-lib ${lib_type})

target_compile_features(burd-lib
  ${scope_keyword}
    cxx_std_20
)

if(LIB_HEADER_ONLY)
  target_compile_definitions(burd-lib
    ${scope_keyword}
      BURD_LIB_HEADER_ONLY
  )
endif()

target_include_directories(burd-lib
  ${scope_keyword}
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

if(NOT LIB_HEADER_ONLY)
  target_sources(burd-lib
    PRIVATE
      src/stub.cpp
  )
endif()

add_library(burd::burd-lib ALIAS burd-lib)
