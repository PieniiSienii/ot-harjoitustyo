# Arkkitehtuuri

``` mermaid
classDiagram
    class Feedback {
        org_id
        mood
        rating
}

class FeedbackRepository
class FeedbackService

FeedbackService --> FeedbackRepository
FeedbackRepository --> Feedback
```