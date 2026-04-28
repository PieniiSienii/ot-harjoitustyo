# Ohjelmistotekniikka, harjoitustyö
## Feedback-app
Sovelluksen avulla asiakkaat voivat antaa anonyymisti yritykselle palautetta, josta yritys saa analyysin omalle alustalleen. Sovelluksella on kaksi käyttäjäryhmää; asiakkaat ja organisaatio.

## Dokumentaatio

- [Käyttöohje](feedback_app/dokumentaatio/kayttoohje.md/)
- [Tuntikirjanpito](feedback_app/dokumentaatio/tuntikirjanpito.md/)
- [Vaatumusmäärittely](feedback_app/dokumentaatio/vaatimusmaarittely.md/)
- [Arkkitehtuurikuvaus](feedback_app/dokumentaatio/arkkitehtuuri.md/)
- [Changelog](feedback_app/dokumentaatio/changelog.md/)
- [Release](https://github.com/PieniiSienii/ot-harjoitustyo/releases/tag/viikko5)

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
