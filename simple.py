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

    # ピクセルの値を0-255にクリップして、uint8型に変換
    result_img = Image.fromarray(np.clip(pixels, 0, 255).astype('uint8'))
    result_img.save(output_path)
    print(f"保存完了: {output_path}")

floyd_steinberg_dithering("./img/orig.png", "./img/simple.png")