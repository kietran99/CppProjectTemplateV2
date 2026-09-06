find_package(doctest REQUIRED)

add_executable(burd-lib-tests stub.test.cpp)

target_link_libraries(burd-lib-tests
  PRIVATE
    doctest::doctest
    burd::burd-lib
)

include(doctest OPTIONAL RESULT_VARIABLE doctestFound)
if(COMMAND doctest_discover_tests)
  doctest_discover_tests(burd-lib-tests)
else()
  if(doctestFound STREQUAL NOTFOUND)
    message(WARNING "doctest.cmake wasn't found on CMAKE_MODULE_PATH.
      Falling back to running a single test entry. See ctest -N.")
  else()
    message(WARNING "doctest_discover_tests wasn't defined in doctest.cmake.
      Falling back to running a single test entry. See ctest -N.")
  endif()
  add_test(NAME fallback COMMAND burd-lib-tests)
endif()
