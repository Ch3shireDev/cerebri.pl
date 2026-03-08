window.MODULE_INDEX_DATA = {
    pageTitle: 'Informatyka - Cerebri.pl',
    moduleTitle: 'Informatyka',
    description: 'Zbiór testów sprawdzających wiedzę z informatyki. Poznaj algorytmy, struktury danych, sieci komputerowe i podstawy programowania. Wybierz dział, aby rozpocząć.',
    theme: {
        light: {
            'bg-primary': '#f4f6f9',
            'bg-secondary': '#ffffff',
            'text-primary': '#2c3e50',
            'text-secondary': '#666666',
            'accent-color': '#2980b9',
            'accent-hover': '#1f5fa6',
            'card-border': 'rgba(0,0,0,0.1)'
        },
        dark: {
            'bg-primary': '#1a1a1a',
            'bg-secondary': '#2d2d2d',
            'text-primary': '#ffffff',
            'text-secondary': '#b0b0b0',
            'accent-color': '#4a9fd8',
            'accent-hover': '#3a84c2',
            'card-border': 'rgba(255,255,255,0.1)'
        }
    },
    topics: [
        {
            title: 'Podstawy Informatyki',
            description: 'Architektura komputera, pamięć RAM, CPU, sieci, protokoły, bazy danych i systemy operacyjne.',
            route: 'informatics/basics',
            src: 'informatics/basics.html'
        },
        {
            title: 'Algorytmy i Struktury Danych',
            description: 'Sortowanie, wyszukiwanie, stosy, kolejki, drzewa binarne oraz złożoność obliczeniowa.',
            disabled: true,
            buttonLabel: 'Wkrótce'
        }
    ]
};