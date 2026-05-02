import pandas as pd
import folium
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import time
from PIL import Image, ImageTk

#-------------------------------
# READ CSV FILE
#-------------------------------
df=pd.read_csv("india_historical_places.csv")

#-------------------------------
# DISPLAY ALL DATA
#-------------------------------

def display_all():
    print("\n====== ALL HISTORICAL PLACES IN INDIA ======\n")
    print(df)

#-------------------------------
# STATEWISE COUNT GRAPH
#-------------------------------
def statewise_graph():
    state_count = df['State'].value_counts()
    plt.figure(figsize=(10,5))
    state_count.plot(kind='bar')
    plt.title('Statewise Historical Places Count')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("statewise_graph.png")
    plt.show()

#-------------------------------
# DYNASTY PIE CHART
#-------------------------------
def dynasty_graph():
    dynasty_count = df['Dynasty'].value_counts()
    plt.figure(figsize=(8,8))
    dynasty_count.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Dynasty Distribution')
    plt.ylabel('')
    plt.savefig("dynasty_graph.png")
    plt.show()

#-------------------------------
# TOP 10 OLDEST PLACES
#-------------------------------
def oldest_places_graph():
    oldest=df.sort_values('YearBuilt').head(10)
    plt.figure(figsize=(12,5))
    plt.bar(oldest['Place'], oldest['YearBuilt'])
    plt.title('Top 10 Oldest Historical Places')
    plt.xlabel('Historical Place')
    plt.ylabel('Year Built')
    plt.xticks(rotation=75)
    plt.tight_layout()
    plt.savefig("oldest10_graph.png")
    plt.show()

#------------------------------
# RESULT WINDOW
#------------------------------
def show_result_window(title, data):
    result_window = tk.Toplevel(root)
    result_window.title(title)
    result_window.geometry("1200x400")
    result_window.configure(bg="#f5f5f5")

    columns = list(data.columns)

    tree = ttk.Treeview(result_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=140, anchor='center')

    for index, row in data.iterrows():
        tree.insert("", tk.END, values=list(row))

    tree.pack(expand=True, fill='both', pady=20)

    scrollbar = ttk.Scrollbar(result_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

#-------------------------------
# SEARCH BY STATE
#-------------------------------
def search_state():
    state = entry_state.get().strip()

    if state == "":
        messagebox.showwarning("Input Error", "Please enter a state name")
        return

    result = df[df["State"].str.lower() == state.lower()]

    if result.empty:
        messagebox.showinfo("Search Result", "No historical places found")
    else:
        show_result_window("State Search Result", result)

#-------------------------------
# SEARCH BY DYNASTY
#-------------------------------
def search_dynasty():
    dynasty = entry_dynasty.get().strip()

    if dynasty == "":
        messagebox.showwarning("Input Error", "Please enter a dynasty name")
        return

    result = df[df["Dynasty"].str.lower() == dynasty.lower()]

    if result.empty:
        messagebox.showinfo("Search Result", "No monuments found")
    else:
        show_result_window("Dynasty Search Result", result)

#-------------------------------
# CREATE COLORFUL INDIA MAP
#-------------------------------
def create_map():
    india_map = folium.Map(location=[22.9734, 78.6569], zoom_start=5)

    marker_colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'cadetblue', 'darkgreen']

    for i, row in df.iterrows():
        popup_text = f'''
        <b>{row['Place']}</b><br>
        {row['Description']}<br>
        State: {row['State']}<br>
        City: {row['City']}<br>
        Built: {row['YearBuilt']}<br>
        Dynasty: {row['Dynasty']}<br>
        '''

        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=popup_text,
            icon=folium.Icon(color=marker_colors[i % len(marker_colors)], icon="glyphicon-tower")
        ).add_to(india_map)

    india_map.save("india_historical_map.html")
    webbrowser.open("india_historical_map.html")
    messagebox.showinfo("Map", "India Historical Map Created Successfully!")


