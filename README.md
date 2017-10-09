# Predicting Success in the UFC

![Red Fighter Wordcloud](https://github.com/spacecadet84/ufc_fight_analysis/blob/master/images/ufc_red_wordcloud.png "Red Fighter Wordcloud")

## Introduction

What does it mean to be the best fighter in the world? Is it the person with the best kick? The best punch? Or is it something else? This project seeks to determine which factors are the best predictors of success in the UFC. It explores every fight since the organization's inception in the hopes of gaining insight into what separates winners and losers. We start with an exploratory visual analysis of all variables before cleaning the data and building our machine learning models. Currently, the algorithms are able to predict the outcome with approximately ~~55-60%~~ ~~57-66%~~ 85-88% accuracy. Our goal is to improve that over time through iteration.

## Background

The Ultimate Fighting Championship (UFC) is a mixed martial arts fighting organization based out of Las Vegas, Nevada. Founded in 1992, it's original goal was to pit fighters from around the world against each other to see which fighting style was the best. In the beginning, there were no rules and there were no weight classes. Eye gouges, groin strikes, headbutts and biting were all legal. Fighters weighing 160 lbs would get tossed in against 400 lbs behemoths. This type of no holds bar contest had never been attempted before and it quickly gained notoriety for its brutality.

It also gave rise to a new way of thinking about fighting. When kung-fu masters, boxers, kickboxers, and karate experts all met for the first time, no one could have predicted the outcome. Most people expected the larger, more gruesome-looking fighters to win. To everyone's shock, it was an unassuming 178 pound man named Royce Gracie who would go on to win the first contest. What was even stranger was that no one could explain how he won the first time (or the second or the third). He didn't pummel his opponent into submission as expected, but instead locked him up using wrestling moves most people hadn't seen before. This was the world's introduction to Brazillian Jiu Jitsu (BJJ).

After Royce went on to win several UFC contests, people began to realize he was not just getting lucky. Fighters started studying this martial art so they could start applying these techniques in their matches or at the very least prevent themselves from being submitted by Royce. Then, they started adding techniques from other fighting styles so that they, too could become the best in the world. This was the beginning of mixed martial arts or MMA. It started out with a multitude of different styles, but a handful started to show up repeatedly: BJJ, wrestling, boxing and kickboxing. Over time, fighters' skill in these 4 areas evolved to where no one art was able to completely dominate the others. 

Now, the UFC is watched by millions worldwide and its support continues to grow. The rules were changed to protect the safety of the fighters. You can no longer gouge your opponent's eyes or pull hair or bite. All fighters are now required to wear standard MMA gloves and shoes are no longer allowed in the octagon. There are now weight classes that range from 115 lbs all the way up to 265. A lot has changed in the UFC and this project seeks to determine which components matter most in a match.

## Data

The data was scraped from www.fightmetrics.com with Beautiful Soup in two stages. The first script compiled a list of event urls and wrote them to a CSV. The second script crawled through those urls and extracted all available fight data into a pandas dataframe. There are 31 features and 8624 records.

During our exploration, we'll examine the data from several perspectives. We'll put it under a microscope through univariate analysis, get a bird's eye view using a correlation matrix and view it from ringside through multivariate analysis.