def seed_ranker(X, y, seed_range):
    """Given an X, target (y) and range to seek, it returns the top 10 performing seeds for the data."""
    seeds = []
    scores = []
    for seed in range (seed_range):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20, random_state=seed)
        lgr = LogisticRegression()
        lgr.fit(X_train, y_train)
        score = lgr.score(X_test,y_test)
        seeds.append(seed)
        scores.append(score)
    scores_df = pd.DataFrame(scores, seeds, columns=['Scores'])
    return scores_df.sort_values("Scores", ascending=False).head(10)