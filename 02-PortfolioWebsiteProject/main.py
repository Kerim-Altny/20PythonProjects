from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    all_projects = [
        {
            "title": "The Stochastic Dungeon",
            "subtitle": "C++ & Raylib Roguelike",
            "desc": "MST (Minimum Spanning Tree) ve Cellular Automata algoritmaları kullanılarak geliştirilmiş prosedürel zindan oluşturucu.",
            "tech": ["C++", "Raylib", "Algorithms"],
            "icon": "bi-controller",
            "link": "https://github.com/Kerim-Altny/TheStochasticDungeon"
        },
        {
            "title": "Advanced Tree Visualizer",
            "subtitle": "Data Structures Tool",
            "desc": "BST, AVL ve Red-Black Tree yapılarını interaktif olarak görselleştiren ve üzerinde işlem yapmaya olanak sağlayan web aracı.",
            "tech": ["JavaScript", "HTML/CSS", "VibeCoding"],
            "icon": "bi-diagram-3-fill",
            "link": "https://github.com/Kerim-Altny/advanced-tree-visualizer"
        },
        {
            "title": "Sorting Visualizer",
            "subtitle": "Algorithm Animation",
            "desc": "Bubble, Quick ve Merge Sort gibi algoritmaların çalışma mantığını animasyonlarla gösteren uygulama.",
            "tech": ["JavaScript", "VibeCoding"],
            "icon": "bi-bar-chart-line-fill",
            "link": "https://github.com/Kerim-Altny/sorting-visualizer"
        },
        {
            "title": "Unity Learning Path",
            "subtitle": "Game Development",
            "desc": "Tilemania, StarBlaster ve DeliveryDash gibi farklı mekaniklere sahip 2D ve 3D Unity oyun projeleri koleksiyonu.",
            "tech": ["C#", "Unity"],
            "icon": "bi-unity",
            "link": "https://github.com/Kerim-Altny/Unity-Learning-Path"
        },
        {
            "title": "Billboard to Spotify",
            "subtitle": "Python Automation",
            "desc": "Geçmiş tarihlerdeki Billboard listelerini otomatik olarak tarayıp kişisel Spotify çalma listelerine dönüştüren Python betiği.",
            "tech": ["Python", "Flask", "Spotify API"],
            "icon": "bi-music-note-beamed",
            "link": "https://github.com/Kerim-Altny/billboard-to-spotify"
        }
    ]
    return render_template("index.html", projects=all_projects)

if __name__ == "__main__":
    app.run(debug=True)