#!python3
# NOTE: This works well on Linux systems, but may be problematic in Windows systems
#       since they do not have built-in C++ compilers.

import cppyy

cppyy.cppdef("""
void say_hello() {
     std::cout << "Hello Python!" << std::endl;
}
""")

cppyy.gbl.say_hello()

print("Hello C++!")