#-------------------------------
# MENU DRIVEN CONSOLE
#-------------------------------
def display_all_window():
    all_window = tk.Toplevel(root)
    all_window.title("All Historical Places Data")
    all_window.geometry("1250x500")
    all_window.configure(bg="#f4f6f7")

    columns = list(df.columns)

    tree = ttk.Treeview(all_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=140, anchor='center')

    for index, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))

    tree.pack(expand=True, fill='both', pady=20)

    scrollbar = ttk.Scrollbar(all_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')


def open_menu_window():
    menu_window = tk.Toplevel(root)
    menu_window.title("Historical India Control Panel")
    menu_window.geometry("420x520")
    menu_window.configure(bg="#dfe6e9")

    panel_style = {
        "font": ("Arial", 11, "bold"),
        "width": 28,
        "bg": "#2c3e50",
        "fg": "white",
        "bd": 2
    }

    tk.Label(
        menu_window,
        text="HISTORICAL INDIA MENU",
        font=("Georgia",20,"bold"),
        bg="#dfe6e9",
        fg="#1b1464"
    ).pack(pady=25)

    tk.Button(menu_window, text="Display All Historical Places", command=display_all_window, **panel_style).pack(pady=10)
    tk.Button(menu_window, text="Monument Distribution by State", command=statewise_graph, **panel_style).pack(pady=10)
    tk.Button(menu_window, text="Dynasty Analysis", command=dynasty_graph, **panel_style).pack(pady=10)
    tk.Button(menu_window, text="Ancient Heritage Timeline", command=oldest_places_graph, **panel_style).pack(pady=10)
    tk.Button(menu_window, text="Create Interactive India Map", command=create_map, **panel_style).pack(pady=10)
    tk.Button(menu_window, text="Exit Control Panel", command=menu_window.destroy, **panel_style).pack(pady=20)

#------------------------------
# STATISTICS
#------------------------------
def project_statistics():
    total_places = len(df)
    oldest_place = df.loc[df["YearBuilt"].idxmin(), "Place"]
    top_state = df["State"].value_counts().idxmax()

    stats_text = f"Total Historical Places: {total_places}    |    Oldest Monument: {oldest_place}    |    Most Represented State: {top_state}"
    return stats_text

#-------------------------------
# CLOCK UPDATE
#------------------------------
def update_clock():
    current_time = time.strftime("%d-%m-%Y   %H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

#------------------------------
# IMAGE
#-------------------------------
def get_monument_image(place):
    image_files = {
        "Taj Mahal": "tajmahal.jpg",
        "Red Fort": "redfort.jpg",
        "Konark Sun Temple": "konark.jpg",
        "Qutub Minar": "qutubminar.jpg",
        "Hampi": "hampi.jpg"
    }
    return image_files.get(place, None)

#-------------------------------
# TKINTER GUI WINDOW
#-------------------------------
root = tk.Tk()
root.title("Historical Places of India Project")
root.state('zoomed')
root.minsize(1000, 700)
root.configure(bg="#e8f0fe")

#--------------- INDIAN FLAG BORDER-------------
top_flag = tk.Frame(root, bg="orange", height=8)
top_flag.pack(fill='x')

mid_flag = tk.Frame(root, bg="white", height=8)
mid_flag.pack(fill='x')

bottom_flag = tk.Frame(root, bg="green", height=8)
bottom_flag.pack(fill='x')

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="HISTORICAL PLACES OF INDIA LOCATOR",
    font=("Georgia",22,"bold"),
    bg="#e8f0fe",
    fg="#1a237e"
)
title.pack(pady=20)

tagline = tk.Label(
    root,
    text="Explore India's Rich Historical Heritage",
    font=("Arial",12,"italic"),
    bg="#e8f0fe",
    fg="#37474f"
)
tagline.pack(pady=5)

#---------------STATS------------------
stats = tk.Label(
    root,
    text=project_statistics(),
    font=("Arial",11,"bold"),
    bg="#e8f0fe",
    fg="#00695c"
)
stats.pack(pady=10)

#---------------- CLOCK LABEL------------------
clock_label = tk.Label(root, font=("Arial",11,"bold"), bg="#e8f0fe", fg="#880e4f")
clock_label.pack(pady=5)
update_clock()

# ---------------- BUTTON STYLE ----------------
button_style = {
    "font": ("Arial", 11, "bold"),
    "width": 25,
    "bg": "#3949ab",
    "fg": "white",
    "bd": 2
}

# ---------------- MAIN FRAMES ----------------
main_frame = tk.Frame(root, bg="#e8f0fe")
main_frame.pack(pady=30)

left_frame = tk.Frame(main_frame, bg="#d6e4ff", bd=3, relief="ridge")
left_frame.grid(row=0, column=0, padx=40)

right_frame = tk.Frame(main_frame, bg="#d6e4ff", bd=3, relief="ridge")
right_frame.grid(row=0, column=1, padx=40)

# ---------------- LEFT FRAME SEARCH SECTION ----------------
tk.Label(left_frame, text="SEARCH SECTION", font=("Arial",15,"bold"),
         bg="#d6e4ff", fg="#0d47a1").pack(pady=15)

tk.Label(left_frame, text="Enter State Name", font=("Arial",12,"bold"),
         bg="#d6e4ff").pack(pady=5)

entry_state = tk.Entry(left_frame, width=28, font=("Arial",12), bd=3)
entry_state.pack(pady=5)

btn_state = tk.Button(left_frame, text="Search by State", command=search_state, **button_style)
btn_state.pack(pady=10)

tk.Label(left_frame, text="Enter Dynasty Name", font=("Arial",12,"bold"),
         bg="#d6e4ff").pack(pady=5)

entry_dynasty = tk.Entry(left_frame, width=28, font=("Arial",12), bd=3)
entry_dynasty.pack(pady=5)

btn_dynasty = tk.Button(left_frame, text="Search by Dynasty", command=search_dynasty, **button_style)
btn_dynasty.pack(pady=10)

# ---------------- RIGHT FRAME ANALYSIS SECTION ----------------
tk.Label(right_frame, text="ANALYSIS TOOLS", font=("Arial",15,"bold"),
         bg="#d6e4ff", fg="#0d47a1").pack(pady=15)

btn_map = tk.Button(right_frame, text="Create Interactive India Map", command=create_map, **button_style)
btn_map.pack(pady=10)

btn_graph1 = tk.Button(right_frame, text="Monument Distribution by State", command=statewise_graph, **button_style)
btn_graph1.pack(pady=10)

btn_graph2 = tk.Button(right_frame, text="Dynasty Analysis", command=dynasty_graph, **button_style)
btn_graph2.pack(pady=10)

btn_graph3 = tk.Button(right_frame, text="Ancient Heritage Timeline", command=oldest_places_graph, **button_style)
btn_graph3.pack(pady=10)

btn_console = tk.Button(right_frame, text="Open Control Panel Menu", command=open_menu_window, **button_style)
btn_console.pack(pady=10)

# ---------------- EXIT BUTTON ----------------
btn_exit = tk.Button(root, text="Exit Application", width=25,
                     font=("Arial",11,"bold"),
                     bg="#b71c1c", fg="white",
                     command=root.destroy)
btn_exit.pack(pady=20)

root.mainloop()

