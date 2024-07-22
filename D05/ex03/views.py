from django.shortcuts import render

def generate_shades(color_name):
    """Generate a list of 50 shades for a given color."""
    shades = []
    for i in range(50):
        intensity = 100
        if color_name == 'black':
            color = f'rgb({intensity}, {intensity}, {intensity})'
        elif color_name == 'red':
            color = f'rgb({intensity}, 0, 0)'
        elif color_name == 'blue':
            color = f'rgb(0, 0, {intensity})'
        elif color_name == 'green':
            color = f'rgb(0, {intensity}, 0)'
        shades.append(color)
    return shades

def ex03_view(request):
    # Generate color shades for each column
    colors = ['black', 'red', 'blue', 'green']
    shades = {color: generate_shades(color) for color in colors}
    # Pass the shades and range to the template
    return render(request, 'ex03_index.html', {'shades': shades, 'range': range(50)})
