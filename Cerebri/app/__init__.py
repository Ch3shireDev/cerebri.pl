"""
Package for the application.
"""
from enum import Enum, auto


class AnswerType(Enum):
    Closed = auto()
    ManyValues = auto()
    Proof = auto()
    ListOfValues = auto()
    Intervals = auto()


webpage_dict = {str(AnswerType.Closed): './app/exercises/closed.html',
                str(AnswerType.ManyValues): './app/exercises/many_values.html',
                str(AnswerType.Proof): './app/exercises/proof.html',
                str(AnswerType.ListOfValues): './app/exercises/list_of_values.html',
                str(AnswerType.Intervals): './app/exercises/intervals.html',
                }


class Exercise:
    def __init__(self, title, content, answers={}, answer_type=AnswerType.Closed, points=1, previous=None, next=None):
        self.title = title
        self.content = content
        self.answers = answers
        self.answer_type = answer_type
        self.points = points
        self.previous = previous
        self.next = next


Exercises = {
    '1': Exercise(
        'Zadanie 1',
        'Liczba \(\log_{\sqrt 2}2\) jest równa',
        {
            'answers':{
            'A': '2',
         'B': '4',
         'C': '\(\sqrt2\)',
         'D': r'\(\frac12\)',},
         'correct': 'A'},
        answer_type=AnswerType.Closed,
        points=1,
        next='2'
    ),

    '2': Exercise(
        'Zadanie 2', 
        'Liczba naturalna \(n = 2^{14}\cdot5^{15}\) w zapisie dziesiętnym ma',
        {
            'answers':{
            'A': '14 cyfr',
         'B': '15 cyfr',
         'C': '16 cyfr',
         'D': '30 cyfr',},
         'correct': 'B'},
        answer_type=AnswerType.Closed,
        points=1,
        next='3',
        previous='1',
    ),

    '3': Exercise(
        'Zadanie 3',
       '''W pewnym banku prowizja od udzielanych kredytów hipotecznych przez cały
                    styczeń była równa \(4\%\). Na początku lutego bank obniżył wysokość prowizji
                    od wszelkich kredytów o 1 punkt procentowy. Oznacza to, że prowizja od kredytów
                    hipotecznych zmniejszyła się o''',
        {
            'answers':{
            'A': '\(1\%\)',
         'B': '\(25\%\)',
         'C': '\(33\%\)',
         'D': '\(75\%\)',},
         'correct': 'B'}, 
         answer_type=AnswerType.Closed,
        points=1,
        next='4',
        previous='2',
    ),

    '4': Exercise(
        'Zadanie 4', 
        r'Równość \(\frac14+\frac15+\frac1a=1\) jest prawdziwa dla:',
        {
            'answers':{
            'A': r'\(a=\frac{11}{20}\)',
            'B': r'\(a=\frac{8}{9}\)',
            'C': r'\(a=\frac{9}{8}\)',
            'D': r'\(a=\frac{20}{11}\)',},
            'correct': 'D', }, answer_type=AnswerType.Closed,
        points=1,
        next='5',
        previous='3',
    ),

    '5': Exercise(
        'Zadanie 5', 
        r'''Para liczb \(x=2\) i \(y=2\) jest rozwiązaniem układu równań $$
\begin{split}ax+y &= 4\\-2x+3y&=2a\end{split}$$ dla:''',
        {
            'answers':{
            'A': r'\(a=-1\)',
            'B': r'\(a=1\)',
            'C': r'\(a=-2\)',
            'D': r'\(a=2\)',},
            'correct': 'B'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='6',
        previous='4',
    ),

    '6': Exercise(
        'Zadanie 6', 
        r'Równanie \(\frac{(x-1)(x+2)}{x-3}=0\) ma rozwiązania:',
        {
            'answers':{
            'A': '\(x=1, x=3, x=-2\)',
            'B': '\(x=-1, x=-3, x=2\)',
            'C': '\(x=1, x=-2\)',
            'D': '\(x=-1, x=2\)',},
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='7',
        previous='5',
    ),

    '7': Exercise(
        'Zadanie 7', 
        r'Miejscem zerowym funkcji liniowej \(f\) określonej wzorem \(f(x) = 3(x+1)-6\sqrt3\) jest liczba:',
        {
            'answers':{
            'A': '\(3-6\sqrt3\)',
            'B': '\(1-6\sqrt3\)',
            'C': '\(2\sqrt3-1\)',
            'D': r'\(2\sqrt3-\frac13\)',},
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='8',
        previous='6',
    ),

    '8': Exercise(
        'Zadanie 8', 
        '''<p>Na rysunku przedstawiony jest fragment paraboli będącej wykresem funkcji kwadratowej \(f\). Wierzchołkiem tej paraboli jest punkt $W=(2,-4)$. Liczby 0 i 4 to miejsca zerowe funkcji $f$.</p>
    <p><img src="https://i.imgur.com/4SnQkD6.png" class="mx-auto d-block"/></p>
    <p>Zbiorem wartości funkcji $f$ jest przedział:</p>''',
        {
            'answers':{
            'A': r'$(-\infty,0\rangle$',
            'B': r'$\langle0,4\rangle$',
            'C': r'$\langle-4,+\infty)$',
            'D': r'$\langle-4,+\infty\rangle$',},
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='9',
        previous='7',

    ),

    '9': Exercise(
        'Zadanie 9', 
        r'''<p><img src="https://i.imgur.com/4SnQkD6.png" class="mx-auto d-block"/></p>
    <p>Największa wartość funkcji $f$ w przedziale $\langle1,4\rangle$ jest równa:</p>''',
        {
            'answers':{
            'A': '-3',
            'B': '-4',
            'C': '4',
            'D': '0',},
            'correct': 'D'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='10',
        previous='8',
    ),

    '10': Exercise(
        'Zadanie 10', 
        r'''<p><img src="https://i.imgur.com/4SnQkD6.png" class="mx-auto d-block"/></p>
    <p>Osią symetrii wykresu funkcji $f$ jest prosta o równaniu:</p>''',
        {
            'answers':{
            'A': 'y=-4',
            'B': 'x=-4',
            'C': 'y=2',
            'D': 'x=2',},
            'correct': 'D'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='11',
        previous='9',
    ),
    '11': Exercise(
        'Zadanie 11',
        'W ciągu arytmetycznym $(a_n)$, określonym dla $n\geq1$, dane są dwa wyrazy: $a_1 = 7$ i $a_8=-49$. Suma ośmiu początkowych wyrazów tego ciągu jest równa:',
        {
            'answers':{
            'A': '-168',
            'B': '-189',
            'C': '-21',
            'D': '-42',},
            'correct': 'A'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='12',
        previous='10',
    ),

    '12': Exercise(
        'Zadanie 12',
        r'Dany jest ciąg geometryczny $(a_n)$, określony dla $n\geq1$. Wszystkie wyrazy tego ciągu są dodatnie i spełniony jest warunek $\frac{a_5}{a_3}=\frac19$. Iloraz tego ciągu jest równy:',
        {
            'answers':{
            'A': r'$\frac13$',
            'B': r'$\frac1{\sqrt3}$',
            'C': r'$3$',
            'D': r'$\sqrt3$',},
            'correct': 'A'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='13',
        previous='11',
    ),

    '13': Exercise(
        'Zadanie 13',

        r'Sinus kąta ostrego $\alpha$ jest równy $\frac45$. Wtedy:',
        {
            'answers':{
            'A': r'$\cos\alpha=\frac54$',
            'B': r'$\cos\alpha=\frac15$',
            'C': r'$\cos\alpha=\frac9{25}$',
            'D': r'$\cos\alpha=\frac35$',},
            'correct': 'D'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='14',
        previous='12',
    ),

    '14': Exercise(

        'Zadanie 14',
        r'''<p>Punkty $D$ i $E$ leżą na okręgu opisanym na trójkącie równobocznym $ABC$ (zobacz rysunek). Odcinek $CD$ jest średnicą tego okręgu. Kąt wpisany $DEB$ ma miarę $\alpha$.</p>
    <p><img src="https://i.imgur.com/k9vOgEY.png" class="mx-auto d-block"/></p>
    <p>Zatem:</p>''',
        {
            'answers':{
            'A': r'$\alpha=30^\circ$',
            'B': r'$\alpha<30^\circ$',
            'C': r'$\alpha>45^\circ$',
            'D': r'$\alpha=45^\circ$',
            },
            'correct': 'A'
        }, 
        answer_type=AnswerType.Closed,
        points=1,
        next='15',
        previous='13',
    ),

    '15': Exercise(
        'Zadanie 15', r'''
    <p>Dane są dwa okręgi: okrąg o środku w punkcie $O$ i promieniu 5 oraz okrąg o środku w punkcie $P$ i promieniu 3. Odcinek $OP$ ma długość 16. Prosta $AB$ jest styczna do tych okręgów w punktach $A$ i $B$. Ponadto prosta $AB$ przecina odcinek $OP$ w punkcie $K$ (zobacz rysunek).<p>
    <p><img src="https://i.imgur.com/iZ7MunK.png" class="mx-auto d-block"/></p>
    <p>Wtedy:</p>''',
        {
            'answers':{
            'A': '$|OK| = 6$',
            'B': '$|OK| = 8$',
            'C': '$|OK| = 10$',
            'D': '$|OK| = 12$',},
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='16',
        previous='14',
    ),

    '16': Exercise(
        'Zadanie 16', 'Dany jest romb o boku długości 4 i kącie rozwartym $150^\circ$. Pole tego rombu jest równe:',
        {
            'answers':{
            'A': '8',
            'B': '12',
            'C': r'$8\sqrt3$',
            'D': '16',},
            'correct': 'A'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='17',
        previous='15',
    ),

    '17': Exercise(
        'Zadanie 17', 'Proste o równaniach $y=(2m+2)x-2019$ oraz $y=(3m-3)x+2019$ są równoległe, gdy:',
        {
            'answers':{
            'A': '$m=-1$',
            'B': '$m=0$',
            'C': '$m=1$',
            'D': '$m=5$',
            },
            'correct': 'D'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='18',
        previous='16',
    ),

    '18': Exercise(
        'Zadanie 18',
        'Prosta o równaniu $y=ax+b$ jest prostopadła do prostej o równaniu $y=-4x+1$ i przechodzi przez punkt $P=(\\frac12,0)$, gdy:',
        {
            'answers':{
            'A': '$a=-4$ i $b=-2$',
            'B': '$a=\\frac14$ i $b=-\\frac18$',
            'C': '$a=-4$ i $b=2$',
            'D': '$a=\\frac14$ i $b=\\frac12$',},
            'correct': 'B'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='19',
        previous='17',
    ),

    '19': Exercise(
        'Zadanie 19', '''
    <p>Na rysunku przedstawiony jeest fragment wykresu funkcji liniowej $f$. Na wykresie tej funkcji leżą punkty $A=(0,4)$ i $B=(2,2)$.</p>
    <p><img src="https://i.imgur.com/mlDimd9.png" class="mx-auto d-block"/></p>
    <p>Obrazem prostej $AB$ w symetrii względem początku układu współrzędnych jest wykres funkcji $g$ określonej wzorem:</p>
    ''',
        {
            'answers':{
            'A': '$g(x)=x+4$',
            'B': '$g(x)=x-4$',
            'C': '$g(x)=-x-4$',
            'D': '$g(x)=-x+4$',},
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='20',
        previous='18',
    ),

    '20': Exercise(
        'Zadanie 20',
        'Dane są punkty o współrzędnych $A=(-2,5)$ oraz $B=(4,-1)$. Średnica okręgu wpisanego w kwadrat o boku $AB$ jest równa:',
        {
            'answers':{
            'A': '12',
            'B': '6',
            'C': '$6\\sqrt2$',
            'D': '$2\\sqrt6$',},
            'correct': 'A'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='21',
        previous='19',
    ),

    '21': Exercise(
        'Zadanie 21', '''<p>Promień $AS$ podstawy walca jest równy połowie wysokości $OS$ tego walca. Sinus kąta $OAS$ (zobacz rysunek) jest równy:</p>
    <p><img src="https://i.imgur.com/47JjEli.png" class="mx-auto d-block"/></p>''',
        {
            'answers':{
            'A': '$\\frac{\\sqrt5}2$',
            'B': '$\\frac{2\\sqrt5}5$',
            'C': '$\\frac12$',
            'D': '$1$',},
            'correct': 'B'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='22',
        previous='20',
    ),

    '22': Exercise(
        'Zadanie 22', '''<p>Podstawą ostrosłupa prawidłowego czworokątnego $ABCDS$ jest kwadrat $ABCD$. Wszystkie ściany boczne tego ostrosłupa są trójkątami równobocznymi.
    <p><img src="https://i.imgur.com/lYrGLMJ.png" class="mx-auto d-block"/></p>
    <p>Miara kąta SAC jest równa:</p>
    ''',
        {
            'answers':{
            'A': r'$90^\circ$',
            'B': r'$75^\circ$',
            'C': r'$60^\circ$',
            'D': r'$45^\circ$',},
            'correct': 'D'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='23',
        previous='21',

    ),
    '23': Exercise(
        'Zadanie 23', 'Mediana zestawu sześciu liczb $4,8,1,a,16,25$ jest równa 14. Zatem:',
        {
            'answers':{
            'A': '$a=7$',
            'B': '$a=12$',
            'C': '$a=14$',
            'D': '$a=20$',
            },
            'correct': 'B'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='24',
        previous='22',
    ),
    '24': Exercise(
        'Zadanie 24', 'Wszystkich liczb pięciocyfrowych, w których występują wyłącznie cyfry 0, 2, 5, jest:',
        {
            'answers':{
            'A': '12',
            'B': '36',
            'C': '162',
            'D': '243',
            },
            'correct': 'C'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='25',
        previous='23',
    ),

    '25': Exercise(
        'Zadanie 25',
        'W pudełku jest 40 kul. Wśród nich jest 35 kul białych, a pozostał to kule czerwone. Prawdopodobieństwo wylosowania każdej kuli jest takie samo. Z pudełka losujemy jedną kulę. Prawdopodobieństwo zdarzenia polegającego na tym, że wylosujemy kulę czerwoną, jest równe:',
        {
            'answers': {
            'A': '$\\frac18$',
            'B': '$\\frac15$',
            'C': '$\\frac1{40}$',
            'D': '$\\frac1{35}$',
            },
            'correct': 'A'
        }, answer_type=AnswerType.Closed,
        points=1,
        next='26',
        previous='24',
    ),

    '26': Exercise(
        'Zadanie 26', 'Rozwiąż równanie $x^3-5x^2-9x+45=0$.',
        {
            'num_answers': [0, 1, 2, 3, 4, 5],
            'answers': [5, 3, -3],
        },
        answer_type=AnswerType.ManyValues,
        points=2,
        next='27',
        previous='25',
    ),

    '27': Exercise(
        'Zadanie 27', 'Rozwiąż nierówność $3x^2-16x+16>0$.',
        {
            'num_answers': [1, 2],
            'answers': [
                    ['-inf', 'left-inf', '4/3', 'right-open'],
                    ['4', 'left-open', 'inf', 'right-inf']
                ]
        },
        answer_type=AnswerType.Intervals,
        points=2,
        next='28',
        previous='26',

    ),

    '28': Exercise(
        'Zadanie 28',
        'Wykaż, że dla dowolnych liczb rzeczywistych $a$ i $b$ prawdziwa jest nierówność: $$3a^2-2ab+3b^2\geq0.$$',
        {
            'steps': [
                    {'id': '0', 'value': 'Przekształcamy nierówność do postaci $a^2-2ab+b^2 \geq -2a^2-2b^2$.'},
                    {'id': '1', 'value': 'Zwijamy nierówność do postaci $(a-b)^2 \geq -2(a^2+b^2)$.'},
                    {'id': '2', 'value': 'Ponieważ $(a-b)^2$ jest dodatnie oraz $(a^2+b^2)$ jest dodatnie, to lewy czynnik zawsze będzie dodatni, a prawy zawsze będzie ujemny.'},
                    {'id': '3', 'value': 'Ponieważ dodatni czynnik będzie zawsze większy lub równy (dla zera) od ujemnego czynnika, nierówność jest poprawna dla każdego $a, b\in\mathbb R$.'},
                ],
            'correct_sequences': [['0','1','2','3']]
        },
        answer_type=AnswerType.Proof,
        points=2,
        next='29',
        previous='27',
    ),

    '29': Exercise(
        'Zadanie 29', '''<p>Dany jet okrąg o środku w punkcie $S$ i promieniu $r$. 
    Na przedłużeniu cięciwy $AB$ poza punkt B odłożono odcinek $BC$ równy promieniowi danego okręgu. 
    Przez punkty $C$ i $S$ poprowadzono prostą. 
    Prosta $CS$ przecina dany okrąg w punktach $D$ i $E$ (zobacz rysunek). 
    Wykaż, że jeżeli miara kąta $ACS$ jest równa $a$, to miara kąta $ASD$ jest równa $3a$.</p>
    <p><img src="https://i.imgur.com/wxlkGKI.png" class="mx-auto d-block"/></p>
    ''',
            {
                'steps': [
                    {'id': '0', 'value': 'Trójkąt BCS jest trójkątem równoramiennym.'}, 
                    {'id': '1', 'value': 'Ponieważ kąt ACS jest równy a, to kąt BSE jest również równy a.'},
                    {'id': '2', 'value': 'Z tego względu kąt CBS jest równy 180 - 2a.'},
                    {'id': '3', 'value': 'Zatem kąt ABS jest równy 2a.'},
                    {'id': '4', 'value': 'Ponieważ ABS jest trójkątem równoramiennym, kąt BAS też jest równy 2a.'},
                    {'id': '5', 'value': 'Kąt ASB jest równy 180 - 4a.'},
                    {'id': '6', 'value':  'Zatem kąt ASD, aby sumował się z ASB i BSC do 180 stopni, musi mieć wartość 3a.'}
                ],
                'correct_sequences': [['0','1','2','3','4','5','6']]
            },
        answer_type=AnswerType.Proof,
        points=2,
        next='30',
        previous='28',
    ),

    '30': Exercise(
        'Zadanie 30',
        'Ze zbioru liczb $\{1,2,3,4,5\}$ losujemy dwa razy po jednej liczbie ze zwracaniem. Oblicz prawdopodobieństwo zdarzenia $A$ polegającego na wylosowaniu liczb, których iloczyn jest liczbą nieparzystą.',
        [
            {'description': 'Prawdopodobieństwo', 'id': 'probability', 'value': '0.36'}
            ],
        answer_type=AnswerType.ListOfValues,
        points=2,
        next='31',
        previous='29',
    ),

    '31': Exercise(
        'Zadanie 31', r'''<p>W trapezie prostokątnym $ABCD$ dłuższa podstawa $AB$ ma długość 8. Przekątna $AC$ tego trapezu ma długość 4 i tworzy z krótszą podstawą trapezu kąt o mierze $30^\circ$ (zobacz rysunek). Oblicz długość przekątnej $BD$ tego trapezu.</p>
    <p><img src="https://i.imgur.com/X0QDW89.png" class="mx-auto d-block"/></p>''',
        [
            {'description': 'Długość przekątnej', 'id': 'diagonal', 'value': '2sqrt(17)'}
            ],
        answer_type=AnswerType.ListOfValues,
        points=2,
        next='32',
        previous='30'
    ),

    '32': Exercise(
        'Zadanie 32', '''<p>Ciąg arytmetyczny $(a_n)$ jest określony dla każdej liczby naturalnej $n\geq1$. Różnicą tego ciągu jest liczba $r=-4$, a średnia arytmetyczna początkowych sześciu wyrazów tego ciągu: $a_1,a_2,a_3,a_4,a_5,a_6$ jest równa 16.</p>
    <p>a) Oblicz pierwszy wyraz tego ciągu.</p>
    <p>b) Oblicz liczbę k, dla której $a_k=-78$.</p>''',
        [
            {"description": "Pierwszy wyraz", "id": "a_1", "value": '26'}, 
            {"description": "Wartość k", "id": "k", "value": '27'}, 
         ],
        answer_type=AnswerType.ListOfValues,
        points=4,
        next='33',
        previous='31',
    ),

    '33': Exercise(
        'Zadanie 33',
        'Dany jest punkt $A=(-18,10)$. Prosta o równaniu $y=3x$, jest symetralną odcinka $AB$. Wyznacz współrzędne punktu $B$.',
        [
            {"description": "Współrzędna x", "id": "x-coordinate", "value": '20.4'}, 
            {"description": "Współrzędna y", "id": "y-coordinate", "value": '-2.8'}, 
          ],
        answer_type=AnswerType.ListOfValues,
        points=4,
        next='34',
        previous='32',
    ),

    '34': Exercise(
        'Zadanie 34', r'''<p>Długość krawędzi podstawy ostrosłupa prawidłowego czworokątnego jest równa 6. Pole powierzchni całkowitej tego ostrosłupa jest cztery razy większe od pola jego podstawy. Kąt $\alpha$ jest kątem nachylenia krawędzi bocznej tego ostrosłupa do płaszczyzny podstawy (zobacz rysunek). Oblicz cosinus kąta $\alpha$.</p>
    <p><img src="https://i.imgur.com/REb8IXm.png" class="mx-auto d-block"/></p>''',
        [{"description": "Wartość $\\cos\\alpha$", "id": "cos-value", "value": "sqrt(5)/5"}],
        answer_type=AnswerType.ListOfValues,
        points=5,
        previous='33',),
}
