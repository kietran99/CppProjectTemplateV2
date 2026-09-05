#pragma once

namespace burd
{
#if defined(BURD_LIB_HEADER_ONLY)
inline int Add(int a, int b)
{
    return a + b;
}
#else
int Add(int a, int b);
#endif
}
