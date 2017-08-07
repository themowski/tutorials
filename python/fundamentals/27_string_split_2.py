# Try to parse a list of variant calls produced by VarScan (http://sourceforge.net/projects/varscan/).

# See what the file looks like before we parse it.
with open('varscan.out') as f:
    for line in f.readlines():
        print line.rstrip()
print

calls = []
with open('varscan.out') as f:
    for line_i, line in enumerate(f.readlines()):
        if line_i == 0:
            headers = line.split() # Split on whitespace
            headers = headers[:10] # Drop off some ugliness at the end
            # print 'Headers', headers
            continue

        values = line.split()
        print 'Values split', values
        values = values[:10] # Drop off the same ugliness
        call = {}
        for header, value in zip(headers, values):
            if ':' in value:
                # Multi-value column
                header_split = header.split(':')
                print 'Header split', header_split
                value_split = value.split(':')
                nested_values_dict = {}
                for nested_header, nested_value in zip(header_split, value_split):
                    nested_values_dict[nested_header] = nested_value
                # Alternatively, use a dict comprehension with the same semantics as the three lines above:
                # nested_values_dict = dict((nested_header, nested_value) for nested_header, nested_value in zip(header_split, value_split))
                call['Nested' + str(len(call))] = nested_values_dict
            else:
                # Single-value column
                call[header] = value
        calls.append(call)
        print 'Values dictionary', list(sorted(call.items()))
print

print "Variants"
for call in calls:
    print call['Chrom'], int(call['Position']), call['Ref'], call['Var']
