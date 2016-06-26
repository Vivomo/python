from psd_tools import PSDImage
# from pymaging.image import LoadedImage
# with open('../src/test.psd') as psd:
#     print(dir(psd))

psd = PSDImage.load('../src/test.psd')
print(psd.header)
print(psd.layers)
png = psd.as_PIL()
png.save('../src/test.jpg')
