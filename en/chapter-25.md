# 25. Something Formless

*Part I: The Way · 《有物混成》*

## The Verse

有物混成，先天地生。寂兮寥兮，独立不改，周行而不殆，可以为天下母。

吾不知其名，字之曰道，强为之名曰大。大曰逝，逝曰远，远曰反。

故道大，天大，地大，王亦大。域中有四大，而王居其一焉。

人法地，地法天，天法道，道法自然。

There was something formed out of chaos, born before heaven and earth. Silent and empty, it stands alone and does not change; it goes round everywhere and is never exhausted. It could be the mother of the world.

I do not know its name. I call it "the way", and, if I must name it, I call it "great". Great means going on. Going on means going far. Going far means coming back.

So the way is great, heaven is great, earth is great, and the king is great as well. In the realm there are four great things, and the king is one of them.

People follow the earth. The earth follows heaven. Heaven follows the way. The way follows what is so of itself.

*The Chinese is the received Wang Bi text. The translation is the author's own.*

## The Trader

1. The market has no name for itself. Bull, bear, risk-on, rotation: these are words we write on it afterwards.

2. A regime is named when it is over. While you are inside it, it is formless.

3. I do not know its name; I call it something. Names are fine for talking about markets. They are dangerous for trading them.

4. A rule that needs the regime named before it can act is a rule that waits for the past.

5. Build rules that answer only what can be measured this morning: how far price has been moving, how thin the market is, where the stop belongs.

6. Size by how much it is moving, not by what it is called. A wild market gets a small size whatever its name.

7. Going far means coming back. Every regime leaves and returns in a different coat. A rule that does not need the name does not need to recognise the coat.

8. In the realm there are four great things, and you are not the market. You are one small thing inside it.

9. The way follows what is so of itself. The rule follows price, not the story about price.

10. When you catch yourself arguing about what kind of market this is, check the size, check the stop, and stop arguing.

## The Story

For a few years I began every week by naming the market.

It was a habit from the time I read a great deal about markets and traded mostly by hand. On Sunday evening I wrote a short note to myself about the week ahead, and the first line of the note was a label. *Late-cycle, defensive rotation.* *Risk-on, breadth improving.* *Bear market rally, be careful.* Under the label I wrote which kinds of setups I would trust that week and which I would be wary of. The label came first because everything else followed from it. If I knew what kind of market it was, I thought, I would know how to trade it.

I was proud of those notes. They were careful and they read well. I wrote them for years, and I never read them back.

---

I read them back in the end because of an argument about a name.

A stretch of the market some time earlier had acquired, in the way these things do, a settled name. Everyone now agreed what it had been. It had a label in the articles, a place in the charts people drew, and a tidy story about how it began and how it ended. Someone at dinner used the name in passing, and I realised I had been trading through that stretch and had no memory of calling it that.

So I went back to the Sunday notes for those months and read them in order.

The labels changed almost every few weeks. That was the first thing. Each label was a description of the few weeks just past, written as if it were a forecast of the weeks to come. When the market had fallen for a while, the note said bear. When it had then risen for a while, the note said the bear was over. I had been reading the rear-view mirror and writing *road ahead* at the top of the page.

The second thing was worse. Through the middle of the stretch that everyone now agreed on, my label had been the opposite of the agreed one. I had not been slightly early or slightly late. I had been confidently, carefully wrong, in good sentences, for weeks. And under each wrong label was a list of setups I would trust and setups I would avoid, so the wrong name had not stayed on the page. It had reached into the trading.

*There was something formed out of chaos, born before heaven and earth.* The stretch had been formless while I was in it. The name came later, from people looking back, and it fitted perfectly, because names given afterwards always do.

---

Some time after that, the language model on my research desk proposed a regime filter. It was a sensible-looking idea, the kind I would once have written myself. Classify the market into a few regimes, and let the rule trade only in the ones where it had done well.

It went into the ledger, like everything else, and through the plain tests. I will not give the numbers. I can tell you where the difficulty lay, because I had read it in my own notes first. The regimes in the history had been labelled using the whole history, including the part after each regime ended. In the backtest, the rule always knew what kind of market it was in, because it was told by the future. In real time the labels could only be drawn from the past, and so they arrived late, and changed their minds, the way mine had on Sunday evenings. A rule that needs the regime named before it can act is a rule that waits for the past.

*I do not know its name. I call it "the way".* Laozi does not pretend to know the name. He picks one so that he can talk, and he says that is what he is doing.

---

What I built instead was a set of rules that do not ask.

They ask other things, and only things that can be measured on the morning itself. How widely has this name been swinging lately? The answer sets the size, so a wild market gets a small position whatever anyone is calling it. Is the market in it deep enough to leave? If not, the entry is refused, and the refusal goes in the log with its reason. Where does the stop belong, given the swings? That is arithmetic too. Not one of these questions needs to know whether it is a bull market, a bear market, a rotation or a pause. Each one is answered by price, and price is the only thing that is always there on the morning.

*The way follows what is so of itself.* The rule follows price, and price does not know what it is called.

The rules still have bad stretches, and some of those stretches are exactly the ones that will later be given names. That is not a failure of the design. A rule that never needs the name will still be wrong in a regime it does not suit. The difference is that it will be wrong at a size set by how much the market is moving, rather than by how sure I am of what the market is.

---

I still write a note on Sunday evenings. The first line is gone. Where the label used to be there is nothing, and below it are the things the board will do in the week: what is due to exit, what the rules are watching, what has been refused and why.

Sometimes, in a loud week, I feel the old pull to write a name at the top. I have learned what it is. It is the wish to be the kind of trader who knows. The names come anyway, later, from other people, and they will fit. They always do. *Going far means coming back.* The market will leave and return in a different coat, and someone will name the coat, and the rules will go on measuring the swings, sizing the position, placing the stop, without needing to recognise it.

---

[Contents](README.md) · [← 24. Standing on Tiptoe](chapter-24.md) · [26. Heavy Is the Root of Light →](chapter-26.md)
