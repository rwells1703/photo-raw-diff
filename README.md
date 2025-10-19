# Photo Raw Diff

This script looks for camera raw image files and checks for any compressed images with the same name. It can list the raw files that don't have a compressed version and also delete them if you choose.

This is handy for quickly reviewing or deleting images based on the compressed versions, making it easy to clean up RAW files afterwards.

## Usage

### Command-Line Arguments

- `--del`: Optional. Include this argument to activate the deletion of raw files without corresponding compressed images.
- `--path=<?>`: Specify the directory path to scan (default is the current working directory).
- `--rtype=<?>`: Define the file extension for raw files (default is `DNG`).
- `--ctype=<?>`: Define the file extension for compressed image files (default is `JPG`).

### Example Commands

**List unmatched raw files in working dir:**
  ```bash
  ./raw-diff.py
  ```


**List unmatched raw files in another directory:**
  ```bash
  ./raw-diff.py --path=/your/dir
  ```

**Delete unmatched raw files:**
  ```bash
  ./raw-diff.py --del
  ```

**Use different file types:**
  ```bash
  ./raw-diff.py --rtype=NEF --ctype=PNG
  ```