"""Imports the unguarded module: its test table runs as a side effect."""
print("before import")
import milkrate_no_main
print("after import - the table above was printed even though we only wanted the functions")
