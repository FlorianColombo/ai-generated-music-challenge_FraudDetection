#!/usr/bin/env python
import pickle
import trueskill


logs = pickle.load(open("meta/FILTERED_LOGS.pkl"))
scores = {}

for _idx, _log in enumerate(logs):

    sub_1 = int(_log['submission_1'])
    sub_2 = int(_log['submission_2'])

    winner = _log['winner']

    try:
        score_1 = scores[sub_1]
    except:
        score_1 = trueskill.Rating()

    try:
        score_2 = scores[sub_2]
    except:
        score_2 = trueskill.Rating()

    if winner == 0:
        n_score_1, n_score_2 = trueskill.rate_1vs1(
            score_1,
            score_2
        )
    else:
        n_score_2, n_score_1 = trueskill.rate_1vs1(
            score_2,
            score_1
        )

    scores[sub_1] = n_score_1
    scores[sub_2] = n_score_2

    print _idx

env = trueskill.global_env()
output = open("new_scores.csv","w")
output.write("submission_id, score, mu, sigma\n")
for _idx, _key in enumerate(scores):
    output.write("{}, {}, {}, {}\n".format(_key, env.expose(scores[_key]), scores[_key].mu, scores[_key].sigma))
    print "Writing : ",_idx

output.close()
print("submission_id, score, mu, sigma\n")
print (scores.key())
for _idx, _key in enumerate(scores):
    print("{}, {}, {}, {}\n".format(_key, env.expose(scores[_key]), scores[_key].mu, scores[_key].sigma))
