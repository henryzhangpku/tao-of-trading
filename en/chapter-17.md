# 17. The Best Rulers Are Barely Known

*Part I: The Way · 《太上，下知有之》*

## The Verse

太上，下知有之；其次，亲而誉之；其次，畏之；其次，侮之。

信不足焉，有不信焉。

悠兮其贵言。功成事遂，百姓皆谓我自然。

The best rulers: the people below barely know they exist. The next best: the people love them and praise them. The next: the people fear them. The next: the people despise them.

Where trust is not enough, there is no trust.

Unhurried, they value their words. When the work is done and things have gone well, the people all say: it happened of itself.

*The Chinese is the received Wang Bi text. The translation is the author's own.*

## The Trader

1. The best risk rule is one you rarely feel. It is there on every ticket and decides nothing loudly.

2. The next best is one you are proud of. Pride is noticing it, and noticing is the first step towards arguing with it.

3. The next is one you fear: a limit so tight it hurts every day. You will find a way around it.

4. The worst is one you despise, and override, and keep on the books anyway, so that you can say you have a rule.

5. Where trust is not enough, there is no trust. A rule you trust most days is a rule you will break on the one day it matters.

6. So build the trust before the money. Test the rule forward, on prices nobody has seen, long enough to watch it be wrong and recover. Trust comes from having seen it fail and come back.

7. Put the rule where your hands cannot reach it in the moment. Written down, run on a schedule, sized before the open. A rule that lives in your head will change with your mood.

8. Unhurried, valuing words. Change the rules rarely and in writing, never on a busy morning and never by tapping a screen.

9. When the work is done, it should look as if nothing happened. The good rule leaves no story. The trader says: the day ran itself.

## The Story

When I started building the system that would eventually trade on its own, a friend who trades from his phone asked me for one feature. He wanted to set a little loop running from the phone: watch this price, and when it crosses that level, send the order, then trail the stop up behind it. He wanted it in his pocket. Everyone does. The phone is where we are.

I built it. It took an evening, and that evening it worked beautifully. I stood in the kitchen and watched a test order go out from the phone in my hand at exactly the price I had set, and the stop follow it up, a tick at a time. It felt like the future.

Then I put the phone in my pocket and walked to the shop.

---

A phone does not want to run your loop. It wants to save its battery. When the screen goes dark, the operating system starts deciding which apps may keep working and which must sleep, and it does not consult the trader. On the test account, with the phone in my pocket, the loop stopped somewhere between the front door and the corner. Not with an error. It simply was not running any more, and nothing on the screen said so. When I took the phone out at the till, the app woke, looked at the price and caught up, as if nothing had happened.

Something had. For the length of a walk to the shop, a position on the test account had had a stop that existed only as a hope. If the price had fallen through it while the phone slept, the order would not have gone out. The exit would have been blocked, not by a rule, but by a battery setting.

On the desk, exits are never blocked. Entries are refused for a long list of reasons, thin markets first among them, and I am content for an entry to be refused for any of them. But if the rule says leave, the system leaves. That asymmetry was the first thing I wrote down when I started building, and here I had built, in one evening, a way for it to fail silently in a pocket.

I took the loop out the next day.

---

I could have engineered around it. People do: background permissions, keep-alive tricks, a server to nudge the phone awake. I spent an afternoon reading about them, and the more I read, the more it seemed I was trying to make a phone into something it was not, so that a trader could feel close to the orders. That closeness was the thing I did not want.

What runs the rules now runs in the cloud, on a schedule, on written rules. Entries are sized before the open, from a file. Stops are placed when the trade is placed. Exits run whether or not anyone is looking, whether or not any phone is awake. The phone can see all of it. It shows what the rules did and why, and what they will do next. It can pause everything, because somebody must always be able to stop a machine. What it cannot do is write a rule or move a stop, and it cannot run an order loop of its own. A rule is changed at a desk, after the close, in writing, into the ledger.

My friend was not pleased. He said I had built a trading app that would not let him trade. That was close enough to true that I did not argue.

---

There was a second reason, and I understood it only later. The phone is where the mood lives. It is in your hand in the queue, at dinner, at three in the morning when you cannot sleep. A loop on the phone is a rule within reach of every one of those moments. You will be tempted to nudge the level while you wait for a coffee. You will tighten the stop at dinner because the chart looked tired. A rule that can be touched from anywhere will be touched from everywhere.

*The best rulers: the people below barely know they exist.* A rule I can reach in the moment is a rule I feel all the time. The rules that run in the cloud I barely feel. They are on every ticket and in every exit, and on most days I find out what they did by reading about it afterwards, like news from a province that is well governed.

Some evenings I open the app and read the day's log from the first line to the last. Positions entered at the size the file said. Stops placed with them. One name refused at the open because its spread was too wide. Two exits at the close, on time. Nobody pressed anything. *When the work is done, the people all say: it happened of itself.* It did not happen of itself. It happened because nobody could reach it.

---

[Contents](README.md) · [← 16. Return to the Root](chapter-16.md) · [18. When the Great Way Is Lost →](chapter-18.md)
