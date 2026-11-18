# 63. Act Without Acting

*Part II: The Virtue · 《为无为》*

## The Verse

为无为，事无事，味无味。大小多少，报怨以德。

图难于其易，为大于其细；天下难事，必作于易；天下大事，必作于细。是以圣人终不为大，故能成其大。

夫轻诺必寡信，多易必多难。是以圣人犹难之，故终无难矣。

Act without acting. Work without working. Taste what has no taste. Treat the small as great and the few as many. Answer resentment with virtue.

Plan the hard while it is easy. Do the great while it is small. The hard things of the world must be done while they are easy; the great things of the world must be done while they are small. So the sage never does great things, and that is how he accomplishes the great.

A light promise is seldom kept. Whoever finds much easy will meet much that is hard. So even the sage treats things as hard, and in the end he has no hardship.

*The Chinese is the received Wang Bi text. The translation is the author's own.*

## The Trader

1. Act without acting. The decisions that matter in a trade are made before the trade exists. After the fill, there should be little left to do.

2. Taste what has no taste. The plain morning check, the size worked out on paper, the log line nobody reads: that is the work.

3. Treat the small as great. A small position gets the whole checklist. Habits are made on small trades and spent on large ones.

4. Answer resentment with virtue. The loss you resent gets the same clean log line as the gain you are proud of.

5. Plan the hard while it is easy. Where to get out is a hard question once you are in. Before the order, it is arithmetic.

6. Do the great while it is small. The stop is placed when the trade is smallest, which is before it has a fill.

7. Every disaster in an account began as a small decision that was put off until later.

8. The sage never does great things. No single trade should be large enough to be a great thing.

9. A light promise is seldom kept. "I will watch it closely" is a light promise. A stop resting in the market is a heavy one.

10. Whoever finds much easy will meet much that is hard. The trade that looks easiest is the one whose size you check twice.

11. Treat it as hard, and in the end there is no hardship. Be tedious on the calm days, so that the wild days have nothing left to decide.

## The Story

Somewhere in every trading system there is a judge: the part that looks at a candidate and says yes or no. In the old days it was a person with a chart. In what I build now, part of the judging is done by a language model, which reads the candidate, the rule it came from and the morning's context, and writes back a short opinion.

This chapter is about the morning I took most of that judge's powers away.

---

The first version of the judge was generous. I had written it a response form with five fields: a verdict, a confidence, a suggested size, a suggested stop and a suggested target. It seemed natural. If you are going to ask something for an opinion, why not ask for the whole opinion?

It ran in shadow for a while. Shadow means it judged every candidate the rules produced, and wrote its answers into a log, and nothing it said touched an order. I read the log each morning before six, when the house is quiet and the night's runs have finished.

One morning I noticed two entries a few days apart that should have been twins. The same rule had produced them. The setups were nearly identical, on paper, number for number. The judge had said yes to both. But it had given the second one a noticeably larger size and a wider stop, and when I read its reasoning, I could see why. The second write-up was more enthusiastic. It had found more to like. The words were warmer, and the numbers had followed the words.

I went back through the log with that in mind, and it was everywhere. Not dramatically. Not in a way that any single entry would show you. But across the weeks, the size and the stop moved with the tone. When the judge argued well for a trade, it sized the trade as if it believed its own argument.

---

I want to be fair to the model, because none of this is a defect peculiar to machines. It is exactly what people do. I have done it. You look at a setup, you build the case for it, and by the time you have built the case you are no longer a neutral party. Then you decide the size. Then you decide the stop. And you decide both as the case's advocate, which is the worst person to ask.

*Plan the hard while it is easy.* The hard questions in a trade are how much and where to get out. They are easy before anyone has argued for the trade, because then they are only arithmetic: the risk you allow per trade, the distance to the stop the rule defines, the size that follows from dividing one by the other. They become hard the moment there is a story. A story wants room. It asks for a slightly wider stop, so that the noise does not shake it out. It asks for a slightly larger size, because this one is better than usual.

The judge had been answering the hard questions at the hardest possible moment: right after it had talked itself into the trade.

---

The change I made that morning was small to look at. I deleted three fields from the response form.

The judge can now say three things: yes, no or wait, with a reason. It cannot say how much. It cannot say where the stop goes. It cannot say where the target is. Those three numbers are computed by plain code, from the rule and the state of the account, before the judge is ever shown the candidate. They are written on the trade card first, and the judge reads them along with everything else, the way a person reviewing a contract reads the price. It may decide the price is wrong and say no. It may not write in a different one.

So the judge can make a trade smaller, by refusing it. It cannot make a trade larger, or looser, by liking it.

I call it the bounded judge, and the bound is the whole design. A judge that can size is an advocate with a pen. A judge that can only veto is a check.

---

The temptation did not stop there, and the next version of it was subtler.

A few weeks later I was reading the log again and thought: the code that sets the stop is crude. It does not know that some mornings are wilder than others. The model does know, or at least it reads the news and the context and can say so. Why not let it adjust the stop a little on wild mornings? Not size, just the stop. A small permission.

*Whoever finds much easy will meet much that is hard.* It would have been easy. One field restored, one sentence in the instructions. And it would have put the advocate's pen back in the advocate's hand, on precisely the mornings when the advocate is most excited.

What I did instead took longer. If wild mornings deserve a different stop, then wildness is a thing that can be measured, and a measurement can go into the formula as code, where it does the same thing every time and can be tested on the history like any other rule. I wrote it that way. It went through the ledger, with its own fingerprint and its own clock, like everything else. The judge still never touches the number. It just reads a number that now knows a little more.

*So even the sage treats things as hard.* That is what treating it as hard meant: not trusting the easy permission, and doing the slow version that can be counted.

---

There is a line in this chapter that I used to skip, because it sounds like a Sunday-school instruction: *answer resentment with virtue.*

The judge made me read it differently. Some mornings the judge says no to a trade, the rule takes no position, and the name goes on to do exactly what the rule hoped. That is a resentful morning. The trade was there, and the machine said no.

The answer to that morning is the same as the answer to every other one. The refusal goes into the log, with its reason, and it is counted with all the other refusals. Some of them will have been right and some wrong, and across enough of them you can see whether the veto earns its place. What you do not do is weaken the veto because of one morning you resent. That is how a check becomes an advocate again, one exception at a time.

---

From the outside, the bounded judge looks like a demotion. It used to set sizes and stops. Now it says yes or no. People who see the design sometimes ask why I would build a capable model and then forbid it from doing the most important part.

But the important part was never the judging. It was the arithmetic, done early, while it was easy and nobody was excited. The model's job is to notice what the rule cannot: the report the screen missed, the reason a name should be left alone this morning. It is very good at that. It is not good at being calm about its own enthusiasm, and neither am I, and that is why neither of us is allowed to set the size after we have fallen for the trade.

*The sage never does great things, and that is how he accomplishes the great.* The judge never sizes a trade. That is why I can trust it to judge one.

---

[Contents](README.md) · [← 62. The Tao Is the Refuge](chapter-62.md) · [64. The Journey of a Thousand Li →](chapter-64.md)
