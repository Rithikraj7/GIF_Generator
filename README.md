# GIF_Generator

This program allows you to generate a GIF using the GIPHY API. You can specify the search query, API key, and output path to generate and save a GIF file.

![Example Snapshot]()

## Prerequisites

- Python 3 installed on your system
- Required Python packages: `requests`, `tkinter`, `Pillow`

## Getting Started

1. Clone the repository or download the source code.

2. Install the required packages using pip:

    ```bash
    pip install requests tkinter Pillow
    ```

3. Obtain a GIPHY API key by signing up at [https://developers.giphy.com/](https://developers.giphy.com/).

4. Open the `generate_gif.py` file and replace `'YOUR_API_KEY'` with your GIPHY API key.

5. Run the script:

    ```bash
    python generate_gif.py
    ```

6. The GIF Generator GUI will open. Enter the search query, choose the output path for the generated GIF, and click on the "Generate GIF" button.

7. The program will retrieve a random GIF from GIPHY based on your search query and save it to the specified output path.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This program uses the GIPHY API to generate GIFs. Visit [https://developers.giphy.com/](https://developers.giphy.com/) for more information.
- The program utilizes the `requests`, `tkinter`, and `Pillow` libraries. Visit their respective documentation for more details.
