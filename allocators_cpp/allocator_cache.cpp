#include <iostream>
#include <cstdlib>
#include <cstdint>

void* aligned_malloc(size_t size, size_t alignment) {
    uintptr_t raw = (uintptr_t)std::malloc(size + alignment - 1 + sizeof(void*));
    if (!raw) return nullptr;

    uintptr_t aligned = (raw + sizeof(void*) + alignment - 1) & ~(alignment - 1);
    ((void**)aligned)[-1] = (void*)raw;
    return (void*)aligned;
}

void aligned_free(void* aligned_ptr) {
    if (aligned_ptr)
        std::free(((void**)aligned_ptr)[-1]);
}

int main() {
    const size_t size = 1024;
    const size_t alignment = 64;

    void* memory = aligned_malloc(size, alignment);
    if (!memory) {
        std::cerr << "Manual aligned allocation failed." << std::endl;
        return 1;
    }

    std::cout << "✅ Aligned memory allocated at: " << memory << std::endl;

    aligned_free(memory);
    return 0;
}
