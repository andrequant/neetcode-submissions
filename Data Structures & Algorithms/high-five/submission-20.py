class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}
        scores_list = []

        for pair in items:
            id_, score = pair
            if id_ not in scores.keys():
                scores[id_] = []
            scores[id_].append(score)

        # scores = dict(sorted(scores.items()))

        for id_, score in scores.items():
            score.sort(reverse=True)
            scores_list.append([id_, sum(score[:5])//5])

        scores_list.sort()
        return scores_list
        