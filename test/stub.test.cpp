#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest/doctest.h"

#include "burd-lib/stub.h"

TEST_CASE("Add returns the sum")
{
    CHECK(burd::Add(1, 3) == 4);
    CHECK(burd::Add(2, 3) == 5);
}
