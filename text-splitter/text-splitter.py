def split_file(input_file, output_prefix, lines_per_file):
    with open(input_file, 'r', encoding="utf8") as f:
        lines = f.readlines()
    
    lines = [line for line in lines if line.strip()]
        
    num_files = len(lines) // lines_per_file + 1
    
    for i in range(num_files):
        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w', encoding="utf8") as f:
            start = i * lines_per_file
            end = (i + 1) * lines_per_file
            f.writelines(lines[start:end])




split_file('text-splitter\input.txt', 'text-splitter/out/output_file', 10)

