import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    sorted_score = scores[['score']].sort_values(by='score', ascending=False).reset_index(drop=True)

    if sorted_score.empty:
        sorted_score['rank'] = []
        return sorted_score

    rank = []
    cur = sorted_score.iloc[0, 0]
    r = 1

    for i in range(len(sorted_score)):
        if cur == sorted_score.iloc[i, 0]:
            rank.append(r)
        else:
            r += 1
            rank.append(r)
            cur = sorted_score.iloc[i, 0]
            
    sorted_score['rank'] = rank
    return sorted_score
