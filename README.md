### text2DNA
[seyitzor.work/text2DNA](www.seyitzor.work/text2DNA/)
> Your name, text, even credit card number...
> DNA encrypted.

"text2DNA" is a tool for converting texts to DNA sequences.

It is written in [Python](https://www.python.org/) as a Django application. So, it requires [Django](https://www.djangoproject.com/) to run. It's not in complete Django form here, only views and models files are included.

The encryption performed from utf-8 encoded text to binary to DNA with: "A for 00, T for 01, G for 11, C for 10"