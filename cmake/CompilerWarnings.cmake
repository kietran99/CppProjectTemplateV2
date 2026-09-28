function(burd_set_warnings target)
  set(msvc_warnings /W4 /Wpermissive- /w14640)
  set(gcc_clang_warnings
    -Wall -Wextra -Wpedantic -Wshadow -Wsign-conversion
    -Wnon-virtual-dtor -Wold-style-cast -Wcast-align -Woverloaded-virtual
    -Wunused
  )
  if(MSVC)
    target_compile_options(${target} PRIVATE ${msvc_warnings})
  else()
    target_compile_options(${target} PRIVATE ${gcc_clang_warnings})
  endif()
endfunction()
