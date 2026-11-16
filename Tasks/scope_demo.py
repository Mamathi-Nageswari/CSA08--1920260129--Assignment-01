"""Task 6 - Local and global names."""
BASE_RATE = 30.00


def read_global():
    """Reads the global constant: allowed and safe."""
    return BASE_RATE + 2.80


def shadow_global():
    """Assigning creates a new LOCAL name; the global is untouched."""
    BASE_RATE = 99.0
    return BASE_RATE


def change_global():
    """With 'global' the function really changes the rate card (do not do this)."""
    global BASE_RATE
    BASE_RATE = 31.00


def broken():
    """Reading then assigning the same name in one function fails."""
    total = BASE_RATE + 1
    BASE_RATE = total
    return BASE_RATE


print("read_global()   ->", read_global(), "| BASE_RATE =", BASE_RATE)
print("shadow_global() ->", shadow_global(), "| BASE_RATE =", BASE_RATE)
try:
    broken()
except UnboundLocalError as error:
    print("broken()        -> UnboundLocalError:", error)
change_global()
print("change_global() -> BASE_RATE is now", BASE_RATE, "for every later payment!")


def local_only():
    """fat_steps exists only while this function runs."""
    fat_steps = 7
    return fat_steps


print("local_only()    ->", local_only(), "| 'fat_steps' visible outside:", "fat_steps" in globals())
