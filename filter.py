from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, image_size, gradation_step):
    for x in range(0, len(image), image_size):
        for y in range(0, len(image[0]), image_size):
            image[x:x + image_size, y:y + image_size] = get_average_brightness(
                image[x:x + image_size, y:y + image_size], image_size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open(input("Введите имя файла, которое хотите конвертировать: "))
    block_size = int(input("Введите размер блока: "))
    gradations_count = int(input("Введите количество градаций серого: "))
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    result = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    result.save(input("Введите имя файла, в которой хотите сохранить результат: "))


if __name__ == '__main__':
    main()
