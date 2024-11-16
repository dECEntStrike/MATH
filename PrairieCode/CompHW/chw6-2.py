import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(image, cmap='gray')

compressed = image.copy()



## Add your code here
def compress_chunk(chunk):
    c = create_dct_basis(chunk.shape[0])
    chunk_dct = np.transpose(c) @ chunk @ c
    chunk_dct[np.abs(chunk_dct) < 0.1*np.max(np.abs(chunk_dct))] = 0
    c_comp = c @ chunk_dct @ np.transpose(c)
    return np.clip(c_comp, 0, 255)

for u in range(0, image.shape[0], 8):
    for v in range(0, image.shape[1], 8):
        chnk = image[u:u+8, v:v+8].copy()
        compressed[u:u+8, v:v+8] = compress_chunk(chnk)

plt.figure()
plt.imshow(compressed, cmap='gray')