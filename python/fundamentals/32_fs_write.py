# We can also write to files using a similar construct:
with open('regents.csv',) as f_in: # Implicit 'r' file mode = open for reading, error if it doesn't exist
    with open('regents_copy.csv', 'w+') as f_out: # w = open for writing, + = truncate the file if it already exists
        data = f_in.read()
        f_out.write(data)

# Note that the "copy" may not be identical to the original because opening
# the files in the manner above translates line endings between platforms.
# i.e., if regents.csv has Unix \n line endings (it does) and we write
# a new file on Windows it will have Windows-native line endings (\r\n).
# Usually we don't care, but occasionally we want to preserve original
# line endings. In this case we open the file in "binary mode":
with open('regents.csv', 'rb') as f_in:
    with open('regents_copy.csv', 'w+b') as f_out:
        data = f_in.read()
        f_out.write(data)
# The other, implicit mode that translates line endings is called "text mode".
