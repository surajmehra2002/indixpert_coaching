# Setexample = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
# what is the size of this SET

import sys

# def get_size(obj, seen=None):
#     """Recursively finds the size of objects, including nested objects."""
#     size = sys.getsizeof(obj)
#     if seen is None:
#         seen = set()
#     obj_id = id(obj)
#     if obj_id in seen:
#         return 0
#     seen.add(obj_id)

#     if isinstance(obj, dict):
#         size += sum([get_size(v, seen) for v in obj.values()])
#         size += sum([get_size(k, seen) for k in obj.keys()])
#     elif hasattr(obj, '__dict__'):
#         size += get_size(obj.__dict__, seen)
#     elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
#         size += sum([get_size(i, seen) for i in obj])

#     return size

# Example usage
Setexample11 = {"Geek1", "Raju", "Geek2", "Nikhil","Geek3","Suraqqqqq"}
size = sys.getsizeof(Setexample11)

print(f"Size of the set in memory: {size} bytes")
