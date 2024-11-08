# Background Removal and Replacement App

This application provides functionality to remove the background from an image and replace it with a solid color or another image. It uses the `rembg` library for background removal and the `PIL` (Pillow) library for image processing.

## Features

- **Remove Background**: Remove the background from an image using the `remove_bg` function.
- **Add Background Color**: Replace the background of an image with a solid color using the `add_bg_color` function.
- **Add Background Image**: Replace the background of an image with another image using the `add_bg_image` function.

## Requirements

- Python 3.x
- Streamlit
- Pillow
- rembg

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the app.

## Functions

### `remove_bg(image)`

Removes the background from the given image.

- **Parameters**: 
  - `image` (PIL.Image): The input image from which the background will be removed.
- **Returns**: 
  - `PIL.Image`: The image with the background removed.

### `add_bg_color(foreground, color)`

Adds a solid color background to the given foreground image.

- **Parameters**: 
  - `foreground` (PIL.Image): The foreground image.
  - `color` (tuple): The color to be used for the background (e.g., `(255, 255, 255, 255)` for white).
- **Returns**: 
  - `PIL.Image`: The combined image with the new background color.

### `add_bg_image(foreground, background)`

Adds a background image to the given foreground image.

- **Parameters**: 
  - `foreground` (PIL.Image): The foreground image.
  - `background` (PIL.Image): The background image.
- **Returns**: 
  - `PIL.Image`: The combined image with the new background image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Maintainer

This repository is maintained by [Anurag Singh](https://github.com/anurag-singh-9622/). You can connect with me on [LinkedIn](https://www.linkedin.com/in/anurag-singh9622/).