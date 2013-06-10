#!/usr/bin/env python
#-*- coding: UTF-8 -*-

questions = [
(u"1 – Princip činnosti polovodičových prvků",
[u"Nejdřív tedy obecně o polovodičích a PN prvcích (Kunovský říkal, že je toho víc, tak ať si vyberu), obecně polovodiče, vlastní/nevlastní, typ P/N, pak dioda PN přechod a propustný/závěrný směr, potenciálová bariéra, V-A charakteristika (+její vysvětlení), saturace",
u"Pak nakreslit obvod s diodou a rezistorem (impedance) a jakým tam bude proud, jak zmírnit impedanci, vztah pro výpočet impedance",
u"5 příkladů kde se PN přechody využívají v praxi",
u"Bipolární a unipolární tranzistor – co je a nakreslit, čím se tranzistor spíná",
u"Nakreslit zapojení tranzistorů, které realizují NAND, Invertor",
u"Jak udělat AND (NAND + invertor), vícevstupej NAND (víc vodíčů do jednoho NANDu), 10 vodičů do jednoho NANDu (nejde, už by to bylo moc zatížený), NAND a příkon (žere hlavně když se přepíná, ale jinak taky žere ale málo), na čem závisí příkon NANDu (asi na frekvenci)"]),

(u"2 – Kombinační logické obvody",
[u"Co jsou kombinační obvody, jakej je rozdíl mezi kombinačníma a sekvenčníma, synchroní a asynchroní, čím se reprezentují (logickou funkcí, tabulkou)",
u"Popis demultiplexoru, vstupy, výstupy, řízení, nakreslit",
u"Obdobně pro multiplexor, dekodér, kodér(schématickou značku, popis principu a zapojení pomocí logických hradel – hlavně multiplexor)",
u"Co je nejdůležitější u logického obvodu (cena a výkon, možná pak i zpoždění)",
u"Umět spočítat počet tranzistorů pro realizaci multiplexoru, jak určit pracovní frekvenci (netuším)",
u"Multiplexor pro logickou funkci (1,5,7)",
u"Sčítačky – úplná, poloviční – jejich rozdíl, nakreslit 4bitovou sčítačku v sérii (nevím jak to přesně má být), zpoždění (úměrné počtu bitů)"]),

(u"3 – Sekvenční logické obvody",
[u"Obecně klopné obvody – rozdělení, nakreslit značení KO-RS, KO-D, KO-T a vysvětlit jak to funguje, jak se popisuje jejich chování (automatem), definici automatu",
u"Moore a Mealy, rozdíly",
u"Umět nakreslit KO ne jako značku, ale s logickými členy",
u"Umět nakreslit přechodový graf (např. RS, JK a umět určit jestli je Moore nebo Mealy)",
u"Jak vytvořit pomocí klopných D obvodů registr"]),

(u"4 – Hierarchie paměti v počítači",
[u"Rozdělení pamětí dle typu (vnitřní paměti procesoru, hlavní paměti včetně rychlých vyrovnávacích a vnější paměti) a principu (polovodičové – bipolární a unipolární MOS, CMOS, magnetické, optické), uchování informací, princip lokality",
u"Vědět přístupové doby (řádově ns u registrů",
u"Rozdíl SRAM a DRAM a příklady – cena za buňku, realizace, složitost, rychlost, hustota na čipu, odběr paměti (která paměť víc žere)",
u"Který registr se používá nejvíce (střadač)",
u"RVP – organizace, přímé a asociativní mapování, velikost, jednotlivé stavy, ",
u"Co je to ROM, PROM, EPROM a EEPROM"]),

(u"5 – Vestavěné systémy",
[u"Obecně co je to vestavěný systém, vlastnosti, využití, architektura (řídíc a funkční bloky), reaktivnost, porovnání s normálním PC. ",
u"Mikrokontrolér – co je to apod.",
u"Časovač – co to je, účel (umožňuje zjistit, kdy došlo k zachycení hrany jednotkou záchytu hrany), duální fci k záchytu hrany (hrana se vygeneruje)",
u"PWM ",
u"WatchDog",
u"Rozhraní a převodníky – principy, části (např. znát dolnopropustní filtr u převodníku)",
u"SCI a SPI, čím se synchronizuje SCI, když je asynchronní (pomocí start bitu)",
u"Synchronní a asynchronní sériový přenos – co to je, kterých je rychlejší (synchronní)"]),

(u"6 – Principy řízení a připojování periferních zařízení",
[u"Systémová sběrnice (má řídící vodiče, datové a adresové vodiče, ty se mohou u sdílených sběrnice překrývat), jaké signály se mohou vyskytovat (nejsem si jist, jestli ty 4 signály: čtení/zápis z/do pamětí a do/z datové části, nebo by to měli být signály se žádostí o přerušení, žádost o přímý přístup do paměti)",
u"Jak funguje přerušení, jak CPU pozná jak má obsloužit přerušení (řadič přerušení mu předá nějakou instrukci s odkazem na program, který se má spustit)",
u"DMA",
u"Jak zjišťovat stav periferní operace (přerušením nebo programovou obsluhou – neustálé dotazování procesoru)"]),

(u"7 – Princip činnosti počítače",
[u"Obecně zřetězené zpracování instrukcí",
u"CISC a RISC, základní rozdíly, význam",
u"Jaký procesor je využívá, jaká část je implementována v inteli, jak se dekóduje instrukce (více dekodérů pro různé druhy), jak zrychlit zpracování (paměť na instrukce), kolikrát je RISC rychlejší v ideálním případě",
u"Jak je to u zřetězeného zpracování když je jeden operand v hlavní paměti a druhý v RVP",
u"Co se stane, když přijde podmíněný a nepodmíněný skok a jak se to řeší na úrovni HW a SW",
u"Délka instrukcí, co znamená první C",
u"Počet a typ instrukcí, aby byl poznat rozdíl a kde je výhodnější RISC",
u"Konflikty – vyjmenovat a vysvětlit na příkladech, i jak se řeší",
u"Co je to hazard, jak vzniká a jak se tomu předchází"]),

(u"8 – Minimalizace logických výrazů",
[u"Co je to minimalizace, proč se dělá, způsoby jak se minimalizace provádí (algebraické, grafické – Karnaughovou mapou, algoritmické)",
u"Boolovská algebra - formální definice, operátory + a . (co znamenají, + je nebo, . a zároveň),",
u"Vědět vzorce bool. Algebry – asociativita, sousednost, sjednocení s nulou a de Morgan",
u"Příklad s Karnaughovou mapou, sám nakreslit nějakou, jak probíhá minimalizace, Karnaughova mapa celé z 1 (její výsledek je 1)",
u"UNDF (log. 1), UNKF (log. 0)",
u"Quine-McCluskey – jak funguje, co na konci vznikne ",
u"Jestli má minimalizace význam v dnešní době (určitě ano, dále rozvést proč)",
u"Nesporné implikanty (můžou se objevit další termíny)",
u"Lze použít pro hradlová pole (nelze, spíše se to používá pro obvody z konkrétních log. Členů)"]),

(u"9 – Reprezentace čísel a základní dvojkové aritmetické operace v počítači",
[u"Rozdělení čísel na FX a FP, jak jsou reprezentována, příklady",
u"FP – normalizace a subnormalizované číslo",
u"Reprezentace záporných čísel, umět i grafy (např. v kódu transformované 0 co bude za hodnotu když bude mít všechny bity 0)",
u"Jak je to s přetečním",
u"Sčítání dvou čísel se znaménkem a bez znaménka v doplňkovém kódu",
u"Násobení dvou čísel v doplňovkém výsledku, co je výsledkem",
u"Co je to Boothův algoritmus"]),

(u"10 – Principy VHDL",
[u"Procesy syntézy (Behaviorální, RTL, Logická)",
u"VHDL – obecně, co je to entita/architektura, co je to proces, jaké typy příkazů jsou v architektuře (paralelní) a procesu (sekvenční), jaké části má proces (deklarační část, sensitivity list a signály), dataflow/strukturální popis,"]),

(u"11 – Metody rasterizace 2D vektorových objektů: úseček, kružnic a křivek",
[u"Obecně co je to rasterizace, proč ji potřebujeme, základní typy vekterových objektů",
u"Rasterizace úsečky – jaké vlastnosti musí úsečka splňovat, rovnice úsečky, algoritmy, co je vstupem a výstupem algoritmů, DDA, DDA s hlídáním chyby, Bresenham (prediktor), jak počítat úsečku, která není v prvním kvadrantu (využití výměny souřadnic, os, prostě dostat ji do prvního kvadrantu a pak zpět)",
u"Rasterizace kružnice – vyjádření, vykreslení po bodech, midpoint",
u"Rasterizace křivky, vlastnosti křivek, druhy, algoritmy (desetinný – vyjádřím křivku polynomem dosazuju X a získávám Y, nebo de Casteljau)",
u"Konkrétní otázky: jaký by mohl vyzniknout problém při ukončování rasterizace kružnice, proč by měli být celočíselné algoritmy rychlejší (dřív to platilo, dneska to tak už není, protože v CPU jsou specializovány moduly pro práci s desetinnými čísly)"]),

(u"12 – Transformace, reprezentace a zobrazení 3D objektů",
[u"Definice bodu v prostoru, transformační matice",
u"Lineární transformace",
u"Nakreslit přímku a její vyjádření (např. směrnicové)",
u"Aspoň nějakou matici pro transformaci vědět (třeba pro posun)",
u"Rotaci kolem obecné osy",
u"Umět pracovat s maticí, a umět je mezi sebou násobit a i s vektory",
u"Co je to gradient (strmost), jaké jsou transformace (otočení, posunutí, změna měřítka, …) a jak se provádí (vynásobením transformační maticí, kde záleží na pořadí), proč používáme na transformace matice a ne něco jiného, proč máme tu váhu bodu",
u"Jak transformovat něco b-rep (musí se pracovat s body a to s těmi význačnými, tedy u válce se středy kružnic a u polygon. Modelu s vrcholy)",
u"Projekci (nezapomenout že je to taky transformace), druhy projekcí",
u"Manifold, CSG, voxely, B-rep",
u"Polygonální model – jak je uložen v paměti, jak ho vykreslit (zjistit co je viditelné, ořezat, udělat projekci, určit barvu každého polygonu – podle světla …), u každé fáze vědět algoritmy"]),

(u"13 – Principy grafických uživatelských rozhraní",
[u"Komunikační kanály (ty smysly)",
u"Módy komunikace (něco jako že PC reaguje v jakémkoli čase na jednu událost stejným způsobem)",
u"Událostmi řízené systémy – co to je, jak se implementují a jejich výhody a nevýhody",
u"Prvky uživatelského rozhraní – textbox, selectbox, radio button, checkbox",
u"AJAX – co to je, k čemu je"]),

(u"14 – Spektrální analýza spojitých a diskrétních signálů",
[u"Co jsou to signály, co je to spektrální analýza a proč se dělá, co je to spektrum",
u"Rozdělení signálů (spojité a diskrétní)",
u"Diskrétní signály – co je výstup, konkrétně u diskrétních periodických signálů",
u"Zakreslit nějaký signál a vyznačit kde jsou na něm koeficienty (například cosinu a zakreslit modul a argument)",
u"Druhy frekvencí (obyčejná, kruhová, normovaná)",
u"Fourierova řade (vzorec je suma komplexních exponenciál), komplexní exponenciály",
u"Fourierova transformace",
u"Nyquistův teorém – princip"]),

(u"15 – Číslicové filty",
[u""]),

(u"16 – Množiny, relace a zobrazení",
[u"Definice množiny, zobrazení, relace",
u"Jak se zapisuje množina, operace na množinách, spočetnost množin",
u"Často bývá matematické vyjádření množiny sudých kladných čísel, nejčastější operace u množin (náleží, prvek patří do)",
u"Zapsat rozdíl množin, zapsat množinově konkatenaci jazyka (konkatenace je zřetězení, w*w‘, nevím co u toho přesně chce slyšet)",
u"Multimnožina (je zobecnění množiny, prvky se mohou vyskytovat vícekrát)",
u"Relace a definovat binární relaci a Kartézský součin, vlastnosti relací (reflexivní, symetrická, antisymetrická, tranzitivní)",
u"Popsat jednotlivé druhy zobrazení"]),

(u"17 – Diferenciální a integrální počet funkcí více proměnných",
[u"Definice limity",
u"Definice derivace pro funkci jedné proměnné a vysvětlit – umět to s trojúhelníkem, tangens apod.",
u"Klesající/rostoucí, maxima/minima, inflexní body, konkávní/konvexní",
u"Základní pravidla derivování",
u"Definice Integrálu a pak určitý a neurčitý",
u"Výpočet integrálu pro přímku y=x od 0 do a",
u"Funkce více proměnných",
u"Co je to gradient"]),

(u"18 – Číselné soustavy a převody mezi nimi",
[u"Polyadické a nepolyadické soustavy – rozdíl, příklady",
u"Metody převádění mezi soustavami, umět v praxi",
u"Umět rozložit číslo na polynom, tedy polynominální zápis, umět vysvětlit poziční zápis",
u"Jak převést binární číslo na hexadecimální – teoreticky, prakticky i v pseudokódu",
u"Převod čísel do dvojkové soustavy (příklad s 30 na 8bitů, kdyby bylo záporné, tak jak by vypadalo v přímém kódu/doplňkovém, ještě i desetinné číslo převést do dvojkové soustavy)",
u"Jak se jmenuje instrukce v asembleru, která převede znaménkové číslo z 8bit registru do 16bit registru se zachováním znaménka (asi Convert)"]),

(u"19 – Boolovy algebry",
[u"Matematický zápis algebry (B = (D, +,*, (not), 0, 1), kde D je doména)",
u"Axiom – co to je a znát je, pak také znát některé teorémy, neutrální prvek, demorgana,",
u"Často je tam práce s množinou {a, b, c}, její potenční množinou, co je v ní 0 a 1",
u"Zda může být boolova algebra na nekonečné množině (asi ne, nevědělo by se kde je max, neboli komplement prázdné množiny)",
u"Využití potenční množiny při popisu booleových algeber"]),

(u"20 – Regulární jazyky a jejich modely",
[u"Regulární jazyk, regulární gramatika, jaká jsou tam pravidla, poznámka (jejich modelem jsou regulární výrazy a KA), definice RV, co je to jazyk, formální definice konkatenace dvou jazyků",
u"Jsou mocnější RV a nebo RV unixového nástroje GREP (základní nástroje GREPu jsou méně mocné než RV z IFJ – například chybí operace sjednocení |)",
u"Definice KA, umět přepsat pa -> q na relaci",
u"Umět nakreslit KA – ať už zadaný nebo vlastní, zadaný například KA který bude přijímat řetězec obsahující sudý počet znaků, a umět KA převést na RV, další příklad může být KA, který generuje nad abecedou {a,b,c} řetězce, kde je každý druhý znak „a“",
u"Rozdíl mezi regulární a bezkontextovou gramatikou, (pravidlo Neterminal->neterminál, BKG se můžou zanořovat a závorkovat)",
u"Druhy automatů (deterministický, nedeterministický, …)",
u"Umět taky více operací s KA - sjednotit 2 apod.",
u"Umět převést KA z nedeterministického na deterministický"]),

(u"21 – Bezkontextové jazyky a jejich modely",
[u"Bezkontextová gramatika (čtveřice …) – definice",
u"Bezkontextový jazyk",
u"Derivační pravidlo",
u"Definice řetězce (L Sigma *)",
u"ZA",
u"Rozdíl mezi BKG a ZA (popisují stejnou třídu jazyků)"]),

(u"22 – Struktura překladače a charakteristika fází překlad",
[u"Znát určitě z předchozích: definici jazyka, gramatiky, BKG apod.",
u"Překladač, fáze překladu",
u"Co se děje v jednotlivých fázích a jakým způsobem pracují, co z nich vyleze",
u"Zkráceně: Lexikální analýza (konečný automat, je tam regulární jazyk), syntaktická analýza",
u"Nějakou konstrukci nějakého jazyka, která by byla z pohledu syntaktické analýzy nejednoznačná",
u"Derivační strom",
u"Metody shora dolů, zdola nahoru – jak fungují, co se u nich používá",
u"Generování výsledného kódu – jaké typy kódů znám (asi byte kód, strojový kód)",
u"Jaký typ architektury se používá v JVM (zásobníková)",
u"Který jazyk se nepřekládá do strojového jazyka (Python)"]),

(u"23 – Numerické metody a matematická pravděpodobnost",
[u"Matice, determinanty,",
u"Vektorový tvar,",
u"Obyčejné diferenciální rovnice (rovnice, které obsahují proměnné a jejich derivace), proč (např. napětí kondenzátoru v závislosti na čase), jak (Euler, runge kutta, taylor)",
u"Jdou řešit analyticky? (jdou ale neděláme to, protože je to složité a nepohodlné)",
u"Metody řešení diferenciálních rovnic",
u"Eulerova metoda, Runge Kutta – jednokrové",
u"Cramer – analytická metoda",
u"Víceřádové metody",
u"Metoda snižování řádu derivace a postupné integrace",
u"Pravděpodobnost, jaký je to jev, umět popsat na hodu kostkou, P nemá jednotku (bezrozměrná veličina)",
u"Pravděpodobnost se spojitým průběhem (integrálem vypočítáme obsah pod tou častí fce kde chceme tu P vypočítat, pokud chceme vypočítat pravděpodobnost menší jak nějakou hodnotu, tak je to integrál od –INF do té hodnoty)",
u"Pseudonáhodná čísla vs. Náhodná, kongruentní generátor + jeho nevýhody (velká nevýhoda je, že po restartu aplikace se začíná opět se stejným počátečním seedem)",
u"Graf rozložení hustoty pravděpodobnosti (normální, gausovo, exponenciální), transformace rozložení pravděpodobnosti, jak generovat exponenciální rozložení (metoda inverzní transformace)"]),

(u"24 – Řešení úloh",
[u"Co je úloha, prohledávání stavového prostoru - definice, rozdělení na informované a neinformované metody",
u"Algoritmus BFS, DFS – jak fungují, co používají",
u"Kritéria pro hodnocení metod (úplnost, optimálnost) a jak jsou na tom různé metody, umět vzorec pro časovou složitost",
u"Jaká metoda má nejmenší paměťovou složitost (Backtracking – ukládá jen cestu a použité operátory u uzlů)",
u"Informované metody – BestFS, co znamená g(x) a h(x)",
u"A*, GS, UCS",
u"Jaký je vztah heuristického ohodnocení v algoritmu A* k reálnému ohodnocení (větší, menší?)",
u"AND/OR grafy – co to je, jak to funguje",
u"Minimax, Alfa/Beta – vědět o co je, umět nakreslit na příkladu",
u"Složitost, třídy složitosti, definice a složitosti základních algoritmů"]),

(u"25 - Simulace",
[u"Systém – formální definice, simulace, vznik modelu systému, abstraktní model, simulační model, vztahy mezi modely (homomorfní a izomorfní), základní typy simulací (diskrétní, spojitá, kombinovaná) – kdy se používají a čím je vyjadřujeme, řízení simulací",
u"Petriho sítě – umět popsat, místa, transakce, pravděpodobnostní přechody",
u"Dělení systému",
u"Modelový čas",
u"Spojité systémy (výjádřené vztahy – většinou diferenciální rovnice prvního řádu)",
u"Hybridní model/simulace, Kombinovaná simulace (skákající míček – popsat že se tam skokově mění stav, celkově si o tomhle jistit více)",
u"SHO – co znamená M/M/1"]),

(u"26 – Datové a řídící struktury",
[u"Datové struktury – co to je, jak je dělíme a jaké máme.",
u"Seznam – druhy, operace nad nimi, prázdný atd.",
u"Složitost vkládání prvku do seznamu, jak dosáhnout konstantní složitosti i pro poslední prvek.",
u"Fronta, zásobník",
u"Binární strom – princip, umět namalovat, průchody binárním stromem – jaké jsou a u některého umět algoritmus – rekurzivní i nerekurzivní",
u"Řídící struktury",
u"Definice cyklů, iterační, sekvenční ",
u"Vytvoření cyklu bez použití for/while (využít goto)"]),

(u"27 – Vyhledávání a řazení",
[u"Vyhledávání – obecně, používané metody, rozdělené",
u"Sekvenční vyhledávání, kdy je výhodné použít (když je seřazené pole)",
u"Vyhledávání se zarážkou – výhody a nevýhody",
u"Asymptotické složitosti vyhledávacích algoritmů",
u"Tabulky s přímým přístupem, co když jsou dvě hodnoty fce stejné",
u"Hash tabulka – hashovací funkce, synonyma, klíč, druhý přístup využívající krok",
u"BVS a jeho složitost (logaritmická – je to dané výškou stromu)",
u"AVL strom",
u"Řazení – formálně (relace uspořádání?), stabilita, přirozenost, třídění, setřídění",
u"Bubble sort, Quick sort"]),

(u"28 – HTML a Javascript",
[u"Tvorba webu, DOM, ",
u"SGML a vztah mezi SGML a HTML",
u"HTML – jaká množina jazyků (kontextový), značkovací jazyk z rodiny SGML, nevýhoda HTML z pohledu vizualizace (jednotlivé prvky se zobrazují jako obdélníky, proto je problém udělat třeba kulaté rohy)",
u"CSS (využívá se prioritní strom) – proč se jmenují kaskádové styly",
u"JavaScript, klientský JS",
u"Závislost HTML a událostí",
u"Jak udržovat informace na stránce (cookies, sessions)",
u"AJAX"]),

(u"29 – Hodnocení složitosti algoritmů",
[u"Jak složitost charakterizujeme, jak obtížnost zjistit",
u"Druhy složitostí, způsob určování",
u"Asymptotická složitost",
u"Horní, dolní a průměrný odhad složitosti",
u"Umět nakreslit graf"]),

(u"30 – Životní cyklus software",
[u"Jednotlivé etapy a modely životního cyklu",
u"Vodopádový model",
u"RUP",
u"V-model",
u"Spirálový model – umět nakreslit a popsat jaké části se střídají (zmínit také že probíhá analýza rizik)",
u"Agilní metody (hodí se vědět něco málo)"]),

(u"31 - UML",
[u"UML - co to je, využití (v SW inženýrství, modeluje části systému v SW)",
u"Pohled a jaké známe, typy diagramů a základní rozdělení,",
u"Diagram tříd – z čeho se skládá, jaké jsou tam vztahy (generalizace – dědičnost, asociace – 2 druhy, dekompozice, agregace)",
u"Sekvenční diagram (zobrazuje posloupnost akci mezi aktery/prvky, svislá osa čas, vodorovná aktéři)",
u"Use-Case diagram",
u"Stavový diagram"]),

(u"32 Konceptuální modelování a návrh relační databáze",
[u"Proces návrhu databáze, Konceptuální modelování (vstup a výstup)",
u"Entita, umět popsat vztah mezi nimi, převést M:N vztah, umět upravit entity s redundantními daty, má smysl mít redundantní data (rychlejší SELECT a využití u operace JOIN), Entitní množina",
u"ER diagram – co to je, umět i nakreslit, kardinalita, primární a cizí klíče, referenční integrita"]),

(u"33 – Relační datový model a jazyk SQL",
[u"Matematická relace, relační algebra, databázová tabulka – kde v ní je ta relace",
u"Operace Union",
u"SQL, operace u DDL a DML",
u"Umět SELECT se spojením dvou tabulek",
u"Integritní omezení, referenční integrita, primární klíč",
u"Typy spojení, jak spojit tabulky určitým způsobem (vnější spojení)",
u"Selekce a projekce"]),

(u"34 – Principy a struktury správy souborů a správy paměti",
[u"Soubor, jaké má atributy, souborový systém, rozdělení disku, i-uzly (jméno souboru není v i-uzlu, ale adresáři), jak se odkazuje na datové bloky,",
u"LAP, FAP, překlad mezi nimi, jak probíhá, jaký prostor na to je potřeba, MMU",
u"Tabulka stránek – jak se v ní hledá, hierarchické tabulky stránek,",
u"Virtualizace stránek, page deamon"]),

(u"35 – Plánování a synchronizace procesů, transakce",
[u"Preemptivní a nepreemptivní plánování, inverze priorit, prioritní plánování",
u"Synchronizace procesů, kritická sekce",
u"Specializované algoritmy pro vstup do KS – umět popsat (Petersonův a Bakery, ty jsou asi starší, tak pak semafory, mutexy a monitory)",
u"Semafor pseudokód, Monitor princip",
u"Možná i instrukce TestAndSet a Swap"]),

(u"36 – Objektová orientace",
[u"Základní koncepty OOP: objekt, zapouzdření, polymorfismus, dědičnost, abstrakce",
u"Výhody a nevýhody OOP",
u"Jak se implementuje polymorfismus (pomocí VMT – tabulka virtuálních metod)",
u"Třídní a beztřídní OOJ, jaký je rozdíl, jak fungují, jak je řešena dědičnost (delegování u třídních X )",
u"Čistě OOJ, hybridně OOJ,"]),

(u"37 – Programování v jazyku symbolických instrukcí",
[u"Jazyk symbolických instrukcí, strojový jazyk, asembler, jak probíhá překlad, proč se strojový kód nepoužívá (nepředvídatelnost podmínek, složitější implementace)",
u"Činnost počítače – z čeho se skládá apod.",
u"Jak funguje fetch, decode, execute",
u"Instruction pointer registr, instruction registr",
u"Instrukční sada – jaké jsou druhy instrukcí, jak vypadá instrukce, popsat operandy, práce s pointry (hranaté závorky), jak sou instrukce kódovány",
u"Rozdělení instrukcí (strojové, direktivy, makra)",
u"Makroinstrukce a pseudoinstrukce",
u"Příznakový registr – co obsahuje, co mají jednotlivé bity na starost"]),

(u"38 – služby aplikační vrstvy",
[u"Matoušek rovnou dával zaměření a to hlavně na telefonii, snmp a jednou netflow ",
u"IP Telefonie, H.323",
u"IP Telefonie",
u"H.323 – dílčí protokoly",
u"Co se převádí do veřejné telefonní sítě PSTN (tady asi jaký prvek, tak brána – gateway), na jakou ústřednu klient posílá zprávu INVITE (v DNS je na to záznam SRV), jak se pozná že daný RTP tok patří k dané komunikaci,",
u"SNMP",
u"Princip, agent a manager, jak funguje zasílání informací, zmínit také Traps",
u"Využití",
u"Ukládání statistik, MIB",
u"SNMP příkazy – jaké jsou, co s nimi nastavím",
u"Netflow"]),

(u"39 – TCP/IP Komunikace",
[u"Komunikace klient-server, co má splňovat (má být konkurentní),",
u"Vrstvy podle TCP modelu, znát i OSI/ISO a umět mezi sebou porovnat, příklady protokolů na jednotlivých vrstvách",
u"IP, TCP a UDP protokoly, rozdíl TCP a UDP",
u"Jak se řeší spolehlivost přenosu",
u"Rozdíl mezi go-back-n a selective repeat – jsou to používané politiky",
u"Statická a dynamická konfigurace IP adresy",
u"QoS, fragmentace ",
u"Jaké jsou typy ip adres a jaký použít protokol pro přenos streamovaného videa",
u"Umět nakreslit datagram a jak je postupně zabalený",
u"Sliding window – princip, k čemu je (aby nedošlo k zahlcení, aby se neposílaly další pakety dokud nejsou v okně potvrzené),"]),

(u"40 – Směrování a filtrování dat v internetu",
[u"Směrování",
u"Popsat algoritmy",
u"Link-state",
u"Dijkstrova metoda – jak funguje, k čemu slouží (výpočet nejkratší cesty v grafu)",
u"Filtrování",
u"Podle jakých kritérií se filtruje, jaké jsou typy firewalů, jak se realizuje samotné vyhledávání (sekvenčně, trie/grid of tries, …)",
u"Klasifikace paketů, firewally",
u"QoS",
u"Rozdělení služeb (diferencované a integrované)",
u"K čemu to je, dle čeho upřednostňujeme tok, kdo značuje pakety (router)",
u"Jaké jsou třídy paketů (best effort, )",
u"SLA, RSVP, rezervaci, DSCP, ToS",
u"WRED, RED"])
]
