from entities.feedback import Feedback


class FeedbackService:
    """Luokka, joka huolehtii palautteiden logiikasta."""

    def __init__(self, repository, question_repository):
        self._repo = repository
        self._question_repo = question_repository

    def save_feedback(self, org_id, mood, answers):
        """Tallentaa palautteen.

        Args:
            org_id: Palautteen kohteena olevan yrityksen id
            mood: Asiakkaan yleinen päivän fiilis
            answers: Lista kolmen kysymyksen vastauksista asteikolla 1-5 
        """

        fb = Feedback(org_id, mood, answers)
        self._repo.add_fb(fb)

    def get_all(self):
        return self._repo.get_all()

    def get_average_ratings(self, org_id):
        """ Muodostaa keskiarvon jokaisen kysymyksen vastauksesta erikseen.

        Args:
            org_id: Kyseessä olevan organisaation id

        Returns:
            Sanakirjan, jossa avaimena on kysymyksen aihe ja arvona sen vastauksien keskiarvo.
        """
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]
        if not feedbacks:
            return {}

        answer_keys = [q["key"] for q in self.get_questions()]
        total = {key: 0 for key in answer_keys}

        for fb in feedbacks:
            for i, value in enumerate(fb.answers):
                key = answer_keys[i]
                total[key] += value



        return {key: total[key] / len(feedbacks) for key in total}

    def get_average_ratings_by_mood(self, org_id):
        """Muodostaa keskiarvot kysymyskategorioista ja järjestää ne moodin mukaan

        Args:
            org_id: Kyseisen organisaation id

        Returns:
            Palauttaa sanakirjan, jossa avaimena mood ja avaimena toinen sanakirja (avaimena kysymyksen aihe ja arvona ka) 
        """
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]

        if not feedbacks:
            return {}

        mood_grouped_ratings = self._group_by_mood(feedbacks)
        return self._calc_averages(mood_grouped_ratings)

    def _group_by_mood(self, feedbacks):
        mood_grouped_ratings = {}

        for fb in feedbacks:
            if fb.mood not in mood_grouped_ratings:
                mood_grouped_ratings[fb.mood] = []

            mood_grouped_ratings[fb.mood].append(fb.answers)

        return mood_grouped_ratings

    def _calc_averages(self, mood_grouped_ratings):
        answer_keys = [q["key"] for q in self.get_questions()]

        result = {}

        for mood, answer_list in mood_grouped_ratings.items():
            totals = [0] * len(answer_keys)

            for answers in answer_list:
                for i in range(len(answer_keys)):
                    totals[i] += answers[i]

            count = len(answer_list)

            result[mood] = {
                key: totals[i] / count
                for i, key in enumerate(answer_keys)
            }
        return result

    def get_questions(self):
        """Hakee kysymykset kysymysten repositoriosta."""
        return self._question_repo.get_all()

    def calc_overall_rating(self, org_id):
        total = 0
        feedbacks = [fb for fb in self._repo.get_all() if fb.org_id == org_id]
        
        if not feedbacks:
            return {}

        count = len(self.get_questions()) * len(feedbacks)
        
        for fb in feedbacks:
            total += sum(fb.answers)

        return total / count