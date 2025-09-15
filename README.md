# FileSleuth

FileSleuth is a very simple tool that will walk a directory (and it's subdirectories) on your system. It will return a list of the file names and their sizes.

&nbsp;

## Why?

This script came about because I wanted to work on some media on my file server.  I was experiencing issues with doing this through the terminal on this Linux box and I wanted to be able to trigger this as part of another script.
Plus, I wanted a bit of a challenge to make something.

&nbsp;

## Features

- List all files in a folder (recursively) and output name, extension, and size
- Sorting by size or filename
- Output to terminal or text file

&nbsp;

## To-Do

- Add options for showing/hiding hidden files.

&nbsp;

## Installation

Clone the repository:

```bash
git clone https://github.com/HarmlessSaucer/FileSleuth.git
cd FileSleuth
```

&nbsp;

## Usage

Run the application:

```bash
filesleuth [options] /path/to/folder
```

&nbsp;

## Options

- `-h` - Display help menu
- `-H` or `--human` - Show file sizes in a more human-readable format
- `--sort` - Sort by `name` or `size` e.g.
  - `--sort name`
  - `--sort size`
- `-o` or `--output` - Optional path to output text file
