window.MODULE_INDEX_DATA = {
    pageTitle: 'Matematyka - Cerebri.pl',
    moduleTitle: 'Matematyka',
    description: 'Zbiór testów sprawdzających wiedzę z matematyki. Rozwiązuj równania, trenuj logiczne myślenie i utrwalaj wzory. Wybierz dział, aby rozpocząć.',
    theme: {
        light: {
            'bg-primary': '#fdf5f6',
            'bg-secondary': '#ffffff',
            'text-primary': '#2c3e50',
            'text-secondary': '#666666',
            'accent-color': '#e84393',
            'accent-hover': '#d81b60',
            'card-border': 'rgba(0,0,0,0.1)'
        },
        dark: {
            'bg-primary': '#1a1a1a',
            'bg-secondary': '#2d2d2d',
            'text-primary': '#ffffff',
            'text-secondary': '#b0b0b0',
            'accent-color': '#cc5555',
            'accent-hover': '#b34444',
            'card-border': 'rgba(255,255,255,0.1)'
        }
    },
    topics: [
        {
            title: 'Trening: Równania liniowe',
            description: 'Nieskończony automat generujący równania z jedną niewiadomą (ax + b = c). Trenuj bez końca, utrzymuj serię i podbijaj mnożnik punktowy.',
            route: 'math/linear-equations',
            src: 'math/linear-equations.html'
        },
        {
            title: 'Egzamin Ósmoklasisty 2025',
            description: 'Zadania z matematyki przygotowujące do egzaminu ósmoklasisty 2025.',
            route: 'math/egzamin-2025',
            src: 'math/egzamin-2025.html'
        },
        {
            title: 'Ułamki i Procenty',
            description: 'Obliczanie ułamków zwykłych, dziesiętnych oraz procentów w zadaniach praktycznych.',
            disabled: true,
            buttonLabel: 'Wkrótce'
        },
    ]
};