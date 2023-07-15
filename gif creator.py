import requests
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


def generate_gif(api_key, search_query, output_file):
    url = f"https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={search_query}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['meta']['status'] == 200:
            gif_url = data['data']['image_original_url']
            gif_response = requests.get(gif_url)

            with open(output_file, 'wb') as f:
                f.write(gif_response.content)

            print(f"GIF generated successfully and saved as '{output_file}'")
        else:
            print(f"Unable to generate GIF. API response: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {e}")
    except (KeyError, ValueError) as e:
        print(f"Invalid response format from API: {e}")


def generate_gif_with_gui():
    def browse_output_path():
        file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
        output_path_entry.delete(0, tk.END)
        output_path_entry.insert(0, file_path)

    def generate():

        api_key = "api key" #add the api key of Giphy here
        search_query = search_query_entry.get()
        output_file = output_path_entry.get()
        generate_gif(api_key, search_query, output_file)

    root = tk.Tk()
    root.title("GIF Generator")
    root.geometry("400x600")
    root.configure(bg='cyan')

    heading_label = tk.Label(root, text="GIF Generator", font=("Helvetica", 20, "bold"), pady=20,bg='cyan')
    heading_label.pack()

    search_query_label = tk.Label(root, text="Search Query:")
    search_query_label.pack(pady=10)
    search_query_entry = tk.Entry(root)
    search_query_entry.pack()

    output_path_label = tk.Label(root, text="Output Path:")
    output_path_label.pack(pady=10)
    output_path_entry = tk.Entry(root)
    output_path_entry.pack()
    browse_button = tk.Button(root, text="Browse", command=browse_output_path)
    browse_button.pack()

    generate_button = tk.Button(root, text="Generate GIF", command=generate)
    generate_button.pack(pady=20)

    root.mainloop()


# Launch the GIF generator GUI
generate_gif_with_gui()
