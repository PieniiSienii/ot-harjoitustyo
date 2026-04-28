# Käyttöohje
Lataa viimeisimmän releasen lähdekoodi

## Käynnistäminen

Ennen käynnistystä, asenna riippuvuudet komennolla:

```bash
poetry install
```

ja suorita sen jälkeen alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

## Käyttäjän valinta

Sovellus käynnistyy käyttäjän valinta ikkunaan:

![](kuvat/aloitusikkuna.png)

Valitse nappia painamalla, haluatko jättää palautteen vai tarkastella organisaation työntekijänä oman organisaation palautteita.

## Organisaatio rooli

Valittuasi käyttäjäksi organisaation, aukeaa tietyn organisaation valintaikkuna. Painiketta painamalla voi valita, minkä organisaation palautteita haluat tarkastella:

![](kuvat/org_valintaikkuna.png)


### Palautteiden tarkastelu
Valittuasi organisaation, näet sille annettujen palautteiden tiivistelmän. Voit myös tarkastella palautteita ryhmiteltynä moodin mukaan:

![](kuvat/org_ratings.png)

ja 

![](kuvat/ratings_by_mood.png)


## Asiakas rooli
Valittuasi käyttäjäksi asiakkaan, aukeaa tietyn organisaation valintaikkuna. Painiketta painamalla voi valita, mille organisaatiolle haluaa antaa palautetta:

![](kuvat/org_valintaikkuna.png)

### Fiilikseen vastaaminen
Valittuasi organisaation, sovellus kysyy sinulta ensin, millainen fiilis sinulla ylipäätään on tänään. Klikkaamalla sinulle parasta vaihtoehtoa pääsee eteenpäin:

![](kuvat/mood_näkymä.png)

### Kysymyksiin vastaaminen
Valittuasi fiiliksen, sovellus kysyy sinulta kolme (3) kysymystä liittyen asiointiin yrityksessä. Vastaa kysymyksiin asteikolla 1-5:

![1](kuvat/cleanliness_q.png)

![2](kuvat/customer_service_q.png)

![3](kuvat/recommend_q.png)

### Kiitos näkymä
Vastattuasi kaikkiin kysymyksiin voit sulkea ikkunan:

![](kuvat/end.png)


**Huom!** Voit painaa `Back` -nappia päästäksesi edelliseen ikkunaan tai `Close Window` sulkeaksesi ikkunan, jos sellaine nappi on näkymässä tarjolla.

