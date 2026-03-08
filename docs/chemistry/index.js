window.MODULE_INDEX_DATA = {
    pageTitle: 'Chemia - Cerebri.pl',
    moduleTitle: 'Chemia',
    description: 'Zbiór testów sprawdzających wiedzę z chemii nieorganicznej. Utrwal budowę, właściwości i reakcje związków chemicznych. Wybierz dział, aby rozpocząć.',
    theme: {
        light: {
            'bg-primary': '#f0fcfd',
            'bg-secondary': '#ffffff',
            'text-primary': '#2c3e50',
            'text-secondary': '#666666',
            'accent-color': '#0abde3',
            'accent-hover': '#0899cc',
            'card-border': 'rgba(0,0,0,0.1)'
        },
        dark: {
            'bg-primary': '#1a1a1a',
            'bg-secondary': '#2d2d2d',
            'text-primary': '#ffffff',
            'text-secondary': '#b0b0b0',
            'accent-color': '#2db8e6',
            'accent-hover': '#26a0d1',
            'card-border': 'rgba(255,255,255,0.1)'
        }
    },
    topics: [
        {
            title: 'Kwasy Beztlenowe',
            description: 'Budowa, nazewnictwo i właściwości kwasów nieposiadających atomów tlenu (np. HCl, H₂S).',
            route: 'chemistry/hydroacids',
            src: 'chemistry/hydroacids.html'
        },
        {
            title: 'Kwasy Tlenowe',
            description: 'Struktura, otrzymywanie i dysocjacja kwasów zawierających tlen w reszcie kwasowej (np. H₂SO₄, HNO₃).',
            route: 'chemistry/oxyacids',
            src: 'chemistry/oxyacids.html'
        },
        {
            title: 'Kwasy (Test zbiorczy)',
            description: 'Kompleksowy przegląd wiedzy o wszystkich rodzajach kwasów, ich reakcjach i teoriach.',
            route: 'chemistry/acids',
            src: 'chemistry/acids.html'
        },
        {
            title: 'Zasady i Wodorotlenki',
            description: 'Budowa, właściwości żrące, wskaźniki pH oraz dysocjacja jonowa zasad i wodorotlenków.',
            route: 'chemistry/bases',
            src: 'chemistry/bases.html'
        },
        {
            title: 'Sole',
            description: 'Klasyfikacja, dysocjacja, reakcje strąceniowe, nazewnictwo i wzory sumaryczne soli.',
            route: 'chemistry/salts',
            src: 'chemistry/salts.html'
        }
    ]
};