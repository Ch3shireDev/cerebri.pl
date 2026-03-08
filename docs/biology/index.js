window.MODULE_INDEX_DATA = {
    pageTitle: 'Biologia - Cerebri.pl',
    moduleTitle: 'Biologia',
    description: 'Zbiór testów sprawdzających wiedzę z biologii. Utrwal budowę komórek, ekologię, ochronę przyrody oraz anatomię człowieka. Wybierz dział, aby rozpocząć.',
    theme: {
        light: {
            'bg-primary': '#f4fbf7',
            'bg-secondary': '#ffffff',
            'text-primary': '#2c3e50',
            'text-secondary': '#666666',
            'accent-color': '#10ac84',
            'accent-hover': '#0d8a6a',
            'card-border': 'rgba(0,0,0,0.1)'
        },
        dark: {
            'bg-primary': '#111814',
            'bg-secondary': '#1e293b',
            'text-primary': '#e2e8f0',
            'text-secondary': '#b0b0b0',
            'accent-color': '#10ac84',
            'accent-hover': '#0d8a6a',
            'card-border': 'rgba(255,255,255,0.1)'
        }
    },
    topics: [
        {
            title: 'Podstawy Biologii',
            description: 'Budowa komórki, organizmy, tkanki i podstawowe procesy życiowe roślin i zwierząt.',
            route: 'biology/basics',
            src: 'biology/basics.html'
        },
        {
            title: 'Ekologia',
            description: 'Ekosystemy, łańcuchy pokarmowe, zależności między organizmami żywymi i środowiskiem.',
            route: 'biology/ecology',
            src: 'biology/ecology.html'
        },
        {
            title: 'Ochrona Przyrody w Polsce',
            description: 'Parki narodowe, rezerwaty, gatunki chronione oraz formy ochrony środowiska naturalnego w Polsce.',
            route: 'biology/nature-conservation',
            src: 'biology/nature-conservation.html'
        },
        {
            title: 'Ciało Człowieka',
            description: 'Układ pokarmowy, krwionośny, oddechowy i pozostałe systemy organizmu ludzkiego.',
            disabled: true,
            buttonLabel: 'Wkrótce'
        }
    ]
};