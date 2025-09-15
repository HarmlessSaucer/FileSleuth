import os
import argparse

def collect_file_info(directory):
    file_info_list = []

    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            name, ext = os.path.splitext(file)
            try:
                size = os.path.getsize(full_path)
            except OSError:
                size = -1  # In case file is inaccessible
            file_info_list.append((file, ext[1:] if ext else '', size))

    return file_info_list

def human_readable_size(size_bytes):
    if size_bytes < 0:
        return "Unknown size"
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def format_file_info(file_info_list, human_readable=False):
    lines = []
    for name, ext, size in file_info_list:
        size_str = human_readable_size(size) if human_readable else f"{size} bytes"
        lines.append(f"{name} | Extension: {ext or 'None'} | Size: {size_str}")
    return lines

def main():
    parser = argparse.ArgumentParser(description="List all files in a folder (recursively) with name, extension, and size.")
    parser.add_argument("path", help="Path to the folder to scan")
    parser.add_argument("-o", "--output", help="Optional path to output text file")
    parser.add_argument("-H", "--human", action="store_true", help="Display file sizes in human-readable format")
    parser.add_argument("--sort", choices=["name", "size"], default="name", help="Sort by 'name' (default) or 'size'")

    args = parser.parse_args()
    folder_path = args.path
    output_file = args.output
    human_flag = args.human
    sort_method = args.sort

    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory or does not exist.")
        return

    file_info = collect_file_info(folder_path)

    if sort_method == "name":
        file_info.sort(key=lambda x: x[0].lower())
    elif sort_method == "size":
        file_info.sort(key=lambda x: x[2], reverse=True)

    formatted = format_file_info(file_info, human_readable=human_flag)

    for line in formatted:
        print(line)

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(formatted))
            print(f"\nFile list written to: {output_file}")
        except Exception as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
  
