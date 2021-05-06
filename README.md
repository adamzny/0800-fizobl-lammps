# 0800-fizobl-lammps

## Badanie dysocjacji NaCl w wodnym roztworze

Symulacja wykonana była za pomocą programu lammps, a analizy danych dokonano za pomocą PLUMED oraz pythona. Do wizualizacji użyto VMD.
Przykładową klatkę z symulacji można zobaczyć w pliku ![nacl.tga](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/nacl.tga)

Symulacja odbywała się w temperaturez 300 K i trwała 1 ns. Bananymi parametrami były odległość między atomami sodu i chloru oraz liczba koordynacyjna.

Zmiany odległości w czasie przedstawiono na wykresie:

![Zmiany odległości](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/distance-time.png)

Ich rozkład przedstawia histogram:

![Histogram](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/histogram.png)

Jony chloru i sodu spędziły większość czasu w formie zdysocjowanej, a najbardziej prawdopodobna wartość odległości między nimi to około 0.5 nm

Dzięki ergodyczności trajektorii można obliczyć energię swobodną układu F=-ln(N) (gdzie N oznacza histogram) która przedstawia się następująco:

![Energia swobodna](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/free_energy.png)

Jak widać, bariera potencjału ma wysokość ok 3 kT i odpowiada odległości ok. 0.4 nm.

Liczba koordynacyjna reprezentuje liczbę atomów związanych z jonem. Dla przeprowadzonej symulacji startuje ona z okolic trójki po czym szybko osiąga optymalną wartość około 5-6, co obrazują wykresy:

![Coordination number in time](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/)

![Coordination number histogram](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/histogram_coord.png)

Otrzymany przebieg energii swobodnej to

![Energia swobodna koordynacji](https://raw.githubusercontent.com/adamzny/0800-fizobl-lammps/main/free_energy_coord.png)

Z powyższych wykresów można odczytać, że liczba koordynacyjna oscylowała przede wszystkim między wartościami 5 i 6, przy czym częstsza była wartość 6. Odpowiadające tym wartościom minima energii swobodnej były oddzielone niewielką barierą potencjału. Dużo rzadziej osiągane były wartości 3 i 4 - odpowiadające im minima lokalne są bardzo płytkiie i oddzielone od wartości 5 i 6 wysoką barierą potencjalną.
