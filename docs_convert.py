"""
Converts the HTML docs to human-readable rST and places them in a rst folder
in the doc/package folders.

Depends on pandoc being installed. Pandoc is available in repositories.
"""

import click
import os
import pypandoc

# directory names to skip
blacklisted = [".git", "license", "csv" ]

@click.command()
@click.option('--to_format', default='rst')
def main(to_format):
    for root, dirnames, filenames in os.walk("./doc"):
        for dir_name in dirnames:
            if dir_name == to_format: # stay high level
                continue
            dest_dir = os.path.join(root, dir_name, to_format)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            html_files = os.listdir(os.path.join(root, dir_name))

            for f in html_files:
                filename, fileext = os.path.splitext(f)
                if fileext in ['.html', '.htm']:
                    print("Processing '%s' :: '%s'" % (dir_name, f))
                    if f == to_format:
                        continue
                    fin = os.path.join(root, dir_name, f)
                    fout = os.path.join(dest_dir, filename + '.' + to_format)
                    output = pypandoc.convert(fin, to_format, outputfile=fout)
                    assert output == ""

if __name__ == '__main__':
    main()
