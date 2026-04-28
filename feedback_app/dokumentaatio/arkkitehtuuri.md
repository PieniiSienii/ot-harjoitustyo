# Arkkitehtuurikuvaus

## Rakenne

Rakenne noudattaa kerrosarkkitehtuuria, jossa käyttöliittymä on eroteltu sovelluslogiikasta ja tietojen tallennuksesta.


### Pakkauskaavio

``` mermaid
flowchart TD
    UI["UI"] --> Service["Services"]
    UI --> OrgRepo["Organization Repository"]

    Service --> FbRepo["Feedback Repository"]
    FbRepo --> DB[(SQLite)]
    OrgRepo --> DB

    UI --> Entities["Entities 
                    Feedback, Organization"]
    Service --> Entities
    FbRepo --> Entities
    OrgRepo --> Entities

    Init["initialize_db.py"] --> DB
    Conn["db_connection.py"] --> DB

```

## Käyttöliittymä
Käyttöliittymää ohjaa UI-luokka, joka ensin näyttää käyttäjävalinnan, ja ohjaa käyttäjän sen jälkeen joko:

- Asiakaspolkuun (`CustomerUI`), tai
- Organisaatiopolkuun (`OrganizationUI`)

Asiakaspolku etenee seuraavasti:

1. Valitse organisaatio
2. Fiiliksen valinta
3. Kolmeen kysymykeen vastaaminen asteikolla 1-5
4. Lopetusnäkymä

Organisaatiopolussa käyttäjä valitsee organisaation, jolloin  näytetään koonti sen palautteista.

## Sovelluslogiikka

Sovelluslogiikasta vastaa `FeedbackService` joka tarjoaa eri metodeita: 

- `save_feedback(org_id, mood, answers)`
- `get_all()`
- `get_average_ratings(org_id)`
- `get_average_ratings_by_mood(org_id)`

FeedbackService tallentaa palautteen `Feedback`-oliona ja antaa tallennuksen vastuun `FeedbackRepository`-luokalle.
Service laskee myös organisaation palautteiden kysymyskohtaiset keskiarvot ja voi luokitella ne moodin mukaan.

`Organization`ja `Feedback` muodostavat sovelluksen tietomallin, jossa organisaatiolla on useita siihen liittyviä palautteita:

```mermaid
    classDiagram
        class Organization {
            org_id
            name
        }

        class Feedback {
            org_id
            mood
            answers
        }

        Organization "1" --> "*" Feedback
```

## Tietojen pysyväistallennus

Tietojen tallennuksesta huolehtii `repositories` luokat `FeedbackRepository` ja `OrganizationRepository`. Tiedot tallennetaan SQLIte- tietokantaan.

## Päätoiminnallisuudet

Kuvataan toimintalogiikkaa sekvenssikaaviona

### Asiakas antaa palautetta

Kun aloitusnäkymässä painetaan painiketta `Customer`, etenee sovellus seuraavasti:

```mermaid
sequenceDiagram
    actor Asiakas
    participant CustomerUI
    participant ViewFlow
    participant SelectOrganizationView
    participant MoodView
    participant QuestionsView
    participant FeedbackService
    participant FeedbackRepository

    Asiakas->>SelectOrganizationView: valitsee organisaation
    SelectOrganizationView-->>CustomerUI: handle_org(org_id)

    CustomerUI->>ViewFlow: show(MoodView)

    Asiakas->>MoodView: valitsee fiiliksen
    MoodView-->>CustomerUI: handle_mood(mood)

    CustomerUI->>ViewFlow: show(QuestionsView)

    Asiakas->>QuestionsView: vastaa kysymyksiin
    QuestionsView-->>CustomerUI: handle_questions(answers)

    CustomerUI->>FeedbackService: save_feedback(org_id, mood, answers)
    FeedbackService->>FeedbackRepository: add_fb(feedback)

    FeedbackRepository-->>FeedbackService: ok
    FeedbackService-->>CustomerUI: return

    CustomerUI->>ViewFlow: show(EndView)
    CustomerUI-->>Asiakas: näyttää EndView-näkymän
```

### Organisaatio tarkastelee palautteita

Kun aloitusnäkymässä painetaan `Organization`, etenee sovellus seuraavasti:

```mermaid
sequenceDiagram
    actor Organisaatio
    participant OrganizationUI
    participant FeedbackService
    participant FeedbackRepository

    Organisaatio->>OrganizationUI: valitsee organisaation

    OrganizationUI->>FeedbackService: get_average_ratings(org_id)
    FeedbackService->>FeedbackRepository: get_all()
    FeedbackRepository-->>FeedbackService: Feedback[]
    FeedbackService-->>OrganizationUI: keskiarvot

    OrganizationUI->>FeedbackService: get_average_ratings_by_mood(org_id)
    FeedbackService-->>OrganizationUI: moodikohtaiset keskiarvot

    OrganizationUI-->>Organisaatio: näyttää OrgRatingsView
```
