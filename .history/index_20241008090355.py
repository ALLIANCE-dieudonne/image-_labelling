import os
import cv2

# Path to the folder with images
IMG_DIR = "path/to/your/images/folder"
LABEL_DIR = "path/to/save/label/files"

# Predefined labels and bounding boxes (Replace this with actual object detection method if needed)
LABELS = [
    {
        "label": "object",
        "class_id": 0,
        "bbox": (50, 50, 150, 150),
    },  # (xmin, ymin, xmax, ymax)
]


def create_yolo_file(image_name, img_shape, labels, output_dir):
    height, width, _ = img_shape

    # Open the .txt file corresponding to the image
    txt_filename = os.path.join(
        output_dir, image_name.replace(".jpg", ".txt").replace(".png", ".txt")
    )
    with open(txt_filename, "w") as f:
        for label in labels:
            class_id = label["class_id"]
            xmin, ymin, xmax, ymax = label["bbox"]

            # Calculate YOLO format values
            x_center = ((xmin + xmax) / 2) / width
            y_center = ((ymin + ymax) / 2) / height
            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            # Write the YOLO format to file (class_id, x_center, y_center, width, height)
            f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


# Process each image in the folder
for img_file in os.listdir(IMG_DIR):
    if img_file.endswith(".jpg") or img_file.endswith(".png"):
        img_path = os.path.join(IMG_DIR, img_file)
        img = cv2.imread(img_path)
        img_shape = img.shape  # (height, width, depth)

        # Replace LABELS with actual bounding box detection logic (if needed)
        create_yolo_file(img_file, img_shape, LABELS, LABEL_DIR)

print("Labeling complete. YOLO format files saved in:", LABEL_DIR)
