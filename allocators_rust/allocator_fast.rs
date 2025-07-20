use std::alloc::{alloc_zeroed, dealloc, Layout};
use std::time::Instant;
use std::ptr;

fn main() {
    let size: usize = 1024 * 1024; // 1MB
    let alignment: usize = 8;

    // Define memory layout
    let layout = match Layout::from_size_align(size, alignment) {
        Ok(l) => l,
        Err(e) => {
            eprintln!("❌ Invalid layout: {}", e);
            return;
        }
    };

    let start = Instant::now();

    // Allocate memory
    let memory = unsafe { alloc_zeroed(layout) };

    if memory.is_null() {
        eprintln!("❌ Rust aligned allocation failed.");
        return;
    }

    println!("✅ Rust Allocation succeeded (1MB aligned block)");

    // Use the memory (optional write)
    unsafe {
        ptr::write_bytes(memory, 1u8, size);
    }

    // Deallocate memory
    unsafe {
        dealloc(memory, layout);
    }

    let duration = start.elapsed();
    println!("⚡ Allocation + Deallocation took: {} ms", duration.as_millis());
}
