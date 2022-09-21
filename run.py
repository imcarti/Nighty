import marshal
from pytransform import pyarmor_runtime

pyarmor_runtime()

print("Cracked by COC (svenskithesource)")
exec(marshal.loads(open("cracked_nightly", "rb").read()))
