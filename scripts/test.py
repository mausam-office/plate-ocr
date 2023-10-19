import time
import easyocr
import cv2

# reader = easyocr.Reader(["hi","mr","ne", 'en'])
# reader = easyocr.Reader(["ne"])
reader = easyocr.Reader(["en"])

begin = time.perf_counter()

image_path = '../data/images/nbr_plate89.jpg'
image = cv2.imread(image_path)
scale = 3
resized_image = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

# start = time.perf_counter()
results = reader.readtext(resized_image)
text = ''
for result in results:
    # box = result[0]
    text += result[1] + ' '
# print(f"{text = }")
# print(f"duration1: {time.perf_counter()-start}")

duration = 0
iterations = 100
for _ in range(iterations):
    start = time.perf_counter()
    results = reader.readtext(resized_image)
    text = ''
    for result in results:
        # box = result[0]
        text += result[1] + ' '
    # print(f"{text = }")
    duration += time.perf_counter()-start

avg_duration = duration/iterations
print(f"avg duration: {avg_duration}, avg fps: {1/avg_duration}")

# print(type(results), results)
cv2.namedWindow('resized image', cv2.WINDOW_NORMAL)

cv2.imshow('resized image', image)
print(f"{time.perf_counter() - begin}")
cv2.waitKey(0)

