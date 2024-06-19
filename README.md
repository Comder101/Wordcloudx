# Wordcloudx
A program that creates a visual representation of the most common words within the text data. Technologies used : Matplotlib, Numpy.
## Installation

If you are using pip:

    pip install wordcloud

If you are using conda, you can install from the `conda-forge` channel:

    conda install -c conda-forge wordcloud
#### Installation notes

wordcloud depends on `numpy`, `pillow`, and `matplotlib`.

If there are no wheels available for your version of python, installing the
package requires having a C compiler set up. Before installing a compiler, report
an issue describing the version of python and operating system being used.

![wordcloudfinal](https://github.com/Comder101/Wordcloudx/assets/86362195/a4dadb06-d129-4fd1-b844-a2f55fea5dcc)

## Command-line usage

The `wordcloud_cli` tool can be used to generate word clouds directly from the command-line:

	$ wordcloud_cli --text mytext.txt --imagefile wordcloud.png

If you're dealing with PDF files, then `pdftotext`, included by default with many Linux distribution, comes in handy:

	$ pdftotext mydocument.pdf - | wordcloud_cli --imagefile wordcloud.png

In the previous example, the `-` argument orders `pdftotext` to write the resulting text to stdout, which is then piped to the stdin of `wordcloud_cli.py`.

Use `wordcloud_cli --help` so see all available options.


