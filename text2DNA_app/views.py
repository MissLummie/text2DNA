from django.shortcuts import render

from django.conf import settings
import os
import time


def main_page(request):
    """
    for some reason the app urls isn't work, so I made this simple change to handle requests
    :param request:
    :return:
    """
    if request.POST.get('firstText'): return text_to_DNA(request)
    if request.POST.get('inDNA'): return DNA_to_text(request)
    return render(request, 'text2DNA.html')


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    # bits = bin(int(text.encode('hex'), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_to_DNA(request):
    firstText = "Hello?"
    if request.method == 'POST':
        firstText = request.POST['firstText']
    bits = text_to_bits(firstText)
    Doubles = []
    binaryDNA = {"00": "A", "01": "T", "11": "G", "10": "C"}
    for i in range(0, len(bits), 2):
        Doubles.append(bits[i:i + 2])
    seq = ""
    for double in Doubles:
        seq = seq + binaryDNA[double]
    f = open(os.path.join(settings.MEDIA_ROOT, 'log.txt'), 'a', encoding='utf-8')
    # t = firstText.decode('utf-8')
    f.write(time.strftime("%d/%m/%y %R") + ' ' + str(firstText) + '\n')
    f.close()
    print("seq:" ,seq)
    return render(request, 'text2DNA.html', {'seq': seq})


"""
def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]
"""


def DNA_to_text(request):
    inDNA = "TACATCTTTCGATCGATCGGAGGG"
    if request.method == 'POST':
        inDNA = request.POST['inDNA']
        if not inDNA:
            inDNA = "TACATCTTTCGATCGATCGGAGGG"
    inDNA = inDNA.upper()
    check = "ok"
    for letter in inDNA:
        if letter in '0123456789bdefhijklmnopqrsuvwxyzBDEFHIJKLMNOPQRSUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c':
            check = "not ok"
    if check == "ok":
        DNAbinary = {"A": "00", "T": "01", "G": "11", "C": "10"}
        bits = ""
        for i in range(0, len(inDNA)):
            bits = bits + DNAbinary[inDNA[i]]
        n = int(bits, 2)
        try:
            # results = to_bytes(n, (n.bit_length() + 7) // 8).decode("utf-8", "surrogatepass")
            results = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode("utf-8", "surrogatepass")
            return render(request, 'text2DNA.html', {'results': results})
        except:
            results = "This is a rare thing to do, your DNA is not suitable for conversion. Don't give up try one more time."
            return render(request, 'text2DNA.html', {'results': results})

    else:
        results = "Are you sure it's a DNA?"
        return render(request, 'text2DNA.html', {'results': results})