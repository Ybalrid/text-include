# text-include

Simple Phyton3 script that generate code to embed a text file into a C++11 program.

The C++ implementation must support [raw string literals](https://en.cppreference.com/w/cpp/language/string_literal).


# Usage

```bash
./text-include.py some_file.txt token > embeded_text_file.inl.h
```

This will read the content of `some_file.txt` and produce a header file containing a defintion of the following form:

```cpp
static const char* some_file_txt = R"token(
//This is the content of some_text.txt
)token"R;
