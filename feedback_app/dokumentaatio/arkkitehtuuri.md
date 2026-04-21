# Arkkitehtuuri

``` mermaid
classDiagram
    class Organization {
        id
        name
    }
    class Feedback {
        org_id
        mood
        rating
}

class FeedbackRepository
class FeedbackService

Organization "1" --> Feedback
FeedbackService --> FeedbackRepository
FeedbackRepository --> Feedback
```
