# Ohjelmistotekniikka, harjoitustyö
## Feedback-app
Sovelluksen avulla asiakkaat voivat antaa anonyymisti yritykselle palautetta, josta yritys saa analyysin omalle alustalleen. Sovelluksella on kaksi käyttäjäryhmää; asiakkaat ja organisaatio.

## Dokumentaatio

- [Käyttöohje](feedback_app/dokumentaatio/kayttoohje.md/)
- [Tuntikirjanpito](feedback_app/dokumentaatio/tuntikirjanpito.md/)
- [Vaatumusmäärittely](feedback_app/dokumentaatio/vaatimusmaarittely.md/)
- [Arkkitehtuurikuvaus](feedback_app/dokumentaatio/arkkitehtuuri.md/)
- [Changelog](feedback_app/dokumentaatio/changelog.md/)
- [Release](https://github.com/PieniiSienii/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus
1. Asenna riippuvuudet komennolla:

   ```bash
   poetry install
   ```

3. Alusta tietokanta komennolla:

   ```bash
   powtry run invoke build
   ```

5. Käynnistä sovellus komennolla:

   ``` bash
   poetry run invoke start
   ```

## Komentorivitoiminnot

### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla: 
``` bash
poetry run invoke start
```
### Testit
Testit suoritetaan komennolla:
``` bash
poetry run invoke test
```
### Testikattavuusraportti
Testikattavuusraportin saa komennolla: 
``` bash
poetry run invoke coverage-report
```
Sivun voi avata linkistä selaimeen

### Pylint
.pylintcr määrittelemät tarkistukset voi suorittaa komennolla:
``` bash
poetry run invoke lint
```
