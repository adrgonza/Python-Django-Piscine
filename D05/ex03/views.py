from django.shortcuts import render

def generate_shades(base_color):
    shades = []
    for i in range(51):
        factor = i / 50
        shade = [
            int(base_color[j] * factor + (255 - factor * 255)) for j in range(3)
        ]
        shades.insert(0 ,f'rgb({shade[0]}, {shade[1]}, {shade[2]})')
    return shades

def colortable(request):
    colors = {
        'noir': (0, 0, 0),
        'rouge': (255, 0, 0),
        'bleu': (0, 0, 255),
        'vert': (0, 255, 0),
    }
    shades = {color: generate_shades(rgb) for color, rgb in colors.items()}
    rows = []
    for i in range(51):
        rows.append({color: shades[color][i] for color in colors})

    return render(request, 'ex03_index.html', {'rows': rows})
