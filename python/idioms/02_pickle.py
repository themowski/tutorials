import pickle
import tempfile

# Simple Python object marshalling
obj = ('tuple', 'I', 'want', 'to', 'save')
with tempfile.TemporaryFile() as f:
    pickle.dump(obj, f)
    f.seek(0) # Read from the beginning of the file
    unpickled_obj = pickle.load(f)
    print unpickled_obj