#include <iostream>
#include <cstdlib>
#include <cstring>
#include <malloc.h> // Required for _aligned_malloc/_aligned_free

int main() {
    size_t size = 1024;
    void* memory = _aligned_malloc(size, 8);
    if (!memory) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return 1;
    }

    std::memset(memory, 0, size);
    std::cout << "Memory allocated and initialized." << std::endl;

    _aligned_free(memory);
    return 0;
}
