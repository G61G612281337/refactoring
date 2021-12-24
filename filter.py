from PIL import Image
import numpy as np
np.seterr(over='ignore')

def transform_to_mosaic(n, m, arr, size, step):
    average_brightness = np.mean(arr[n:n+size, m:m+size][:])
    arr[n:n+size, m:m+size][:] = int(average_brightness // step) * step

open_name = input('Введите назвние изображения : ')
save_name = input('Введите назвние выходного изображения : ')

arr = np.array(Image.open(open_name))
	@@ -35,6 +20,6 @@ def transform_to_mosaic(n_idx, m_idx, arr, size, step, average_brightness):
for n in range(0, width - size + 1, size):
    for m in range(0, height - size + 1, size):
        transform_to_mosaic(n, m, arr, size, step)
res = Image.fromarray(arr)
res.save(save_name)
