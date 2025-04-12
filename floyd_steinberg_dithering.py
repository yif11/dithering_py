from PIL import Image
import numpy as np

def floyd_steinberg_dithering(input_path: str, output_path: str):
    # グレースケールとして読み込み
    img = Image.open(input_path).convert("L")
    pixels = np.array(img, dtype=float)

    height, width = pixels.shape

    for y in range(height):
        for x in range(width):
            old_pixel = pixels[y, x]
            new_pixel = 0 if old_pixel < 128 else 255
            pixels[y, x] = new_pixel
            quant_error = old_pixel - new_pixel

            # Floyd-Steinberg
            if x + 1 < width:
                pixels[y, x + 1] += quant_error * 7 / 16
            if x - 1 >= 0 and y + 1 < height:
                pixels[y + 1, x - 1] += quant_error * 3 / 16
            if y + 1 < height:
                pixels[y + 1, x] += quant_error * 5 / 16
            if x + 1 < width and y + 1 < height:
                pixels[y + 1, x + 1] += quant_error * 1 / 16

    # ピクセルの値を0-255にクリップして、uint8型に変換
    result_img = Image.fromarray(np.clip(pixels, 0, 255).astype('uint8'))
    result_img.save(output_path)
    print(f"保存完了: {output_path}")

floyd_steinberg_dithering("./img/img.png", "./img/0.png")