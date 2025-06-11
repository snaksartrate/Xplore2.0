# White base image
white_img = 255 * np.ones((300, 250, 3), dtype=np.uint8)

# The background and base of house
cv.rectangle(white_img, (0,0), (300,300), [180, 225, 245], -1)
cv.rectangle(white_img, (0,295), (295,300), [124, 252, 0], -1)
cv.rectangle(white_img, (50,300), (200,200), [220, 100, 220], -1)

# The ☀ Sun
cv.circle(white_img, (200,50), 30, [240, 240, 50], -1)

# Draw the triangle outline
cv.line(white_img, (125,100), (200,200), [100, 100, 150], 10)
cv.line(white_img, (50,200), (125,100), [100, 100, 150], 10)

# Define triangle points as a NumPy array
pts = np.array([[50, 200], [125, 100], [200, 200]], dtype=np.int32)
pts = pts.reshape((-1, 1, 2))

# Fill the triangle with black
cv.fillPoly(white_img, [pts], color=(100, 100, 150))

# Draw windows and door with a handle
cv.rectangle(white_img, (75,250), (100,225), [230, 162, 250], -1)
cv.rectangle(white_img, (150,250), (175,225), [230, 162, 250], -1)
cv.rectangle(white_img, (110,300), (140,250), [255, 200, 255], -1)
cv.rectangle(white_img, (111,278), (117,280), [200, 100, 250], -1)

# Add text to the image
cv.putText(white_img, "My House", (60,190), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, [255, 255, 255], 2)

# Display Image
cv2_imshow(white_img)
cv.waitKey(0)
cv.destroyAllWindows()