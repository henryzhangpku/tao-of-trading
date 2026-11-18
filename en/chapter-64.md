# 64. The Journey of a Thousand Li

*Part II: The Virtue · 《其安易持》*

## The Verse

其安易持，其未兆易谋。其脆易泮，其微易散。为之于未有，治之于未乱。

合抱之木，生于毫末；九层之台，起于累土；千里之行，始于足下。

为者败之，执者失之。是以圣人无为，故无败；无执，故无失。民之从事，常于几成而败之。慎终如始，则无败事。

是以圣人欲不欲，不贵难得之货；学不学，复众人之所过。以辅万物之自然，而不敢为。

What is at rest is easy to hold. What has not yet shown a sign is easy to plan for. What is brittle is easy to break; what is small is easy to scatter. Act on it before it exists. Put it in order before it falls into disorder.

A tree you cannot reach around grew from a hair-tip. A tower of nine storeys rose from a heap of earth. *The journey of a thousand li commenced with a single step.*

Whoever forces it, ruins it. Whoever grips it, loses it. So the sage does not force, and does not ruin; does not grip, and does not lose. People at their work most often fail when it is nearly done. Be as careful at the end as at the beginning, and nothing will fail.

So the sage wants what others do not want, and does not prize goods that are hard to get. He learns what others do not learn, and goes back to what the crowd has walked past. He helps the ten thousand things be what they are, and does not dare to force them.

*The Chinese is the received Wang Bi text. The translation is the author's own, except the line in italics, which is James Legge's (1891, public domain).*

## The Trader

1. A trade is easiest to hold before it is entered. Before the order there is nothing to defend, and so everything can still be decided: the size, the stop, the day you will leave.

2. What has not yet shown a sign is easy to plan for. Write the exit while the screen is quiet. An exit written during a fall is not a plan. It is a wish holding a pen.

3. A small loss is brittle. It breaks easily, at the price you named. A large loss is not brittle. It has grown roots, and you will find reasons to water it.

4. Put the account in order before it is in disorder. Sizing is the order. Everything after the fill is housekeeping.

5. A tree you cannot reach around grew from a hair-tip. An edge you can trust grew from a test you were willing to run slowly.

6. A tower of nine storeys rose from a heap of earth. A record — on paper or with money — rises one counted day at a time. A day skipped or rewritten is a brick pulled from the bottom.

7. Whoever forces a trade ruins it. The market does not owe you a setup because you have time this morning.

8. Whoever grips a position loses it. The hand that will not open at the stop opens later, wider, at a price it did not choose.

9. Few people fail at the start. They fail when it is nearly done: the forward test in its last weeks, the rule loosened the morning before it would have been proved, the winning trade turned into a losing one by a stop moved out of greed.

10. Be as careful at the end as at the beginning. The exit is an order like any other, and it deserves the attention you gave the entry.

11. Want what others do not want: the boring day, the skipped trade, the test that takes a season.

12. Learn what others do not learn: how to sit still. Go back to what the crowd walked past: the plain rule, written down, left alone.

13. Fast is slow. Slow is fast. The trader who hurries arrives back at the beginning.

## The Story

Every child in China can finish the sentence. You say 千里之行, and a room of nine-year-olds says 始于足下 before you have taken a breath. I learned it the way you learn a multiplication table, as a thing to recite, and for most of my life I thought it was about starting. Take the first step. Get going. It is printed on posters for that reason.

It took me years in markets to notice that the chapter it comes from is not mostly about starting. It is about finishing. *People at their work most often fail when it is nearly done.* The first step is the easy one. The thousandth is where people turn around.

---

The research desk I built works in stages, and the stages are deliberately slow. An idea starts in discovery, which is a crowded room: anything can come in, from a paper, from a hunch, from a language model asked to suggest something. Most ideas die at the door. The door is a set of plain tests that do not care how good the idea sounds. Does it still work after trading costs? After twice the costs? In the first half of the history and in the second half, separately? With its single best month taken out? Every attempt goes into a ledger, failed ones included, so the bar rises with every try. An idea that has been tried forty different ways has to clear a higher bar than one tried once, because forty tries will find something by luck.

A few ideas get through. That is where most people, including the younger version of me, would stop and trade them. The tests are passed. The chart is beautiful. Why wait?

Because every test so far has been run on the past, and the past has been looked at. However careful you are, you have seen the data, and some of what you think is edge is your own eye. The only data you have not seen is the data that has not happened yet.

So the next stage is a forward test, and the forward test has one rule above all the others: the rule being tested is frozen.

