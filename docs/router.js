/**
 * Cerebri.pl - Centralny Router
 * Zarządzanie nawigacją Hash-based dla całej aplikacji
 * * Obsługuje routing w formacie:
 * - /#!/<category> - strona główna kategorii (np. /#!/biology)
 * - /#!/<category>/<quiz-name> - konkretny quiz (np. /#!/biology/basics)
 */

(function(window) {
    'use strict';

    // ========================================
    // KONFIGURACJA MODUŁÓW I ROUTE'ÓW
    // ========================================
    
    const ROUTES = {
        'math': { 
            src: 'templates/index.html?module=math', 
            name: 'Matematyka' 
        },
        'math/linear-equations': { 
            src: 'math/linear-equations.html', 
            name: 'Równania liniowe' 
        },
        'biology': { 
            src: 'templates/index.html?module=biology', 
            name: 'Biologia' 
        },
        'biology/basics': { 
            src: 'biology/basics.html', 
            name: 'Podstawy Biologii' 
        },
        'biology/ecology': { 
            src: 'biology/ecology.html', 
            name: 'Ekologia' 
        },
        'biology/nature-conservation': { 
            src: 'biology/nature-conservation.html', 
            name: 'Ochrona Przyrody' 
        },
        'chemistry': { 
            src: 'templates/index.html?module=chemistry', 
            name: 'Chemia' 
        },
        'chemistry/hydroacids': { 
            src: 'chemistry/hydroacids.html', 
            name: 'Kwasy Beztlenowe' 
        },
        'chemistry/oxyacids': { 
            src: 'chemistry/oxyacids.html', 
            name: 'Kwasy Tlenowe' 
        },
        'chemistry/acids': { 
            src: 'chemistry/acids.html', 
            name: 'Kwasy' 
        },
        'chemistry/bases': { 
            src: 'chemistry/bases.html', 
            name: 'Zasady i Wodorotlenki' 
        },
        'chemistry/salts': { 
            src: 'chemistry/salts.html', 
            name: 'Sole' 
        },
        'informatics': { 
            src: 'templates/index.html?module=informatics', 
            name: 'Informatyka' 
        },
        'informatics/basics': { 
            src: 'informatics/basics.html', 
            name: 'Podstawy Informatyki' 
        },
        'physics': { 
            src: 'templates/index.html?module=physics', 
            name: 'Fizyka' 
        },
        'physics/uniform-motion': { 
            src: 'physics/uniform-motion.html', 
            name: 'Ruch jednostajny' 
        }
    };

    // ========================================
    // KLASA ROUTER
    // ========================================
    
    class CerebrRouter {
        constructor() {
            this.iframe = null;
            this.routes = ROUTES;
            this.initialized = false;
        }

        /**
         * Inicjalizacja routera - wiązanie z iframe
         * @param {HTMLIFrameElement} iframeElement - Element iframe do zarządzania
         */
        init(iframeElement) {
            if (this.initialized) {
                console.warn('Router już zainicjalizowany');
                return;
            }

            this.iframe = iframeElement;
            this.initialized = true;

            // Obsługa przycisku wstecz/naprzód w przeglądarce
            window.addEventListener('popstate', (e) => {
                if (e.state && e.state.route) {
                    this.navigate(e.state.route, false); // false = nie dodawaj do historii
                } else {
                    this.showWelcome();
                }
            });

            // Inicjalne załadowanie z URL
            this.initializeFromUrl();
        }

        /**
         * Pokazuje ekran powitalny bezpośrednio z elementu w index.html
         */
        showWelcome() {
            if (!this.iframe) return;
            
            // Wyczyść zawartość iframe'a
            this.iframe.removeAttribute('src');
            this.iframe.removeAttribute('srcdoc');
            
            // Przełącz widoczność kontenerów
            document.getElementById('iframe-wrapper').classList.add('d-none');
            document.getElementById('welcome-screen').classList.remove('d-none');
            
            // Zaktualizuj URL
            if (window.location.hash !== '#!/') {
                window.history.pushState(null, 'Cerebri.pl', '#!/');
            }
            
            // Odznacz wszystkie aktywne linki w menu
            this._clearActiveLinks();
        }

        /**
         * Nawigacja do określonej ścieżki
         * @param {string} routePath - Ścieżka routingu (np. 'biology' lub 'biology/basics')
         * @param {boolean} updateHistory - Czy dodać do historii przeglądarki (domyślnie: true)
         * @returns {boolean} - Czy nawigacja się powiodła
         */
        navigate(routePath, updateHistory = true) {
            const route = this.routes[routePath];
            
            if (!route) {
                console.error(`Nie znaleziono route'a: ${routePath}`);
                return false;
            }

            if (!this.iframe) {
                console.error('Router nie zainicjalizowany - brak iframe');
                return false;
            }

            // Przełącz widoczność - ukryj powitanie, pokaż iframe
            document.getElementById('welcome-screen').classList.add('d-none');
            document.getElementById('iframe-wrapper').classList.remove('d-none');

            // WAŻNE: Najpierw zaktualizuj URL, POTEM zmień iframe
            // To zapewnia, że URL jest zawsze zsynchronizowany z zawartością
            const newUrl = `#!/${routePath}`;
            if (updateHistory) {
                window.history.pushState({ route: routePath }, route.name, newUrl);
            } else {
                window.history.replaceState({ route: routePath }, route.name, newUrl);
            }

            // Oznacz aktywny link w menu (dla kategorii głównych)
            this._updateActiveLinks(routePath);

            // Załaduj zawartość w iframe
            this.iframe.removeAttribute('srcdoc');

            // Użyj absolutnego URL, aby uniknąć problemów z kontekstem ścieżek
            const absoluteSrc = new URL(route.src, window.location.href).href;
            this.iframe.src = absoluteSrc;

            return true;
        }

        /**
         * Nawigacja wstecz - skraca route hierarchicznie
         * Przykład: biology/basics -> biology -> ekran powitalny
         * @param {string|null} fromRoute - Opcjonalny route, z którego wracamy (jeśli null, używa aktualnego URL)
         * @returns {boolean} - Czy operacja się powiodła
         */
        navigateBack(fromRoute = null) {
            // Określ aktualny route
            const currentRoute = fromRoute || this.getCurrentRoute();
            
            if (!currentRoute) {
                // Jesteśmy już na stronie powitalnej
                return false;
            }

            // Sprawdź czy route ma hierarchię (zawiera /)
            const segments = currentRoute.split('/');
            
            if (segments.length > 1) {
                // Mamy route typu 'biology/basics' -> wróć do 'biology'
                const parentRoute = segments[0];
                return this.navigate(parentRoute);
            } else {
                // Mamy route typu 'biology' -> wróć do ekranu powitalnego
                this.showWelcome();
                return true;
            }
        }

        /**
         * Nawigacja do konkretnej kategorii (kompatybilność wsteczna)
         * @param {string} categoryRoute - Route kategorii (np. 'biology')
         * @param {string} categorySrc - Ścieżka do pliku kategorii (np. 'biology/index.html')
         */
        navigateToCategory(categoryRoute, categorySrc) {
            if (!this.iframe) return;

            // Przełącz widoczność - ukryj powitanie, pokaż iframe
            document.getElementById('welcome-screen').classList.add('d-none');
            document.getElementById('iframe-wrapper').classList.remove('d-none');

            const route = this.routes[categoryRoute];
            const routeName = route ? route.name : 'Powrót';

            // Zaktualizuj historię i URL
            window.history.pushState(
                { route: categoryRoute }, 
                routeName, 
                `#!/${categoryRoute}`
            );

            // Załaduj stronę kategorii
            this.iframe.src = categorySrc;

            // Oznacz aktywny link
            this._updateActiveLinks(categoryRoute);
        }

        /**
         * Inicjalizacja z URL przy pierwszym załadowaniu
         */
        initializeFromUrl() {
            const hash = window.location.hash;
            
            if (hash.startsWith('#!/')) {
                const routePath = hash.substring(3); // Wyciągnij ścieżkę z '#!/...'
                
                if (this.routes[routePath]) {
                    // Załaduj route bez dodawania do historii (replaceState)
                    this.navigate(routePath, false);
                    return;
                }
            }
            
            // Domyślnie: ekran powitalny
            this.showWelcome();
        }

        /**
         * Oznacza aktywny link w nawigacji
         * @param {string} routePath - Ścieżka routingu
         * @private
         */
        _updateActiveLinks(routePath) {
            // Czyść wszystkie aktywne linki
            this._clearActiveLinks();

            // Znajdź główną kategorię (np. 'biology' z 'biology/basics')
            const mainCategory = routePath.split('/')[0];

            // Linki w menu mają data-src w formie '<category>/index.html'
            const activeLink = document.querySelector(`[data-src^="${mainCategory}/"]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }

        /**
         * Usuwa oznaczenie aktywności ze wszystkich linków
         * @private
         */
        _clearActiveLinks() {
            document.querySelectorAll('.module-link').forEach(link => {
                link.classList.remove('active');
            });
        }

        /**
         * Zwraca informacje o danym route
         * @param {string} routePath - Ścieżka routingu
         * @returns {Object|null} - Obiekt route lub null
         */
        getRoute(routePath) {
            return this.routes[routePath] || null;
        }

        /**
         * Dodaje nowy route dynamicznie
         * @param {string} routePath - Ścieżka routingu
         * @param {string} src - Ścieżka do pliku HTML
         * @param {string} name - Nazwa route'a
         */
        addRoute(routePath, src, name) {
            this.routes[routePath] = { src, name };
        }

        /**
         * Pobiera aktualny route z URL (zawsze z parent window context)
         * @returns {string|null} - Aktualny route lub null jeśli jesteśmy na ekranie powitalnym
         */
        getCurrentRoute() {
            // Zawsze czytaj z window gdzie router jest zainicjalizowany (parent)
            const hash = window.location.hash;
            if (hash.startsWith('#!/')) {
                const route = hash.substring(3);
                return route || null;
            }
            return null;
        }
    }

    // ========================================
    // INICJALIZACJA I EKSPORT
    // ========================================
    
    // Utwórz globalną instancję routera
    const router = new CerebrRouter();

    // Eksportuj do window dla dostępu globalnego
    window.CerebrRouter = router;

    // API dla użycia w szabłonach (iframe contexts)
    window.CerebrRouterAPI = {
        /**
         * Nawigacja do route'a - użycie w szablonach
         * @param {string} route - Ścieżka routingu
         * @param {string} src - Ścieżka do pliku (opcjonalnie, dla kompatybilności)
         */
        navigate: function(route, src) {
            router.navigate(route);
        },

        /**
         * Nawigacja wstecz - użycie w quizach (skraca route hierarchicznie)
         * @param {string|null} fromRoute - Opcjonalny route, z którego wracamy
         */
        navigateBack: function(fromRoute = null) {
            if (!fromRoute) {
                const hash = window.location.hash;
                if (hash.startsWith('#!/')) {
                    fromRoute = hash.substring(3) || null;
                }
            }
            return router.navigateBack(fromRoute);
        },

        /**
         * Nawigacja do konkretnej kategorii (kompatybilność wsteczna)
         * @param {string} categoryRoute - Route kategorii
         * @param {string} categorySrc - Ścieżka do kategorii
         */
        navigateToCategory: function(categoryRoute, categorySrc) {
            router.navigateToCategory(categoryRoute, categorySrc);
        },

        /**
         * Zwraca aktualny route z URL parent window
         */
        getCurrentRoute: function() {
            const hash = window.location.hash;
            if (hash.startsWith('#!/')) {
                const route = hash.substring(3);
                return route || null;
            }
            return null;
        }
    };

    // Obsługa kompatybilności wstecznej - ekspozycja loadContent jako alias
    window.loadContent = function(routePath) {
        return router.navigate(routePath);
    };

})(window);