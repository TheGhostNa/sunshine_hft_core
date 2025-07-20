#include <iostream>
#include <cstdlib>
#include <new>

int main() {
    size_t size = 1024;

    void* memory = std::malloc(size);
    if (!memory) {
        std::cerr << "Allocation failed" << std::endl;
        return 1;
    }

    std::cout << "Memory allocated at: " << memory << std::endl;

    std::free(memory);
    return 0;
}