Frozen means something exact. The screen is copied as it was recorded, every threshold and every filter, and the copy is pinned by its fingerprint — a hash, a short string of letters and numbers computed from the file. Change one character of the rule, one threshold from 0.30 to 0.31, and the fingerprint changes. A different fingerprint is a different rule, and a different rule is a different test, and its day count starts again at one.

Then you wait. The book of frozen rules is filled each day at the prices of that day, and scored against a random control — the same number of picks, chosen by dice — so that a good market does not look like a good rule. Nobody touches it. For a season.

---

I want to tell you about one of those seasons, because it is the closest I have come to watching this chapter happen to me.

I was up before five, which is when the machine that runs the night's work usually finishes. The coffee and the board come up together. The frozen book had been running for some weeks. The first stretch had been quiet. Then came a bad week, not a disaster, the kind of week every rule has, but bad enough that I opened the trades one by one.

One of them was a trade I would never have taken. You know the kind: the stock had a story I did not like, the chart looked tired, and the rule had bought it anyway, because the rule does not read stories or look at charts the way I do. It had gone down. It was the largest single drag on the week.

And my hand went to the config.

I want to be honest about how reasonable it felt. I was not going to do anything dramatic. I was going to add one filter, a small one, that would have kept that kind of name out. I could even justify it: the filter was sensible, it was the kind of thing I would have put in at the design stage if I had thought of it. It would take ten minutes.

It would also change the fingerprint. The book would no longer be the book I froze. The weeks already run would belong to a rule that no longer existed, and the new rule would start at day one with a filter fitted to exactly one bad week — the most overfitted kind of rule there is, because it was written by a man looking at the loss it was designed to prevent.

*Whoever forces it, ruins it. Whoever grips it, loses it.*

I closed the file.

---

The good idea did not go away, and that is the part of this story I am proudest of, because it is the part that was built in advance rather than willed in the moment.

On the desk, a language model reads the results each morning and is allowed to propose anything. It proposed, that same week, almost exactly the filter I had wanted to add. The model proposes; the rules decide. Its proposal did not go into the frozen book. It went into the ledger as a new trial with its own fingerprint, its own forward test and its own day count starting at one. If it was a good idea, it would prove it the same slow way. If it was not, it would have cost nothing but time.

That is all slow is fast means in practice. It is not a feeling of patience. It is a mechanism that turns every urge to change something into a new beginning instead of a broken ending.

---

The other half of the chapter came near the end of the season.

*Be as careful at the end as at the beginning.* In trading, the end is the exit, and the exit is where people are careless in a particular way: they spend all their attention deciding whether to get in, and then treat getting out as an afterthought, or as a negotiation with themselves.

One of the rules I hold hardest, in everything I have built, is lopsided on purpose. An entry is refused if the market is thin — if the spread is wide, the volume is low, the quote is stale, if there is no one on the other side to take the position back. That is the care at the beginning. But an exit is never blocked. Not by the same checks, not by anything. If the rule says leave, the system leaves, at the best price it can find, even an ugly one.

People ask why the asymmetry. If thin markets are dangerous, why let the exit go through in a thin market? Because the danger is not symmetrical. A refused entry costs you a trade you did not need. A refused exit can cost you the account. A door that opens only one way is not caution. It is a trap with good manners.

Near the end of that season, one of the names in the frozen book opened on a gap, the market for it was thin, and the rule said to sell at the open. Everything in me that likes a good fill wanted to wait for the book to fill in. The rule did not wait. That is what it was for. I do not remember the fill. I remember that I did not have to decide anything, because the deciding had been done months earlier, on a quiet afternoon, when it was easy.

*Act on it before it exists. Put it in order before it falls into disorder.*

---

I am not going to tell you how that frozen book did. That is not what this chapter is about, and a number here would be a performance claim, which this book does not make. What I can tell you is that when the season ended I knew exactly what it had done, because nothing in it had been touched. The record meant what it said. Every brick in the tower was the one that was laid on the day.

Most of what passes for research in trading is a tower built from the top: the conclusion first, then a history found to support it. The fingerprint, the ledger, the random control, the season of waiting — these are just ways of building from the heap of earth upward, one counted day at a time.

It is slower. It is the only way I have found that does not send you back to the beginning.

When I think about the sentence the children recite now, I hear the second half of the chapter under it. The journey of a thousand li begins with a single step. It is finished by the person who does not change the map at li nine hundred.

---

[Contents](README.md) · [← 63. Act Without Acting](chapter-63.md) · [65. The Ancients Did Not Enlighten →](chapter-65.md)
